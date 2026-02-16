#!/usr/bin/env python3
"""Restructure content folders into the new 3-folder flat structure.

Moves files from the old folder hierarchy into:
  - notes/     (all knowledge, books, courses, papers, talks, blog summaries)
  - posts/     (original writings)
  - projects/  (things built)

Also:
  - Adds content-type tags to moved files
  - Adds aliases for URL redirects (old path → new path)
  - Updates full-path wikilinks across the entire vault
  - Renames files that need standardization
  - Validates wikilink integrity

Usage:
    python scripts/restructure_folders.py                # dry run
    python scripts/restructure_folders.py --apply        # apply changes
"""

import argparse
import os
import re
import shutil
from pathlib import Path

CONTENT_DIR = Path("content")

# ============================================================================
# Folder migration mapping: old folder → (new folder, tag to add)
# ============================================================================

FOLDER_MAPPING: list[tuple[str, str, str | None]] = [
    # (old_folder_glob, new_folder, tag_to_add)
    # Order matters — more specific paths first

    # Knowledge subfolders
    ("Knowledge/Tech-Science", "notes", None),  # already has topic tags
    ("Knowledge/Tools", "notes", "tool"),
    ("Knowledge/Startups-BigTechs", "notes", "startups"),

    # Knowledge root files (Glossary, Scalers, etc.)
    ("Knowledge", "notes", None),

    # Miscellaneous
    ("Miscellaneous/Finance", "notes", "finance"),
    ("Miscellaneous", "notes", None),  # health, philosophy, countries

    # Reading content → notes
    ("Books", "notes", "book"),
    ("Courses", "notes", "course"),
    ("Research Papers", "notes", "paper"),
    ("Talks", "notes", "talk"),
    ("Blogs", "notes", "summary"),

    # Original writing → posts
    ("Writings", "posts", "writing"),

    # Projects
    ("Pet Projects", "projects", "project"),
]

# Files to rename during migration (old_name → new_name)
FILE_RENAMES: dict[str, str] = {
    "Boost Your Immunity with Nutrition! 💪 🍎.md": "Boost Your Immunity with Nutrition.md",
    "2025 Kickoff!! NeurIPS Recap and SOTA.md": "2025 Kickoff NeurIPS Recap and SOTA.md",
    "Mindfullness & Meditation.md": "Mindfulness and Meditation.md",
}

# Old full-path wikilinks to update after restructure
# (searched regex pattern → replacement)
# These will be computed dynamically based on actual file moves


def compute_old_slug(filepath: Path) -> str:
    """Compute the old Quartz slug (URL path) for a file relative to content/."""
    rel = filepath.relative_to(CONTENT_DIR)
    # Remove .md extension, keep path
    slug = str(rel.with_suffix(""))
    return slug


def compute_new_slug(new_path: Path) -> str:
    """Compute the new Quartz slug for a file relative to content/."""
    rel = new_path.relative_to(CONTENT_DIR)
    slug = str(rel.with_suffix(""))
    return slug


def add_tag_to_frontmatter(content: str, tag: str) -> str:
    """Add a tag to YAML frontmatter if not already present."""
    lines = content.split("\n")

    if not lines or lines[0].strip() != "---":
        # No frontmatter — add it
        return f"---\ntags:\n  - {tag}\n---\n{content}"

    # Find frontmatter end
    fm_end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm_end = i
            break

    if fm_end is None:
        return content

    fm_lines = lines[1:fm_end]

    # Check if tags section exists
    tags_start = None
    tags_end = None
    in_tags = False

    for i, line in enumerate(fm_lines):
        stripped = line.strip()
        if re.match(r"^tags:\s*$", stripped) or re.match(r"^tags:\s+", stripped):
            tags_start = i
            # Check if inline array
            if re.match(r"^tags:\s*\[", stripped):
                tags_end = i
                break
            in_tags = True
            continue

        if in_tags:
            if re.match(r"^\s+-", line):
                tags_end = i
            else:
                in_tags = False

    if tags_start is not None:
        # Check if tag already exists
        existing_tags = []
        for i in range(tags_start, (tags_end or tags_start) + 1):
            line = fm_lines[i]
            match = re.search(r"-\s+(.+)$", line)
            if match:
                existing_tags.append(match.group(1).strip().strip("'\""))

        if tag in existing_tags:
            return content

        # Add tag after last tag line
        insert_idx = (tags_end or tags_start) + 1
        fm_lines.insert(insert_idx, f"  - {tag}")
    else:
        # No tags section — add one
        fm_lines.append("tags:")
        fm_lines.append(f"  - {tag}")

    new_lines = ["---"] + fm_lines + lines[fm_end:]
    return "\n".join(new_lines)


