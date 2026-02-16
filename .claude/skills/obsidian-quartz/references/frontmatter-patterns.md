# Frontmatter Patterns by Content Type

## Blogs (summaries of external content)

```yaml
---
description: Summarised the key points from the blog post by *Author* about "Topic"
author: Author Name
date: YYYY-MM-DD
---
```

Followed by a metadata table with Author and Source columns.

## Books

```yaml
---
tags:
  - Book
  - TopicTag
  - Reading
author: Author Full Name
---
```

Tags always include `Book` and `Reading`. Followed by a metadata table with Original source, My annotated source, and Status. Status uses inline tags: `#Completed`, `#InProgress`, `#Todo`.

Optionally `title:` if display title should differ from filename.

## Courses

```yaml
---
tags:
  - datascience
  - Course
  - ProviderTag
  - FrameworkTag
draft: true
---
```

Tags always include `Course`. Use `draft: true` for incomplete notes.

## Knowledge/Tech-Science (concept pages)

```yaml
---
tags:
  - relevantTopic1
  - relevantTopic2
---
```

No `title`, `author`, or `date` needed. Domain-specific tags: `machinelearning`, `datascience`, `softwareengineering`, `Programming`, `DevOps`, etc.

## Knowledge/Tools

```yaml
---
tags:
  - softwareengineering
  - Programming
  - relevantTag
description: Tool Name - Brief description
---
```

## Research Papers

```yaml
---
tags:
  - topicTag
  - ResearchPaper
---
```

Tags always include `ResearchPaper`. Filename: `Author Lastname - Title - Year.md`. Followed by a metadata table with source and status.

## Talks/Meetups

```yaml
---
tags:
  - topicTag
  - Talks
  - EventOrganizer
  - Meetup
title: Event Title
---
```

Tags usually include `Talks` or `Meetup`.

## Writings (personal reflections)

No frontmatter is typical. Filenames are date-prefixed: `YYYY-MM-DD Description.md`. Content begins with `## Introduction` and a `> [!SUMMARY]` callout.

## Pet Projects

```yaml
---
tags:
  - softwareengineering
  - Projects
  - TechStack
  - OpenSource
---
```

Tags always include `Projects`.

## Miscellaneous/Finance

```yaml
---
tags:
  - Finance
  - Investment
---
```

## People (Knowledge/Startups-BigTechs/People/)

No frontmatter. Content uses bullet-point format with bold labels.

## Companies (Knowledge/Startups-BigTechs/Companies/)

No frontmatter. Content uses milestone-based chronological format.

## Collection pages (My Book Collection, My Project Collection)

```yaml
---
title: Page Title
description: "Long description for SEO"
socialDescription: "Shorter social sharing text"
tags:
  - CategoryTag
---
```

These use custom HTML with `<div class="books-grid">` or `<div class="projects-grid">` and card elements. Do not modify the HTML structure without understanding the associated CSS.

---

## Common tag vocabulary

**Content type tags:** `Book`, `Reading`, `Course`, `ResearchPaper`, `Projects`, `Talks`, `Meetup`

**Domain tags (camelCase):** `datascience`, `machinelearning`, `artificialintelligence`, `deeplearningai`, `softwareengineering`

**Technology tags:** `LLM`, `GAI`, `NLP`, `AIAgent`, `Chatbot`, `CrewAI`, `Docker`, `Python`, `Programming`, `DevOps`

**Topic tags:** `Finance`, `Investment`, `Money`, `Philosophy`, `Habits`, `Psychology`

**Source tags:** `OpenSource`, `Hacks`, `Google`, `Anthropic`, `YC`

**Status (inline only, NEVER in frontmatter):** `#Completed`, `#InProgress`, `#Todo`, `#Draft`, `#WIP`

These status tags appear inside metadata tables in the content body, not in YAML frontmatter.
