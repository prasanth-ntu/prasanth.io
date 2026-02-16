#!/usr/bin/env python3
"""Generate structure statistics and visualizations for the prasanth.io blog.

Produces a markdown file with:
- ASCII directory tree with file counts
- Mermaid mindmap of folder hierarchy
- Stats tables (files per folder, tag distribution, size distribution)
- Quality audit (missing tags/frontmatter, drafts)

Usage:it makes sense.
    python scripts/blog_stats.py                                  # stdout
    python scripts/blog_stats.py --output content/notes/Page Tree.md
    python scripts/blog_stats.py --format mermaid|ascii|all
"""

import argparse
import re
from collections import defaultdict
from pathlib import Path


def parse_frontmatter(content: str) -> dict:
    """Extract frontmatter fields from markdown content."""
    result = {"tags": [], "draft": False, "title": None}

    if not content.startswith("---"):
        return result

    lines = content.split("\n")
    fm_end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm_end = i
            break

    if fm_end is None:
        return result

    fm_lines = lines[1:fm_end]
    in_tags = False

    for line in fm_lines:
        stripped = line.strip()

        if stripped.startswith("draft:") and "true" in stripped.lower():
            result["draft"] = True

        if stripped.startswith("title:"):
            result["title"] = stripped[6:].strip().strip("'\"")

        if re.match(r"^tags:\s*$", stripped):
            in_tags = True
            continue

        if in_tags:
            if re.match(r"^\s+-\s+", line):
                tag_val = re.sub(r"^\s*-\s*", "", line).strip().strip("'\"")
                if tag_val:
                    result["tags"].append(tag_val)
            else:
                in_tags = False

    return result


def analyze_content(content_dir: Path) -> dict:
    """Analyze all markdown files in the content directory."""
    stats = {
        "total_files": 0,
        "total_chars": 0,
        "by_folder": defaultdict(lambda: {"files": 0, "chars": 0}),
        "tag_counts": defaultdict(int),
        "files_without_tags": [],
        "files_without_frontmatter": [],
        "draft_files": [],
        "documents": [],
    }

    for md_file in sorted(content_dir.rglob("*.md")):
        # Skip files in special directories
        rel = md_file.relative_to(content_dir)
        parts = rel.parts
        if any(
            p in ("attachments", ".obsidian", ".smart-env", "templates", "paige-ai-report", "quartz")
            for p in parts
        ):
            continue

        try:
            text = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        char_count = len(text)
        fm = parse_frontmatter(text)

        folder = parts[0] if len(parts) > 1 else "root"

        stats["total_files"] += 1
        stats["total_chars"] += char_count
        stats["by_folder"][folder]["files"] += 1
        stats["by_folder"][folder]["chars"] += char_count

        for tag in fm["tags"]:
            stats["tag_counts"][tag] += 1

        if not fm["tags"]:
            stats["files_without_tags"].append(str(rel))

        if not text.startswith("---"):
            stats["files_without_frontmatter"].append(str(rel))

        if fm["draft"]:
            stats["draft_files"].append(str(rel))

        stats["documents"].append({
            "path": str(rel),
            "folder": folder,
            "chars": char_count,
            "tags": fm["tags"],
            "draft": fm["draft"],
        })

    return stats


def generate_ascii_tree(content_dir: Path) -> str:
    """Generate an ASCII directory tree with file counts."""
    lines = ["```"]
    lines.append(f"content/")

    folders = {}
    for md_file in sorted(content_dir.rglob("*.md")):
        rel = md_file.relative_to(content_dir)
        parts = rel.parts
        if any(
            p in ("attachments", ".obsidian", ".smart-env", "templates", "paige-ai-report", "quartz")
            for p in parts
        ):
            continue
        folder = parts[0] if len(parts) > 1 else "root"
        folders.setdefault(folder, 0)
        folders[folder] += 1

    # Root files
    root_count = folders.pop("root", 0)
    if root_count:
        lines.append(f"├── ({root_count} root files)")

    # Folders
    folder_list = sorted(folders.items())
    for i, (folder, count) in enumerate(folder_list):
        prefix = "└──" if i == len(folder_list) - 1 else "├──"
        att_dir = content_dir / folder / "attachments"
        att_count = sum(1 for _ in att_dir.rglob("*") if _.is_file()) if att_dir.exists() else 0
        att_str = f" + {att_count} attachments" if att_count else ""
        lines.append(f"{prefix} {folder}/ ({count} files{att_str})")

    lines.append("```")
    return "\n".join(lines)