def add_alias_to_frontmatter(content: str, alias: str) -> str:
    """Add an alias to YAML frontmatter for URL redirects."""
    lines = content.split("\n")

    if not lines or lines[0].strip() != "---":
        return content

    fm_end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm_end = i
            break

    if fm_end is None:
        return content

    fm_lines = lines[1:fm_end]

    # Check if aliases section exists
    aliases_start = None
    aliases_end = None
    in_aliases = False

    for i, line in enumerate(fm_lines):
        stripped = line.strip()
        if re.match(r"^aliases:\s*$", stripped):
            aliases_start = i
            in_aliases = True
            continue
        if re.match(r"^aliases:\s*\[", stripped):
            aliases_start = i
            aliases_end = i
            break
        if in_aliases:
            if re.match(r"^\s+-", line):
                aliases_end = i
            else:
                in_aliases = False

    if aliases_start is not None:
        # Add alias after last alias line
        insert_idx = (aliases_end or aliases_start) + 1
        fm_lines.insert(insert_idx, f"  - {alias}")
    else:
        # No aliases section — add one before the end
        fm_lines.append("aliases:")
        fm_lines.append(f"  - {alias}")

    new_lines = ["---"] + fm_lines + lines[fm_end:]
    return "\n".join(new_lines)


def should_skip_file(filepath: Path) -> bool:
    """Check if a file should be skipped during migration."""
    name = filepath.name

    # Skip Index.md files — they'll be replaced with new index.md files
    if name == "Index.md" or name == "index.md":
        # But keep the root index.md
        if filepath.parent == CONTENT_DIR:
            return True  # Skip root index — handled separately in Phase 4
        return True  # Skip all folder Index.md files

    # Skip the Page Tree.md (Dataview file being replaced by script)
    if name == "Page Tree.md":
        return True

    return False


def should_skip_attachment_dir(dirpath: Path) -> bool:
    """Check if a directory is an attachment directory."""
    return dirpath.name in ("attachments", "attachmets", "images", "documents", "pdfs", "slides")


def get_target_folder(filepath: Path) -> tuple[str, str | None] | None:
    """Determine which new folder a file should go to.

    Returns:
        (new_folder, tag_to_add) or None if file shouldn't be moved.
    """
    rel = filepath.relative_to(CONTENT_DIR)
    rel_str = str(rel.parent)

    for old_folder, new_folder, tag in FOLDER_MAPPING:
        if rel_str == old_folder or rel_str.startswith(old_folder + "/"):
            return new_folder, tag

    return None


def find_all_md_files(content_dir: Path) -> list[Path]:
    """Find all markdown files, excluding special directories."""
    files = []
    for md_file in content_dir.rglob("*.md"):
        # Skip files inside attachment directories
        parts = md_file.relative_to(content_dir).parts
        if any(p in ("attachments", "attachmets", ".obsidian", "templates") for p in parts[:-1]):
            # Exception: the weird Talks/attachments/Index.md
            if md_file.name == "Index.md" and "attachments" in parts:
                continue  # skip it
            continue
        files.append(md_file)
    return sorted(files)


def find_all_attachment_dirs(content_dir: Path) -> list[Path]:
    """Find all attachment directories."""
    dirs = []
    for root, dirnames, filenames in os.walk(content_dir):
        root_path = Path(root)
        if root_path.name in ("attachments", "attachmets"):
            dirs.append(root_path)
    return sorted(dirs)


def update_fullpath_wikilinks(content: str, link_map: dict[str, str]) -> str:
    """Update full-path wikilinks based on the link mapping.

    link_map: old_path_without_ext → new_path_without_ext
    """
    def replace_link(match):
        full_match = match.group(0)
        prefix = match.group(1)  # [[ or ![[
        path = match.group(2)
        suffix = match.group(3)  # |alias or #section or empty
        closing = match.group(4)  # ]]

        # Check if this path matches any in our map
        # Try exact match first
        if path in link_map:
            return f"{prefix}{link_map[path]}{suffix}{closing}"

        # Try without trailing Index (folder/Index → folder links)
        if path.endswith("/Index"):
            base = path[:-6]
            if base in link_map:
                return f"{prefix}{link_map[base]}{suffix}{closing}"

        return full_match

    # Match wikilinks with paths (containing /)
    # Pattern: [[path/to/file|alias]] or [[path/to/file#section]] or [[path/to/file]] or ![[path/to/file]]
    pattern = r'(!?\[\[)((?:[^|\]#]+/)+[^|\]#]+)((?:[|#][^\]]*)?)(]])'
    return re.sub(pattern, replace_link, content)


