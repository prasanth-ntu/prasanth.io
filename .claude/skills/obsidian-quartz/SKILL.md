---
name: obsidian-quartz
description: >-
  Manage the Obsidian vault published via Quartz at prasanth.io.
  Creates, edits, and organizes Markdown notes following vault conventions
  for file naming, frontmatter, tags, wikilinks, callouts, and directory placement.
  Use when creating notes, editing vault content, adding glossary entries,
  updating index.md pages, cross-linking notes, advising on naming conventions
  or tag usage, querying vault structure, or working with the Quartz
  build and deploy pipeline.
---

# Obsidian Vault for prasanth.io (Quartz)

Conventions for an Obsidian vault published as a Quartz 4 static site. Vault root: `content/`. Branch: `v4`.

**Build commands:**
- Dev server: `npm run dev` or `npm run serve`
- Production build: `npm run build` (runs prebuild scripts automatically)
- Sync to remote: `npm run sync`

## Directory placement

3 content folders, all flat (no subfolders). Tags handle all categorization.

| Folder | Path | What goes here | Tags to add |
|---|---|---|---|
| Notes | `content/notes/` | All knowledge: tech concepts, tool guides, book notes, course notes, paper notes, talk notes, blog summaries, finance, health, startups | Topic tags + content-type tags (`book`, `course`, `paper`, `talk`, `summary`, `tool`) |
| Posts | `content/posts/` | Original writings, reflections, essays | `writing` |
| Projects | `content/projects/` | Personal software project documentation | `project` |

**Root-level files:**
- `content/index.md` — Homepage / content hub
- `content/about.md` — CV / resume
- `content/Featured links.md` — Curated navigation links

Each folder has an `attachments/` subdirectory for images/media and an `index.md` hub page.

**Decision guide:** "Where does this file go?"
- Did I learn something? → `notes/`
- Did I write something original? → `posts/`
- Did I build something? → `projects/`

## File naming rules

1. **Title Case with spaces** (primary convention): `Atomic Habits.md`, `The Psychology of Money.md`
2. **Date prefix for writings** in Posts: `2025-02-01 Reflections on Meeting with Magesh.md`
3. **Author-first for research papers**: `A Vaswani - Attention Is All You Need - 2017.md`
4. **Provider prefix for courses**: `DeepLearning.AI - Multi AI Agent Systems with CrewAI.md`
5. **Exchange format for finance**: `Tesla (NASDAQ - TSLA).md`
6. **No emoji** in filenames
7. **No trailing punctuation** (no `!!`, trailing `?`, etc.)
8. Use `and` instead of `&` in filenames
9. **Never use** kebab-case or snake_case for content files
10. Index pages are always lowercase `index.md`

## Frontmatter conventions

All frontmatter fields are optional. The vault uses a flexible, metadata-light approach.

- `tags` is the most common field. Always use a YAML array with **lowercase kebab-case** tags:
  ```yaml
  tags:
    - machine-learning
    - data-science
    - book
  ```
- **Canonical tag vocabulary** (~35 tags):
  - *Domain*: `ai`, `machine-learning`, `deep-learning`, `data-science`, `nlp`, `llm`, `gen-ai`, `software-engineering`, `devops`, `python`, `statistics`, `gpu`, `spark`, `sql`
  - *Content type*: `book`, `course`, `paper`, `talk`, `project`, `tool`, `writing`, `summary`
  - *Topic*: `finance`, `startups`, `health`, `science`, `self-improvement`, `open-source`, `ai-agents`, `prompting`, `infrastructure`, `optimization`, `documentation`, `learning`
  - *Source*: `google`, `anthropic`, `openai`, `hugging-face`, `grab`
- `author` — for books, papers, blog summaries (the original author, not vault owner)
- `date` — ISO format `YYYY-MM-DD`, mainly on blog summaries
- `description` — blog posts and collection pages
- `draft: true` — hides page from published site (Quartz `RemoveDrafts` filter)
- `title` — only when display title differs from filename
- `aliases` — for URL redirects from old paths (Quartz `AliasRedirects` plugin)

## Wikilink and linking conventions

