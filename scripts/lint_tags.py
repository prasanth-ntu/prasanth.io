#!/usr/bin/env python3
"""Lint frontmatter and inline tags for kebab-case compliance.

Checks that all tags (both YAML frontmatter and inline #hashtags) are
lowercase kebab-case. Exits non-zero if violations are found.

Usage:
    python scripts/lint_tags.py              # check and report
    python scripts/lint_tags.py --fix        # auto-fix known violations
"""

import argparse
import re
import sys
from pathlib import Path

# Known inline tag mappings (old → new). Extend as needed.
INLINE_TAG_FIXES: dict[str, str] = {
    "machinelearning": "machine-learning",
    "datascience": "data-science",
    "softwareengineering": "software-engineering",
    "artificialintelligence": "ai",
    "deeplearning": "deep-learning",
    "dataengineering": "data-engineering",
    "informationretrieval": "information-retrieval",
    "openaccess": "open-access",
    "techology": "technology",
    "MachineLearning": "machine-learning",
    "MLEngineering": "ml-engineering",
    "InterviewPrep": "interview-prep",
    "DataAnalytics": "data-analytics",
    "DataScience": "data-science",
    "CareerGrowth": "career-growth",
    "ResearchPaper": "research-paper",
    "International": "international",
    "OpenSource": "open-source",
    "Programming": "programming",
    "Embeddings": "embeddings",
    "Investment": "investment",
    "Statistics": "statistics",
    "Singapore": "singapore",
    "Startup": "startups",
    "Coding": "coding",
    "DevOps": "devops",
    "Python": "python",
    "Stocks": "stocks",
    "India": "india",
    "Math": "math",
    "GAI": "gen-ai",
    "AGI": "agi",
    "NLP": "nlp",
    "LLM": "llm",
    "AI": "ai",
}

# Status tags are intentionally PascalCase — skip them
STATUS_TAGS = {
    "Completed", "InProgress", "Todo", "ToRead",
    "Listened", "Attended", "ToListen", "WIP", "Draft",
}

# Patterns that look like tags but aren't (CSS hex, SVG IDs, etc.)
FALSE_POSITIVES = {
    "f", "e", "a", "b", "c", "d",
    "fff", "ffffff", "dfd", "cbd", "gradient",
}
FALSE_POSITIVE_PREFIXES = ("export-svg", "image-", "image_", "tasktype")


def is_false_positive(tag: str) -> bool:
    lower = tag.lower()
    return (
        lower in FALSE_POSITIVES
        or any(lower.startswith(p) for p in FALSE_POSITIVE_PREFIXES)
    )


def is_valid_tag(tag: str) -> bool:
    """Check if a tag is valid lowercase kebab-case."""
    return bool(re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", tag))


def check_frontmatter_tags(content: str) -> list[str]:
    """Return list of non-compliant frontmatter tags."""
    if not content.startswith("---"):
        return []
    end = content.find("\n---", 3)
    if end == -1:
        return []
    fm = content[3:end]

    tags = []
    in_tags = False
    for line in fm.split("\n"):
        stripped = line.strip()
        if re.match(r"^tags:\s*$", stripped):
            in_tags = True
            continue
        if in_tags:
            m = re.match(r"^\s+-\s+(.+)$", stripped)
            if m:
                tags.append(m.group(1).strip().strip("'\""))
            else:
                in_tags = False
        elif stripped.startswith("tags:"):
            # inline: tags: [a, b] or tags: single
            inline = re.match(r"^tags:\s*\[(.+)\]", stripped)
            if inline:
                tags.extend(t.strip().strip("'\"") for t in inline.group(1).split(","))
            else:
                val = stripped.split(":", 1)[1].strip().strip("'\"")
                if val:
                    tags.append(val)

    return [t for t in tags if not is_valid_tag(t)]


def check_inline_tags(content: str) -> list[tuple[int, str]]:
    """Return list of (line_number, tag) for non-compliant inline hashtags."""
    # Skip frontmatter
    body = content
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            body = content[end + 4:]

    violations = []
    for i, line in enumerate(body.split("\n"), start=1):
        # Skip code blocks (basic heuristic)
        if line.strip().startswith("```"):
            continue
        for m in re.finditer(r"(?:^|(?<=\s))#([A-Za-z][A-Za-z0-9_-]*)", line):
            tag = m.group(1)
            if is_false_positive(tag) or tag in STATUS_TAGS:
                continue
            if not is_valid_tag(tag):
                violations.append((i, tag))
    return violations


def fix_inline_tags(content: str) -> str:
    """Apply known inline tag fixes."""
    for old, new in INLINE_TAG_FIXES.items():
        pattern = r"#" + re.escape(old) + r"(?![A-Za-z0-9_-])"
        content = re.sub(pattern, "#" + new, content)
    return content


def main():
    parser = argparse.ArgumentParser(description="Lint tags for kebab-case compliance")
    parser.add_argument("--content-dir", default="content", help="Content directory")
    parser.add_argument("--fix", action="store_true", help="Auto-fix known violations")
    args = parser.parse_args()

    content_path = Path(args.content_dir)
    if not content_path.exists():
        print(f"Error: {args.content_dir} not found")
        return 1

    md_files = sorted(content_path.rglob("*.md"))
    total_violations = 0
    files_with_issues = 0

    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        rel = md_file.relative_to(content_path)

        fm_issues = check_frontmatter_tags(text)
        inline_issues = check_inline_tags(text)

        if fm_issues or inline_issues:
            files_with_issues += 1

            if args.fix:
                text = fix_inline_tags(text)
                md_file.write_text(text, encoding="utf-8")
                # Re-check after fix
                inline_issues = check_inline_tags(text)

            if fm_issues:
                for tag in fm_issues:
                    print(f"  {rel}: frontmatter tag '{tag}' is not kebab-case")
                    total_violations += 1

            if inline_issues:
                for lineno, tag in inline_issues:
                    print(f"  {rel}:{lineno}: inline tag '#{tag}' is not kebab-case")
                    total_violations += 1

    if total_violations > 0:
        action = "remaining after fix" if args.fix else "found"
        print(f"\n{total_violations} tag violations {action} in {files_with_issues} files.")
        if not args.fix:
            print("Run with --fix to auto-fix known violations, or update INLINE_TAG_FIXES in scripts/lint_tags.py.")
        return 1
    else:
        print(f"All tags OK across {len(md_files)} files.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