def generate_mermaid_mindmap(stats: dict) -> str:
    """Generate a Mermaid mindmap of the folder structure."""
    lines = ["```mermaid", "mindmap", "  root((prasanth.io))"]

    for folder in sorted(stats["by_folder"].keys()):
        if folder == "root":
            continue
        data = stats["by_folder"][folder]
        lines.append(f"    {folder}")
        lines.append(f"      {data['files']} files")

    lines.append("```")
    return "\n".join(lines)


def generate_tag_chart_html(sorted_tags: list[tuple[str, int]], top_n: int = 15) -> str:
    """Generate a self-contained Plotly.js HTML chart for tag usage."""
    tags = [t for t, _ in sorted_tags[:top_n]]
    counts = [c for _, c in sorted_tags[:top_n]]
    # Build JSON arrays inline
    import json
    tags_json = json.dumps(tags)
    counts_json = json.dumps(counts)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Top {top_n} Tags by Usage</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
  body {{ margin: 0; background: transparent; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }}
  #chart {{ width: 100%; height: 100vh; min-height: 400px; }}
</style>
</head>
<body>
<div id="chart"></div>
<script>
const tags = {tags_json};
const counts = {counts_json};
const colors = counts.map((_, i) => {{
  const t = i / (counts.length - 1);
  const r = Math.round(66 + t * 40);
  const g = Math.round(133 + t * 60);
  const b = Math.round(244 - t * 120);
  return `rgb(${{r}},${{g}},${{b}})`;
}});