- **Internal links**: `[[Note Name]]` — CrawlLinks uses `shortest` path resolution
- **With alias**: `[[notes/index|Notes]]` or `[[Full Path/Note|Display Text]]`
- **Section links**: `[[Glossary#Accuracy]]` or `[[Note Name#Section]]`
- **Image embeds**: `![[image-name.png]]` (from folder's `attachments/` directory)
- **Image with size**: `![[image.png||700]]` (Obsidian width syntax)
- **PDF embeds**: `![[file.pdf]]`
- **No leading slashes** in wikilink paths
- Full path needed only for disambiguation (e.g., `[[notes/index|Notes]]` vs `[[projects/index|Projects]]`); otherwise shortest path works
- No duplicate filenames exist (except `index.md` per folder), so shortest path is always unambiguous

## Content templates

### Knowledge note (in `notes/`)

```markdown
---
tags:
  - topic-tag
  - another-tag
---
> [!TIP] **Mental model:** One-line conceptual summary

## Content with headers, code blocks, callouts
```

### Book note (in `notes/`)

```markdown
---
tags:
  - book
  - topic-tag
author: Author Full Name
---

| | |
| ------------------- | --- |
| Original source | [Source](URL) |
| My annotated source | [GDrive](URL) |
| Status | #Completed |

# Chapter/Section content...
```

### Course note (in `notes/`)

```markdown
---
tags:
  - course
  - data-science
  - provider-tag
draft: true
---
**Key resources**
- Course [link](URL)
- My Github Repo [link](URL)

Below sections contain the key take aways from each lesson.

---
# Lesson content...
```

### Research paper note (in `notes/`)

```markdown
---
tags:
  - paper
  - topic-tag
---

| | |
| ------------------- | --- |
| Original source | [arXiv](URL) |
| My annotated source | [GDrive](URL) |
| Status | #Todo |
```

Filename: `Author Lastname - Title - Year.md`

### Blog summary (in `notes/`)

```markdown
---
tags:
  - summary
  - topic-tag
description: Summarised the key points from the blog post by *Author Name* about "Topic"
author: Author Name
date: YYYY-MM-DD
---

| Author | Author Name |
| ------ | ----------- |
| Source | [source-name](URL) |

> [!SUMMARY] Key takeaway in one sentence

---
# Section Heading
Content...
```

### Talk/event note (in `notes/`)

```markdown
---
tags:
  - talk
  - topic-tag
  - organiser-tag
date: YYYY-MM-DD
event: Full Event Name
organiser: Organiser Name
location: Venue — Address
speakers:
  - Speaker One
  - Speaker Two
draft: true
aliases:
  - Talks/YYYY-MM-DD Organiser - Event Name
---

[Event link](URL) | [Photos](URL)

**Agenda**

- **HH:MM AM – HH:MM AM** _Talk Title_ — Speaker Name

---
# Talk Title — Speaker Name

> Synopsis as blockquote

- Bullet-point notes

---
# Key Takeaways

-

---
# Action Items

- [ ]

---
# Resources / Links

-
```

Filename: `YYYY-MM-DD Organiser - Event Name.md` (date prefix for chronological sorting, consistent with posts convention).

### Original writing (in `posts/`)

```markdown
---
tags:
  - writing
  - topic-tag
---

Content...
```

Filename: `YYYY-MM-DD Title.md`

### Glossary entry (in `notes/Glossary.md`)

Entries are under alphabetical letter headings (`# A`, `# B`, etc.). Each entry:

```markdown
## Term Name
#inlineTag1 #inlineTag2

Definition paragraph.

**Example**: Usage in a sentence.
```

Note: Glossary uses **inline hashtags** after the `##` heading, NOT frontmatter tags.

## Callout syntax

Common callout types in this vault:
```
> [!SUMMARY] Brief summary
> [!QUOTE] Quoted text with attribution
> [!INFO] Informational note
> [!TIP] Practical advice
> [!HINT] Subtle guidance
> [!IMPORTANT] Key takeaway
> [!WARNING] Caution or counterpoint
> [!TODO] Action item (often with "TBA")
> [!ERROR] Error or anti-pattern
> [!Question] Open question
```

## Special syntax

- **Highlights**: `==highlighted text==`
- **Inline status tags**: `#Completed`, `#InProgress`, `#Todo`, `#Draft`, `#WIP` (used in metadata tables, NOT in frontmatter)
- **Colored text**: `<span style="color:green">text</span>`, `<span style="color:red">text</span>`
- **LaTeX math**: `$inline$` and `$$block$$` (rendered via KaTeX)
- **Mermaid diagrams**: ` ```mermaid ` blocks (timeline, graph TD, flowchart)
- **Footnotes**: `[^1]` with `[^1]: definition` at end
- **Checkboxes**: `- [ ]` unchecked, `- [x]` checked

## Quartz build pipeline

- **Prebuild**: `scripts/sync-slideshow.sh` and `scripts/sync-html.sh` run automatically before build
- **Draft filtering**: `RemoveDrafts` plugin excludes files with `draft: true`
- **Ignored patterns**: `private`, `templates`, `.obsidian` directories are excluded from build
- **Static paths**: Links starting with `/static/` bypass Quartz slug processing (custom modification in `quartz/plugins/transformers/links.ts`)
- **Link resolution**: CrawlLinks uses `shortest` path strategy — wikilinks resolve to the shortest matching path
- **URL redirects**: `AliasRedirects` plugin generates redirect pages for `aliases` in frontmatter
- **OG images**: `CustomOgImages()` plugin generates social media previews (slow; comment out in `quartz.config.ts` for faster dev builds)
- **Date priority**: `CreatedModifiedDate` uses frontmatter > git > filesystem

## Common operations

### Adding a glossary entry
1. Open `content/notes/Glossary.md`
2. Find the correct alphabetical section (`# A`, `# B`, etc.)
3. Add `## Term Name`, inline hashtags, definition, and optional example
4. Cross-link to concept pages if they exist: `[[Concept Page Name]]`

### Creating a new note
1. All new files go in `content/notes/` (unless it's an original writing → `posts/` or a project → `projects/`)
2. Use Title Case with spaces for the filename
3. Apply the appropriate frontmatter template for the content type
4. Add relevant tags from the canonical vocabulary (lowercase kebab-case)
5. Use wikilinks for internal references

### Marking content as draft
Set `draft: true` in frontmatter. This prevents Quartz from publishing the page.

### Adding an image
1. Place the image in the folder's `attachments/` subdirectory
2. Reference with `![[image-name.png]]` or `![[image-name.png||700]]` for sized display
