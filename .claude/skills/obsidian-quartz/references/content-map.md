# Content Directory Map

## Full directory tree

```
content/
├── index.md                              # Site homepage (personal bio, professional journey)
├── Featured links.md                     # Curated cross-reference hub (wikilinks by category)
├── Blogs/                                # Summaries of external blog posts/newsletters
│   ├── Index.md                          # Hub (longform frontmatter only)
│   ├── attachments/                      # Blog-related images
│   └── *.md                              # Individual blog summaries
├── Books/                                # Book notes and summaries
│   ├── Index.md                          # Hub (longform frontmatter only)
│   ├── My Book Collection.md             # Gallery page with HTML cards (special format)
│   ├── attachments/images/               # Book cover images (.webp preferred)
│   └── *.md                              # Individual book notes
├── Courses/                              # Online course notes
│   ├── Index.md                          # Hub
│   └── *.md                              # Course notes (provider prefix naming)
├── Knowledge/                            # Reference materials and glossaries
│   ├── Index.md                          # Hub (links to Tech, Tools, Startups)
│   ├── Glossary.md                       # Master glossary (alphabetical sections)
│   ├── Scalers.md                        # ML scalers reference
│   ├── Tech-Science/                     # Technical concepts (largest subdirectory)
│   │   ├── *.md                          # Concept pages (Docker, Transformer Model, etc.)
│   │   └── *.html                        # Architecture diagrams (synced to static/)
│   ├── Tools/                            # Software tool guides
│   │   ├── Index.md                      # Hub
│   │   ├── attachments/                  # Tool screenshots
│   │   └── *.md                          # Tool pages (Claude Code, Obsidian, etc.)
│   └── Startups-BigTechs/               # Business/startup ecosystem
│       ├── Index.md                      # Hub
│       ├── Companies/                    # Company profiles
│       │   ├── Index.md
│       │   └── CompanyName/             # Deep-dives (e.g., Paige-AI/ with slideshow)
│       ├── People/                       # Notable person profiles
│       │   └── *.md                      # Person pages (Sam Altman, etc.)
│       ├── Ecosystem/                    # VCs, accelerators
│       │   ├── YC/
│       │   ├── a16z/
│       │   └── Breyer Capital/
│       └── Resources/                    # Curated resource lists
├── Miscellaneous/                        # Varied topics
│   ├── Index.md                          # Hub
│   ├── Philosophy.md                     # Quotes and philosophical notes
│   ├── Places to visit and explore.md
│   ├── Miscellaneous.md                  # Catch-all
│   ├── Finance/                          # Financial topics
│   │   ├── Index.md
│   │   ├── attachments/
│   │   └── *.md                          # Stock notes, market analysis
│   ├── Countries/                        # Country info pages
│   │   └── *.md                          # Singapore, Malaysia, Australia
│   └── attachments/
├── Pet Projects/                         # Personal project documentation
│   ├── Index.md                          # Hub
│   ├── My Project Collection.md          # Gallery page with HTML cards (special format)
│   ├── attachments/images/               # Project thumbnails
│   └── *.md                              # Individual project docs
├── Research Papers/                      # Academic paper notes
│   ├── Index.md                          # Hub
│   └── *.md                              # Paper notes (Author - Title - Year format)
├── Talks/                                # Conference and meetup notes
│   ├── attachments/
│   └── *.md                              # Talk/meetup notes
└── Writings/                             # Personal reflections and essays
    ├── Index.md                          # Hub (has body content with categories)
    └── *.md                              # Date-prefixed writings
```

## Placement decision guide

When creating a new note, use this logic:

1. **Summary of an external blog post or newsletter?** → `content/Blogs/`
2. **About a book?** → `content/Books/`
3. **Course notes?** → `content/Courses/`
4. **Technical concept, algorithm, or architecture?** → `content/Knowledge/Tech-Science/`
5. **Software tool or dev environment?** → `content/Knowledge/Tools/`
6. **Person profile?** → `content/Knowledge/Startups-BigTechs/People/`
7. **Company profile?** → `content/Knowledge/Startups-BigTechs/Companies/`
8. **VC, accelerator, or ecosystem entity?** → `content/Knowledge/Startups-BigTechs/Ecosystem/`
9. **Academic paper?** → `content/Research Papers/`
10. **Conference or meetup notes?** → `content/Talks/`
11. **Personal project?** → `content/Pet Projects/`
12. **Personal reflection, essay, or journal entry?** → `content/Writings/`
13. **Finance, investing, or markets?** → `content/Miscellaneous/Finance/`
14. **Country-specific info?** → `content/Miscellaneous/Countries/`
15. **Philosophical or inspirational?** → Append to `content/Miscellaneous/Philosophy.md`
16. **A definition or glossary term?** → Add entry to `content/Knowledge/Glossary.md`
17. **None of the above?** → `content/Miscellaneous/`

## Special pages (do not create duplicates)

- `content/index.md` — Site homepage
- `content/Featured links.md` — Curated links hub
- `content/Knowledge/Glossary.md` — Master glossary (add entries, don't create a new file)
- `content/Books/My Book Collection.md` — HTML gallery (special card format)
- `content/Pet Projects/My Project Collection.md` — HTML gallery (special card format)
- `content/Miscellaneous/Philosophy.md` — Append quotes/insights, don't create separate files
