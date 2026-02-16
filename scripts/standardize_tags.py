#!/usr/bin/env python3
"""Standardize frontmatter tags across all content markdown files.

Applies a canonical tag mapping (old inconsistent tags → new kebab-case tags),
removes placeholder text, deduplicates, and writes back.

Usage:
    python scripts/standardize_tags.py                    # dry run (report only)
    python scripts/standardize_tags.py --apply            # apply changes
    python scripts/standardize_tags.py --report report.md # save report to file
"""

import argparse
import re
from pathlib import Path

# ============================================================================
# Canonical tag mapping: old (inconsistent) → new (lowercase kebab-case)
# ============================================================================
# Multiple old tags can map to the same canonical tag.
# Keys are CASE-INSENSITIVE (the script lowercases before lookup).

TAG_MAPPING: dict[str, str] = {
    # --- Domain: AI & ML ---
    "datascience": "data-science",
    "dataanalytics": "data-science",
    "machinelearning": "machine-learning",
    "machinelearningengineering": "machine-learning",
    "ml": "machine-learning",
    "artificialintelligence": "ai",
    "ai": "ai",
    "agi": "ai",
    "deeplearning": "deep-learning",
    "deeplearningai": "deep-learning",
    "neuralnetworks": "deep-learning",
    "llm": "llm",
    "gai": "gen-ai",
    "nlp": "nlp",
    "embeddings": "nlp",
    "aiagent": "ai-agents",
    "agents": "ai-agents",
    "promptingtechniques": "prompting",
    "optimizationtechniques": "optimization",
    "featurescaling": "machine-learning",

    # --- Domain: Software Engineering ---
    "softwareengineering": "software-engineering",
    "software engineering": "software-engineering",
    "programming": "software-engineering",
    "coding": "software-engineering",
    "metaprogramming": "software-engineering",
    "python": "python",
    "#python": "python",
    "sql": "sql",
    "devops": "devops",
    "infrastructure": "infrastructure",
    "cloud": "infrastructure",
    "mlops": "devops",
    "versioncontrol": "devops",
    "gpu": "gpu",
    "spark": "spark",
    "hive": "sql",
    "postgresql": "sql",
    "database": "sql",
    "jupyter": "python",
    "notebooks": "python",
    "numpy": "python",
    "pandas": "python",
    "pytorch": "deep-learning",
    "http": "software-engineering",
    "error": "software-engineering",
    "codes": "software-engineering",
    "protocol": "software-engineering",
    "authentication": "software-engineering",
    "token": "software-engineering",
    "logging": "software-engineering",
    "logs": "software-engineering",
    "opensearch": "software-engineering",
    "search": "software-engineering",

    # --- Content type ---
    "book": "book",
    "books": "book",
    "reading": "book",
    "course": "course",
    "researchpaper": "paper",
    "talks": "talk",
    "projects": "project",
    "tool": "tool",
    "library": "tool",

    # --- Topic: Finance ---
    "finance": "finance",
    "investment": "finance",
    "stocks": "finance",
    "trading": "finance",
    "money": "finance",
    "market": "finance",
    "banking": "finance",
    "retirement": "finance",

    # --- Topic: Health & Science ---
    "healthcare": "health",
    "healthtech": "health",
    "medicine": "health",
    "medical": "health",
    "disease": "health",
    "syndrome": "health",
    "pathology": "health",
    "cancer": "health",
    "newborn": "health",
    "baby": "health",
    "parenting": "health",
    "child": "health",
    "fitness": "health",
    "biology": "science",
    "science": "science",
    "neurology": "science",
    "psychology": "science",

    # --- Topic: Startups & Business ---
    "startup": "startups",
    "startups": "startups",
    "entrepreneurship": "startups",
    "business": "startups",
    "siliconvalley": "startups",
    "yc": "startups",
    "accelerator": "startups",
    "vc": "startups",
    "a16z": "startups",
    "growth": "startups",

    # --- Topic: Self-improvement ---
    "habits": "self-improvement",
    "self-help": "self-improvement",
    "improvement": "self-improvement",

    # --- Topic: Other ---
    "opensource": "open-source",
    "openaccess": "open-source",
    "statistics": "statistics",
    "math": "statistics",
    "documentation": "documentation",
    "standards": "documentation",

    # --- Source/Company ---
    "google": "google",
    "googledevelopersspace": "google",
    "gemini": "google",
    "anthropic": "anthropic",
    "openai": "openai",
    "gpt": "openai",
    "huggingface": "hugging-face",
    "crewai": "ai-agents",
    "grab": "grab",

    # --- Tools/IDE ---
    "ide": "tool",
    "vscode": "tool",
    "mac": "tool",
    "obsidian": "tool",
    "quartz": "tool",
    "pkm": "tool",
    "github": "tool",
    "shortcuts": "tool",

    # --- Media/Content ---
    "podcast": "talk",
    "webinar": "talk",
    "meetup": "talk",
    "youtube": "talk",
    "music": "misc",
    "fiction": "book",
    "fantasy": "book",
    "memoir": "book",
    "tamil": "misc",
    "singapore": "misc",

    # --- Misc ---
    "analytics": "data-science",
    "concepts": "learning",
    "learning": "learning",
    "ideas": "learning",
    "hacks": "learning",
    "future": "misc",
    "media": "misc",
    "converter": "tool",
    "image": "misc",
    "video": "misc",
    "chatbot": "ai-agents",
    "gist": "misc",
    "portfolio": "misc",
    "development": "software-engineering",
    "review": "misc",
    "assessment": "misc",
    "paige": "project",
    "slideshow": "misc",
    "translation": "nlp",
    "scripts": "software-engineering",
    "#todo": "draft",
    "todo": "draft",

    # --- Speakers (map to talk or remove) ---
    "ilyasutskever": "talk",
    "andrejkarpathy": "talk",
    "machinelearningsingapore": "talk",
    "neurips": "talk",
}