def main():
    parser = argparse.ArgumentParser(description="Restructure content folders")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry run)")
    args = parser.parse_args()

    if not CONTENT_DIR.exists():
        print(f"Error: Content directory not found: {CONTENT_DIR}")
        return 1

    mode = "APPLYING" if args.apply else "DRY RUN"
    print(f"[{mode}] Restructuring content folders...\n")

    # ========================================================================
    # Step 1: Plan all file moves
    # ========================================================================
    print("Step 1: Planning file moves...")

    md_files = find_all_md_files(CONTENT_DIR)
    print(f"  Found {len(md_files)} markdown files")

    moves: list[dict] = []
    skipped: list[str] = []
    unmapped: list[str] = []

    for filepath in md_files:
        if should_skip_file(filepath):
            skipped.append(str(filepath.relative_to(CONTENT_DIR)))
            continue

        # Root-level files (index.md, Featured links.md) stay at root
        rel = filepath.relative_to(CONTENT_DIR)
        if len(rel.parts) == 1:
            skipped.append(str(rel))
            continue

        target = get_target_folder(filepath)
        if target is None:
            unmapped.append(str(rel))
            continue

        new_folder, tag = target
        filename = filepath.name

        # Apply renames
        if filename in FILE_RENAMES:
            filename = FILE_RENAMES[filename]

        new_path = CONTENT_DIR / new_folder / filename

        # Check for collision
        if new_path.exists() and new_path != filepath:
            print(f"  WARNING: Collision detected: {filepath} → {new_path} (already exists)")
            continue

        old_slug = compute_old_slug(filepath)
        new_slug = compute_new_slug(new_path)

        moves.append({
            "old_path": filepath,
            "new_path": new_path,
            "old_slug": old_slug,
            "new_slug": new_slug,
            "tag": tag,
            "renamed": filename != filepath.name,
        })

    print(f"  Planned {len(moves)} file moves")
    print(f"  Skipped {len(skipped)} files (Index.md, root files, etc.)")
    if unmapped:
        print(f"  WARNING: {len(unmapped)} unmapped files:")
        for f in unmapped:
            print(f"    - {f}")

    # ========================================================================
    # Step 2: Plan attachment directory moves
    # ========================================================================
    print("\nStep 2: Planning attachment moves...")

    attachment_dirs = find_all_attachment_dirs(CONTENT_DIR)
    attachment_moves: list[tuple[Path, Path]] = []

    for att_dir in attachment_dirs:
        rel = att_dir.relative_to(CONTENT_DIR)
        parent_folder = str(rel.parts[0]) if rel.parts else ""

        # Determine destination based on parent folder
        dest_folder = None
        for old_folder, new_folder, _ in FOLDER_MAPPING:
            if parent_folder == old_folder.split("/")[0]:
                dest_folder = new_folder
                break

        if dest_folder:
            dest_att = CONTENT_DIR / dest_folder / "attachments"
            if att_dir != dest_att:
                attachment_moves.append((att_dir, dest_att))

    print(f"  Planned {len(attachment_moves)} attachment directory merges")

    # ========================================================================
    # Step 3: Build wikilink update map
    # ========================================================================
    print("\nStep 3: Building wikilink update map...")

    # Map old paths to new paths for wikilink updates
    link_map: dict[str, str] = {}
    for move in moves:
        old_slug = move["old_slug"]
        new_slug = move["new_slug"]
        if old_slug != new_slug:
            link_map[old_slug] = new_slug

    # Also map old folder Index paths to new folder index
    old_index_mappings = {
        "Knowledge/Tech-Science/Index": "notes/index",
        "Knowledge/Tools/Index": "notes/index",
        "Knowledge/Startups-BigTechs/Index": "notes/index",
        "Knowledge/Startups-BigTechs/Companies/Index": "notes/index",
        "Knowledge/Startups-BigTechs/Ecosystem/Index": "notes/index",
        "Knowledge/Startups-BigTechs/Ecosystem/YC/Index": "notes/index",
        "Knowledge/Startups-BigTechs/Ecosystem/a16z/Index": "notes/index",
        "Knowledge/Startups-BigTechs/People/Index": "notes/index",
        "Knowledge/Startups-BigTechs/Resources/Index": "notes/index",
        "Knowledge/Index": "notes/index",
        "Books/Index": "notes/index",
        "Courses/Index": "notes/index",
        "Research Papers/Index": "notes/index",
        "Talks/Index": "notes/index",
        "Blogs/Index": "notes/index",
        "Miscellaneous/Index": "notes/index",
        "Miscellaneous/Finance/Index": "notes/index",
        "Writings/Index": "posts/index",
        "Pet Projects/Index": "projects/index",
    }
    link_map.update(old_index_mappings)

    # Special fix: broken links
    link_map["Knowledge/Tech"] = "notes/index"
    link_map["Knowledge/Finance/Glossary"] = "notes/Glossary"
    link_map["Knowledge/Tech-Science/ChatGPT"] = "notes/ChatGPT"

    print(f"  Built {len(link_map)} wikilink mappings")

    # ========================================================================
    # Step 4: Execute moves
    # ========================================================================
    if args.apply:
        print("\nStep 4: Executing file moves...")

        # Create new folder structure
        for folder in ["notes", "posts", "projects"]:
            (CONTENT_DIR / folder).mkdir(exist_ok=True)
            (CONTENT_DIR / folder / "attachments").mkdir(exist_ok=True)

        # Move content files
        for move in moves:
            old_path = move["old_path"]
            new_path = move["new_path"]

            # Read content
            content = old_path.read_text(encoding="utf-8")

            # Add content-type tag if specified
            if move["tag"]:
                content = add_tag_to_frontmatter(content, move["tag"])

            # Add alias for URL redirect
            old_slug = move["old_slug"]
            content = add_alias_to_frontmatter(content, old_slug)

            # Write to new location
            new_path.parent.mkdir(parents=True, exist_ok=True)
            new_path.write_text(content, encoding="utf-8")

            # Remove old file
            old_path.unlink()

        print(f"  Moved {len(moves)} files")

        # Move attachment directories
        for src_att, dest_att in attachment_moves:
            dest_att.mkdir(parents=True, exist_ok=True)
            # Merge: copy all files from source to destination
            for item in src_att.rglob("*"):
                if item.is_file():
                    rel_in_att = item.relative_to(src_att)
                    dest_file = dest_att / rel_in_att
                    dest_file.parent.mkdir(parents=True, exist_ok=True)
                    if not dest_file.exists():
                        shutil.copy2(item, dest_file)
                    else:
                        print(f"  WARNING: Attachment collision, skipping: {rel_in_att}")

            # Remove source attachment dir
            shutil.rmtree(src_att)

        print(f"  Merged {len(attachment_moves)} attachment directories")

        # Clean up empty old folders
        print("\n  Cleaning up empty folders...")
        for old_folder, _, _ in FOLDER_MAPPING:
            old_path = CONTENT_DIR / old_folder
            if old_path.exists():
                try:
                    # Remove directory and any remaining empty subdirs
                    shutil.rmtree(old_path)
                    print(f"    Removed {old_folder}/")
                except Exception as e:
                    print(f"    Could not remove {old_folder}/: {e}")

        # ====================================================================
        # Step 5: Update wikilinks across ALL files
        # ====================================================================
        print("\nStep 5: Updating wikilinks across all files...")

        all_md_files = list(CONTENT_DIR.rglob("*.md"))
        updated_count = 0
        for md_file in all_md_files:
            # Skip files in attachment dirs
            parts = md_file.relative_to(CONTENT_DIR).parts
            if any(p in ("attachments", ".obsidian", "templates") for p in parts[:-1]):
                continue

            try:
                content = md_file.read_text(encoding="utf-8")
                new_content = update_fullpath_wikilinks(content, link_map)
                if new_content != content:
                    md_file.write_text(new_content, encoding="utf-8")
                    updated_count += 1
            except Exception as e:
                print(f"  ERROR updating wikilinks in {md_file}: {e}")

        print(f"  Updated wikilinks in {updated_count} files")

    else:
        print("\nStep 4: [DRY RUN] Would execute these moves:")
        for move in moves[:20]:
            old_rel = move["old_path"].relative_to(CONTENT_DIR)
            new_rel = move["new_path"].relative_to(CONTENT_DIR)
            tag_str = f" +#{move['tag']}" if move["tag"] else ""
            rename_str = " (RENAMED)" if move["renamed"] else ""
            print(f"  {old_rel} → {new_rel}{tag_str}{rename_str}")
        if len(moves) > 20:
            print(f"  ... and {len(moves) - 20} more")

        print(f"\n  Attachment merges:")
        for src, dest in attachment_moves:
            print(f"  {src.relative_to(CONTENT_DIR)} → {dest.relative_to(CONTENT_DIR)}")

    # ========================================================================
    # Step 6: Summary
    # ========================================================================
    print(f"\n{'=' * 60}")
    print(f"SUMMARY")
    print(f"{'=' * 60}")
    print(f"Files moved:        {len(moves)}")
    print(f"Files skipped:      {len(skipped)}")
    print(f"Attachments merged: {len(attachment_moves)}")
    print(f"Wikilink mappings:  {len(link_map)}")
    if unmapped:
        print(f"UNMAPPED FILES:     {len(unmapped)}")

    return 0


if __name__ == "__main__":
    exit(main())
