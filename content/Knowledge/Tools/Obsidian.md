---
tags:
  - SoftwareEngineering
  - Obsidian
  - Quartz
  - PKM
  - Tool
  - OpenSource
title: Obsidian - The best personal knowledge management (PKM) tool
---
# Markdown formatting
## Basic formatting Syntax
- [Basic formatting syntax](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax)
### Paragraphs
If you want to prevent spaces from collapsing or add multiple blank spaces, you can use the `&nbsp;` (non-breaking space) or `<br>` (line break) HTML tags.
### Footnotes
You can add footnotes[^1] to your notes using the following syntax:

[^1]: This is the referenced text.


```md
This is a simple footnote[^1].

[^1]: This is the referenced text.
[^2]: Add 2 spaces at the start of each new line.
  This lets you write footnotes that span multiple lines.
[^note]: Named footnotes still appear as numbers, but can make it easier to identify and link references.
```

You can also inline footnotes in a sentence. Note that the caret goes outside the brackets.

You can also use inline footnotes. ^[This is an inline footnote.]

```md
You can also use inline footnotes. ^[This is an inline footnote.]
```

Note

Inline footnotes only work in reading view, not in Live Preview.

### Comments
You can add comments by wrapping text with `%` by using it twice. Comments are only visible in Editing view.

Testing out a ...%%comment%%... (inline comment), which is hidden.


```md
This is an %%inline%% (inline) comment where the word inline is enclosed with % twice.

Below is a block comment, which is hidden in view mode.
%%
This is a block comment.

Block comments can span multiple lines.
%%
```

## Obsidian Flavored Markdown

| Syntax          | Description                                                                                                               | Example                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `[[Link]]`      | [Internal links](https://help.obsidian.md/Linking+notes+and+files/Internal+links)                                         |                                                                                                                            |
| `![[Link]]`     | [Embed files](https://help.obsidian.md/Linking+notes+and+files/Embed+files)                                               |                                                                                                                            |
| `![[Link#^id]]` | [Block references](https://help.obsidian.md/Linking+notes+and+files/Internal+links#Link%20to%20a%20block%20in%20a%20note) |                                                                                                                            |
| `^id`           | [Defining a block](https://help.obsidian.md/Linking+notes+and+files/Internal+links#Link%20to%20a%20block%20in%20a%20note) | [[Obsidian#^6c454f]]<br><br>[[Obsidian#Non-obsidian Site Inspirations]]<br><br>[[AI-ML-DS-and-SE Glossary#^casual-effect]] |
| `%%Text%%`      | [Comments](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Comments)                              |                                                                                                                            |
| `~~Text~~`      | [Strikethroughs](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Bold,%20italics,%20highlights)   |                                                                                                                            |
| `==Text==`      | [Highlights](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Bold,%20italics,%20highlights)       |                                                                                                                            |
| ` ``` `         | [Code blocks](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Code%20blocks)                      |                                                                                                                            |
| `- [ ]`         | [Incomplete task](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Task%20lists)                   |                                                                                                                            |
| `- [x]`         | [Completed task](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Task%20lists)                    |                                                                                                                            |
| `> [!note]`     | [Callouts](https://help.obsidian.md/Editing+and+formatting/Callouts)                                                      |                                                                                                                            |
| (see link)      | [Tables](https://help.obsidian.md/Editing+and+formatting/Advanced+formatting+syntax#Tables)                               |                                                                                                                            |
### Plugins
- [ ] https://quartz.jzhao.xyz/plugins/ObsidianFlavoredMarkdown - Need to revisit this, and explore deeper for Block references (https://help.obsidian.md/Linking+notes+and+files/Internal+links#Link%20to%20a%20block%20in%20a%20note)

## Callouts
- [Callouts](https://help.obsidian.md/Editing+and+formatting/Callouts)
### Supported callout types
- `> [!note]`
- `> [!abstract]`
	- Aliases: `summary`, `tldr`
- `> [!info]`
- `> [!todo]`
- `> [!tip]`
	- Aliases: `hint`, `important`
- `> [!success]`
	- Aliases: `check`, `done`
- `> [!question]`
	- Aliases: `help`, `faq`
- `> [!warning]`
	- Aliases: `caution`, `attention`
- `> [!failure]`
	- Aliases: `fail`, `missing`
- `> [!danger]`
	- Aliases: `error`
- `> [!bug]`
- `> [!example]`
- `> [!quote]`
	- Aliases: `cite`
### Nested callouts 
```
> [!question] Can callouts be nested?
> > [!todo] Yes!, they can.
> > > [!example]  You can even use multiple layers of nesting.
```
### Foldable callouts
```
 > [!note]- Foldable
 > This is a foldable callout
```

# Updating the Site
## Key commands
- **Building the quartz**
	- This will start a local web server to run our Quartz on our computer. We can view it at `http://localhost:8080/`
```bash
npx quartz build --serve
```
- **Sync the change to Github & Deploy**
	- Run tis command every time we want to push updates to our repository.
```bash
npx quartz sync
```
- Upgrading Quartz
	- To fetch the latest Quartz updates, simply run
```bash
npx quartz update
```

For more details, refer  [Quartz 4.0](https://quartz.jzhao.xyz/) official documentation

---
# Customising the site
- **Open Graph Meta Tags**
	- Preview and generate using this site: https://www.opengraph.xyz/url/https%3A%2F%2Fprasanth.io
- Line wrap in source mode of when editing table entry
	- Solution provided in [Obsidian forum](https://forum.obsidian.md/t/line-wrap-in-source-mode-or-when-editing-table-entry/60901)
---
# Obsidian References
## Site Inspirations
-  https://notes.yxy.ninja/ - NUS CS student 
- https://yomaru.dev/projects
- https://www.rcook.net/How-I-use-Obsidian,-Quartz,-Git-and-Apache-to-publish-these-notes
- https://wfhbrian.com/obsidian/introducing-smart-chat-transform-your-obsidian-notes-into-interactive-ai-powered-conversations#limitations-and-tips-for-a-better-experience 
- https://oliverfalvai.com/Personal-changelog
	- https://oliverfalvai.com/evergreen/obsidian-tips-and-tricks
-  https://tfthacker.com/article-obsidian-dashboardplusplus2022
- https://hermitage.utsob.me/
- https://collapsedwave.com/Machine-Learning/Autodiff
## Tutorials & Youtube Videos
- [How to publish your notes for free with Quartz](https://www.youtube.com/watch?v=6s6DT1yN4dw&t=227s)  
	- The youtube video that I referred to publish my Obsidian notes using Quartz plugin and Github Pages for 🆓
- ["Obsidian" Canvas on STEROIDS: Excalidraw 1.9.5 release](https://www.youtube.com/@VisualPKM)
## Documentations
- [Quartz 4.0](https://quartz.jzhao.xyz/) 
	- The documentation I referred to publish my Obsidian notes for free with Quarts

# Non-obsidian Site Inspirations
- http://saratchandranagavarapu.rf.gd/index.html