# Tags to completely remove (placeholder text, not real tags)
TAGS_TO_REMOVE: set[str] = {
    "[other relevant tags]",
    "other relevant tags",
}

# Tags that should pass through as-is (already canonical or intentionally kept)
# If a tag isn't in TAG_MAPPING and isn't in TAGS_TO_REMOVE, it gets lowered+kebab-cased
PASSTHROUGH_TAGS: set[str] = set()


def parse_frontmatter(content: str) -> tuple[dict | None, str, str]:
    """Parse YAML frontmatter from markdown content.

    Returns:
        (frontmatter_dict, frontmatter_raw, body) or (None, "", content) if no frontmatter
    """
    if not content.startswith("---"):
        return None, "", content

    # Find the closing ---
    end_match = re.search(r"\n---\s*\n", content[3:])
    if not end_match:
        return None, "", content

    fm_end = end_match.start() + 3  # offset from start of content
    fm_raw = content[3 : fm_end + 1].strip()
    body = content[fm_end + 4 + end_match.end() - end_match.start() :]

    # Actually let's be more precise
    lines = content.split("\n")
    fm_start = 0
    fm_end_line = None

    if lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                fm_end_line = i
                break

    if fm_end_line is None:
        return None, "", content

    fm_lines = lines[1:fm_end_line]
    body_lines = lines[fm_end_line + 1 :]

    return fm_lines, "\n".join(lines[: fm_end_line + 1]), "\n".join(body_lines)