Plotly.newPlot('chart', [{{
  x: tags,
  y: counts,
  type: 'bar',
  marker: {{ color: colors, line: {{ color: 'rgba(255,255,255,0.3)', width: 1 }} }},
  hovertemplate: '<b>%{{x}}</b><br>Count: %{{y}}<extra></extra>'
}}], {{
  title: {{ text: 'Top {top_n} Tags by Usage', font: {{ size: 18 }} }},
  xaxis: {{
    tickangle: -45,
    tickfont: {{ size: 12 }},
    automargin: true
  }},
  yaxis: {{
    title: 'Count',
    gridcolor: 'rgba(128,128,128,0.2)'
  }},
  plot_bgcolor: 'rgba(0,0,0,0)',
  paper_bgcolor: 'rgba(0,0,0,0)',
  margin: {{ t: 50, b: 120, l: 60, r: 20 }},
  hoverlabel: {{ bgcolor: '#333', font: {{ color: '#fff' }} }}
}}, {{
  responsive: true,
  displayModeBar: false
}});
</script>
</body>
</html>"""


def generate_report(stats: dict, content_dir: Path, fmt: str = "all") -> str:
    """Generate the full markdown report."""
    report = []
    report.append("---")
    report.append("title: Blog Structure & Stats")
    report.append("---")
    report.append("")
    report.append("> [!info] Auto-generated")
    report.append("> This page is auto-generated by [`blog_stats.py`](https://github.com/prasanth-ntu/prasanth.io/blob/v4/scripts/blog_stats.py). Do not edit manually.")
    report.append("")
    report.append(f"**Total files:** {stats['total_files']}  ")
    report.append(f"**Total characters:** {stats['total_chars']:,}  ")
    report.append(f"**Unique tags:** {len(stats['tag_counts'])}  ")
    report.append(f"**Drafts:** {len(stats['draft_files'])}")
    report.append("")

    # ASCII tree
    if fmt in ("ascii", "all"):
        report.append("## Directory Tree\n")
        report.append(generate_ascii_tree(content_dir))
        report.append("")

    # Mermaid mindmap
    if fmt in ("mermaid", "all"):
        report.append("## Structure Overview\n")
        report.append(generate_mermaid_mindmap(stats))
        report.append("")

    # Files per folder table
    report.append("## Files per Folder\n")
    report.append("| Folder | Files | % of Total | Characters |")
    report.append("|--------|-------|------------|------------|")
    for folder in sorted(stats["by_folder"].keys(), key=lambda f: stats["by_folder"][f]["files"], reverse=True):
        data = stats["by_folder"][folder]
        pct = data["files"] / stats["total_files"] * 100
        report.append(f"| {folder} | {data['files']} | {pct:.1f}% | {data['chars']:,} |")
    report.append("")

    # Tag distribution (top 30)
    report.append("## Tag Distribution (Top 30)\n")
    report.append("| Tag | Count | % of Files |")
    report.append("|-----|-------|------------|")
    sorted_tags = sorted(stats["tag_counts"].items(), key=lambda x: x[1], reverse=True)
    for tag, count in sorted_tags[:30]:
        pct = count / stats["total_files"] * 100
        report.append(f"| `{tag}` | {count} | {pct:.1f}% |")
    report.append("")

    # Interactive Plotly bar chart for tags
    if sorted_tags:
        report.append("## Tag Usage Chart\n")
        report.append('<iframe src="/static/pages/tag-usage-chart.html" width="100%" height="450" frameborder="0" loading="lazy"></iframe>')
        report.append("")

    # Document size distribution
    report.append("## Document Size Distribution\n")
    size_buckets = {
        "Tiny (< 500 chars)": 0,
        "Small (500-2K chars)": 0,
        "Medium (2K-5K chars)": 0,
        "Large (5K-10K chars)": 0,
        "Very Large (> 10K chars)": 0,
    }
    for doc in stats["documents"]:
        chars = doc["chars"]
        if chars < 500:
            size_buckets["Tiny (< 500 chars)"] += 1
        elif chars < 2000:
            size_buckets["Small (500-2K chars)"] += 1
        elif chars < 5000:
            size_buckets["Medium (2K-5K chars)"] += 1
        elif chars < 10000:
            size_buckets["Large (5K-10K chars)"] += 1
        else:
            size_buckets["Very Large (> 10K chars)"] += 1

    report.append("| Size Category | Count | % |")
    report.append("|---------------|-------|---|")
    for category, count in size_buckets.items():
        pct = count / stats["total_files"] * 100 if stats["total_files"] else 0
        report.append(f"| {category} | {count} | {pct:.1f}% |")
    report.append("")

    # Quality audit
    report.append("## Quality Audit\n")
    report.append(f"**Files without tags:** {len(stats['files_without_tags'])}")
    if stats["files_without_tags"]:
        for f in sorted(stats["files_without_tags"])[:20]:
            report.append(f"- `{f}`")
        if len(stats["files_without_tags"]) > 20:
            report.append(f"- ... and {len(stats['files_without_tags']) - 20} more")
    report.append("")

    report.append(f"**Files without frontmatter:** {len(stats['files_without_frontmatter'])}")
    if stats["files_without_frontmatter"]:
        for f in sorted(stats["files_without_frontmatter"])[:20]:
            report.append(f"- `{f}`")
        if len(stats["files_without_frontmatter"]) > 20:
            report.append(f"- ... and {len(stats['files_without_frontmatter']) - 20} more")
    report.append("")

    report.append(f"**Draft files:** {len(stats['draft_files'])}")
    if stats["draft_files"]:
        for f in sorted(stats["draft_files"]):
            report.append(f"- `{f}`")
    report.append("")

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="Generate blog structure statistics")
    parser.add_argument(
        "--content-dir",
        default="content",
        help="Path to content directory (default: content)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output file path (default: print to stdout)",
    )
    parser.add_argument(
        "--format",
        choices=["mermaid", "ascii", "all"],
        default="all",
        help="Output format (default: all)",
    )
    args = parser.parse_args()

    content_path = Path(args.content_dir)
    if not content_path.exists():
        print(f"Error: Content directory not found: {args.content_dir}")
        return 1

    print(f"Analyzing content in {args.content_dir}...")
    stats = analyze_content(content_path)
    print(f"Found {stats['total_files']} files with {len(stats['tag_counts'])} unique tags")

    report = generate_report(stats, content_path, args.format)

    # Generate interactive chart HTML
    sorted_tags = sorted(stats["tag_counts"].items(), key=lambda x: x[1], reverse=True)
    if sorted_tags:
        chart_html = generate_tag_chart_html(sorted_tags)
        chart_dir = Path("quartz/static/pages")
        chart_dir.mkdir(parents=True, exist_ok=True)
        chart_path = chart_dir / "tag-usage-chart.html"
        chart_path.write_text(chart_html, encoding="utf-8")
        print(f"Chart saved to {chart_path}")

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Report saved to {args.output}")
    else:
        print("\n" + report)

    return 0


if __name__ == "__main__":
    exit(main())