def extract_tags_from_frontmatter(fm_lines: list[str]) -> tuple[list[str], list[int]]:
    """Extract tags from frontmatter lines.

    Returns:
        (list of tag values, list of line indices in fm_lines that contain tag data)
    """
    tags = []
    tag_line_indices = []
    in_tags = False

    for i, line in enumerate(fm_lines):
        stripped = line.strip()

        # Check for inline array: tags: [tag1, tag2]
        inline_match = re.match(r"^tags:\s*\[(.+)\]\s*$", stripped)
        if inline_match:
            raw = inline_match.group(1)
            # Split by comma, strip whitespace and quotes
            for t in raw.split(","):
                t = t.strip().strip("'\"").strip()
                if t:
                    tags.append(t)
            tag_line_indices.append(i)
            continue

        # Check for tags: followed by nothing (YAML list follows)
        if re.match(r"^tags:\s*$", stripped):
            in_tags = True
            tag_line_indices.append(i)
            continue

        # Check for tags: with a single value
        single_match = re.match(r"^tags:\s+(.+)$", stripped)
        if single_match and not single_match.group(1).startswith("["):
            val = single_match.group(1).strip().strip("'\"")
            if val:
                tags.append(val)
            tag_line_indices.append(i)
            continue

        # If we're in the tags list, look for "  - tag" entries
        if in_tags:
            list_match = re.match(r"^\s+-\s+(.+)$", stripped)
            if list_match or re.match(r"^\s+-\s+", line):
                tag_val = re.sub(r"^\s*-\s*", "", line).strip().strip("'\"")
                if tag_val:
                    tags.append(tag_val)
                tag_line_indices.append(i)
            else:
                # No longer in tags section
                in_tags = False

    return tags, tag_line_indices


def canonicalize_tag(tag: str) -> str | None:
    """Map a tag to its canonical form.

    Returns:
        Canonical tag string, or None if the tag should be removed.
    """
    # Check for removal
    if tag.lower().strip() in TAGS_TO_REMOVE:
        return None

    # Strip leading # if present
    clean = tag.strip()
    if clean.startswith("#"):
        clean = clean[1:]

    # Look up in mapping (case-insensitive)
    lookup = clean.lower().replace(" ", "").replace("-", "")
    # Try exact lowercase first
    lower = clean.lower().replace(" ", "")
    if lower in TAG_MAPPING:
        return TAG_MAPPING[lower]

    # Try with no separators
    if lookup in TAG_MAPPING:
        return TAG_MAPPING[lookup]

    # Try the original lowercase
    if clean.lower() in TAG_MAPPING:
        return TAG_MAPPING[clean.lower()]

    # Not in mapping — convert to kebab-case
    # Insert hyphens before uppercase letters (camelCase → camel-case)
    kebab = re.sub(r"(?<=[a-z])(?=[A-Z])", "-", clean)
    kebab = kebab.lower().replace(" ", "-").replace("_", "-")
    # Collapse multiple hyphens
    kebab = re.sub(r"-+", "-", kebab).strip("-")
    return kebab


def rebuild_frontmatter(fm_lines: list[str], tag_line_indices: list[int],
                         new_tags: list[str]) -> str:
    """Rebuild frontmatter with new tags, preserving other fields."""
    result_lines = []

    # Remove old tag lines
    tag_indices_set = set(tag_line_indices)
    first_tag_idx = min(tag_line_indices) if tag_line_indices else len(fm_lines)

    inserted = False
    for i, line in enumerate(fm_lines):
        if i in tag_indices_set:
            if not inserted:
                # Insert new tags at the position of the first old tag line
                if new_tags:
                    result_lines.append("tags:")
                    for t in sorted(new_tags):
                        result_lines.append(f"  - {t}")
                inserted = True
            continue
        result_lines.append(line)

    # If there were no tag lines but we have tags to add
    if not tag_line_indices and new_tags:
        result_lines.append("tags:")
        for t in sorted(new_tags):
            result_lines.append(f"  - {t}")

    return "---\n" + "\n".join(result_lines) + "\n---"


def process_file(filepath: Path, apply: bool = False) -> dict | None:
    """Process a single markdown file.

    Returns:
        Dict with change info, or None if no changes needed.
    """
    content = filepath.read_text(encoding="utf-8")

    fm_lines, fm_raw, body = parse_frontmatter(content)
    if fm_lines is None:
        return None

    tags, tag_line_indices = extract_tags_from_frontmatter(fm_lines)
    if not tags and not tag_line_indices:
        return None

    # Map old tags to new
    old_tags = list(tags)
    new_tags_set: set[str] = set()
    removed: list[str] = []
    mapped: list[tuple[str, str]] = []

    for tag in old_tags:
        canonical = canonicalize_tag(tag)
        if canonical is None:
            removed.append(tag)
        elif canonical != tag:
            mapped.append((tag, canonical))
            new_tags_set.add(canonical)
        else:
            new_tags_set.add(tag)

    new_tags = sorted(new_tags_set)

    # Check if anything changed
    if sorted(old_tags) == new_tags and not removed:
        return None

    change = {
        "file": str(filepath),
        "old_tags": old_tags,
        "new_tags": new_tags,
        "removed": removed,
        "mapped": mapped,
    }

    if apply:
        new_fm = rebuild_frontmatter(fm_lines, tag_line_indices, new_tags)
        new_content = new_fm + "\n" + body
        filepath.write_text(new_content, encoding="utf-8")
        change["applied"] = True

    return change


def generate_report(changes: list[dict], total_files: int) -> str:
    """Generate a markdown report of all changes."""
    report = []
    report.append("# Tag Standardization Report\n")
    report.append(f"**Total files scanned:** {total_files}")
    report.append(f"**Files with tag changes:** {len(changes)}\n")

    # Summary of all mappings applied
    all_mappings: dict[str, set[str]] = {}
    for change in changes:
        for old, new in change["mapped"]:
            if new not in all_mappings:
                all_mappings[new] = set()
            all_mappings[new].add(old)

    report.append("## Tag Mappings Applied\n")
    report.append("| New Tag | Old Tags Replaced |")
    report.append("|---------|------------------|")
    for new_tag in sorted(all_mappings.keys()):
        old_tags = ", ".join(sorted(all_mappings[new_tag]))
        report.append(f"| `{new_tag}` | {old_tags} |")

    # Tags removed
    all_removed = set()
    for change in changes:
        all_removed.update(change["removed"])
    if all_removed:
        report.append(f"\n## Tags Removed\n")
        for tag in sorted(all_removed):
            report.append(f"- `{tag}`")

    # Per-file details
    report.append("\n## Per-File Changes\n")
    for change in changes:
        rel_path = change["file"]
        report.append(f"### `{rel_path}`")
        report.append(f"- **Before:** {', '.join(change['old_tags'])}")
        report.append(f"- **After:** {', '.join(change['new_tags'])}")
        if change["removed"]:
            report.append(f"- **Removed:** {', '.join(change['removed'])}")
        report.append("")

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="Standardize frontmatter tags")
    parser.add_argument(
        "--content-dir",
        default="content",
        help="Path to content directory (default: content)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes (default: dry run)",
    )
    parser.add_argument(
        "--report",
        default=None,
        help="Save report to file (default: print to stdout)",
    )
    args = parser.parse_args()

    content_path = Path(args.content_dir)
    if not content_path.exists():
        print(f"Error: Content directory not found: {args.content_dir}")
        return 1

    md_files = sorted(content_path.rglob("*.md"))
    print(f"Scanning {len(md_files)} markdown files...")

    changes = []
    for md_file in md_files:
        change = process_file(md_file, apply=args.apply)
        if change:
            changes.append(change)

    mode = "APPLIED" if args.apply else "DRY RUN"
    print(f"\n[{mode}] {len(changes)} files {'modified' if args.apply else 'would be modified'}")

    report = generate_report(changes, len(md_files))

    if args.report:
        Path(args.report).write_text(report, encoding="utf-8")
        print(f"Report saved to {args.report}")
    else:
        print("\n" + report)

    return 0


if __name__ == "__main__":
    exit(main())
