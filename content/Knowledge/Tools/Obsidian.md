---
tags:
  - softwareengineering
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

### Rendering images
**Custom image size with caption and background color**

```html
<div style="text-align: center;">

<img src="Llama-pre-training-data-details.png" alt="Llama pre-training data details" style="max-width: 400px; height: auto; background-color: white; display: block; margin: 0 auto;">

<p style="font-size: 0.9em; color: #666; margin: 4px 0 0 0; font-style: italic;">Figure: Llama pre-training data details showing the composition and sources of training data used in the model</p>

</div>
```
<div style="text-align: center;">

<img src="Llama-pre-training-data-details.png" alt="Llama pre-training data details" style="max-width: 400px; height: auto; background-color: white; display: block; margin: 0 auto;">

<p style="font-size: 0.9em; color: #666; margin: 4px 0 0 0; font-style: italic;">Figure: Llama pre-training data details showing the composition and sources of training data used in the model</p>

</div>

## Obsidian Flavored Markdown

| Syntax          | Description                                                                                                               | Example                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `[[Link]]`      | [Internal links](https://help.obsidian.md/Linking+notes+and+files/Internal+links)                                         |                                                                                                                            |
| `![[Link]]`     | [Embed files](https://help.obsidian.md/Linking+notes+and+files/Embed+files)                                               |                                                                                                                            |
| `![[Link#^id]]` | [Block references](https://help.obsidian.md/Linking+notes+and+files/Internal+links#Link%20to%20a%20block%20in%20a%20note) |                                                                                                                            |
| `^id`           | [Defining a block](https://help.obsidian.md/Linking+notes+and+files/Internal+links#Link%20to%20a%20block%20in%20a%20note) | [[Obsidian#^6c454f]]<br><br>[[Obsidian#Non-obsidian Site Inspirations]]<br><br>[[Knowledge/Glossary#^casual-effect]] |
| `%%Text%%`      | [Comments](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Comments)                              |                                                                                                                            |
| `~~Text~~`      | [Strikethroughs](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Bold,%20italics,%20highlights)   |                                                                                                                            |
| `==Text==`      | [Highlights](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Bold,%20italics,%20highlights)       |                                                                                                                            |
| ` ``` `         | [Code blocks](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Code%20blocks)                      |                                                                                                                            |
| `- [ ]`         | [Incomplete task](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Task%20lists)                   |                                                                                                                            |
| `- [x]`         | [Completed task](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Task%20lists)                    |                                                                                                                            |
| `> [!note]`     | [Callouts](https://help.obsidian.md/Editing+and+formatting/Callouts)                                                      |                                                                                                                            |
| (see link)      | [Tables](https://help.obsidian.md/Editing+and+formatting/Advanced+formatting+syntax#Tables)                               |                                                                                                                            |
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
---
# Plugins
- [ ] https://www.youtube.com/watch?v=7Rvl9Sl29Jk - Obsidian Smart Connections - Need to revisit this
- [ ] https://quartz.jzhao.xyz/plugins/ObsidianFlavoredMarkdown - Need to revisit this, and explore deeper for [Block references](https://help.obsidian.md/Linking+notes+and+files/Internal+links#Link%20to%20a%20block%20in%20a%20note)
- [ ] [LongForm](obsidian://show-plugin?id=longform) - Helps to create long projects. Need to revisit this to understand its features properly
- [ ] [canvas2document](obsidian://show-plugin?id=canvas2document) - [Github](https://github.com/slnsys/obsidian-canvas2document)
- [ ] [Templated](obsidian://show-plugin?id=templater-obsidian) - [Github](https://github.com/SilentVoid13/Templater)
- [ ] [Emoji Toolbar](obsidian://show-plugin?id=obsidian-emoji-toolbar) - [Github](https://github.com/oliveryh/obsidian-emoji-toolbar)
---
# Extending Obsidian
## CSS Snippets
- For more details, refer https://help.obsidian.md/Extending+Obsidian/CSS+snippets

### table-wrap.css
```css
/* 
	Cribbed from the excellent ITS Theme
	https://github.com/SlRvb/Obsidian--ITS-Theme 
*/
.cm-s-obsidian .HyperMD-table-row.HyperMD-table-row.HyperMD-table-row {
	white-space: pre-wrap;
	min-width: min-content;
	}
```

### frozen-headers.css
```css
/* Freeze table headers in Obsidian */
table {
    border-collapse: collapse;
    width: 100%;
}

thead {
    position: sticky;
    top: 0;
    background-color: var(--background-primary);
    z-index: 2; /* Ensure it stays above the content */
}

th {
    background-color: var(--background-secondary);
    color: var(--text-normal);
    text-align: left;
    padding: 8px;
}

td {
    padding: 8px;
    border: 1px solid var(--background-modifier-border);
}
```

### mermaid-tweak.css
```css
/*
Source(s): 
    - https://stackoverflow.com/questions/78935770/how-to-set-rendered-mermaid-diagrams-width-to-be-based-on-screen-size-in-obsidia
    - https://forum.obsidian.md/t/resize-and-align-mermaid-diagrams/7019
    - https://www.reddit.com/r/ObsidianMD/comments/1crsgop/til_about_mermaid_diagrams/?rdt=50293
Date updated: 2024-02-14 (YYYY-MM-DD)
*/

/** Set Mermaid Diagrams to 100% width of screen by default */

.mermaid svg {
    display: block;
    width: 100%;
    margin: 0;
    padding: 0;
}

/** On hover, make the diagram full width and enable horizontal scrolling */

div:has(> .mermaid):hover {
    width: auto !important;
}

.mermaid:hover {
    overflow: scroll;
    padding: 0;
    margin: 0;
    text-align: left;
}

.mermaid:hover svg {
    display: block;
    width: auto;
    margin: 0;
    padding: 0;
}
```

### `customer.scss` for Animated GIFs
```css
@use "./base.scss";

// put your custom CSS here!

/* Animated emoji styles */
.animated-emoji {
  display: inline-block;
  vertical-align: middle;
  margin: 0;
  padding: 0;
  
  img {
    display: inline-block;
    vertical-align: middle;
    margin: 0;
    padding: 0;
  }
}
```

Example: Without custom css
- <picture style="display: inline-block; vertical-align: middle;"><source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/2705/512.webp" type="image/webp"><img src="https://fonts.gstatic.com/s/e/notoemoji/latest/2705/512.gif" alt="✅" width="25" height="25" style="display: inline-block; vertical-align: middle;"></picture> 
**Example: With custom css class in quartz styles**
- <picture class="animated-emoji"><source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f613/512.webp" type="image/webp"><img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f613/512.gif" alt="✅" width="25" height="25"></picture>
---

# Env setup
Quartz requires at least [Node](https://nodejs.org/)  and `npm` to function correct. For more details, refer [Get Started](https://quartz.jzhao.xyz/)
# Github repo setup
```bash
# Clone the repo locally
git clone https://github.com/prasanth-ntu/prasanth.io

# list all the repositories that are tracked
git remote -v

# if you don't have upstream as a remote, add it so updates work
git remote add upstream https://github.com/jackyzha0/quartz.git
```

# Updating the Site
## Key commands
- **Building the quartz**
	- This will start a local web server to run our Quartz on our computer. We can view it at `http://localhost:8080/`
```bash
npx quartz build --serve
```

### What actually happens during `npx quartz build --serve`

1. **Prebuild** runs first (`sync-slideshow.sh` + `sync-html.sh`) — copies slideshow and HTML files into `quartz/static/`
2. **esbuild transpiles** the Quartz config, plugins, and components into a single cached JS file (`quartz/.quartz-cache/transpiled-build.mjs`)
3. **`buildQuartz()`** runs — parses all markdown from `content/`, filters out drafts, then **emits** output files to `public/` using these emitter plugins:

| Emitter | What it produces |
|---------|-----------------|
| `AliasRedirects` | Redirect pages for aliases defined in frontmatter |
| `ComponentResources` | JS/CSS bundles for interactive components |
| `ContentPage` | The actual HTML page for each markdown file |
| `FolderPage` | Index pages for folders |
| `TagPage` | Pages for each tag |
| `ContentIndex` | RSS feed + sitemap |
| `Assets` | Processed SCSS → CSS |
| `Static` | Copies `quartz/static/` to `public/static/` |
| `NotFoundPage` | The 404 page |
| `CustomOgImages` | Open Graph preview images (`.webp`) for every page — the thumbnail shown when sharing links on social media, Slack, Discord, etc. This is the slowest emitter as it renders text onto images using satori + sharp for each page |
4. Since `--serve` is passed, it also:
   - Sets `--watch` to `true` — auto-rebuilds when source files change
   - Starts an **HTTP server** on `localhost:8080` serving files from `public/`
   - Starts a **WebSocket server** for live reload (browser refreshes automatically on rebuild)
   - Handles URL routing (e.g. `/foo/` → `/foo/index.html`, `/foo` → `/foo.html`)

> [!tip] With vs without `--serve`
> - **`npx quartz build`**: Builds the site to `public/` and exits. This is what GitHub Actions uses.
> - **`npx quartz build --serve`**: Builds, starts a local server with live reload, and watches for changes. This is for local development.

- **Sync the change to Github & Deploy**
	- Run this command every time we want to push updates to our repository.
```bash
npx quartz sync
```

### What actually happens during `npx quartz sync`

The sync command is **not a build** — it's a git orchestration tool. The actual build happens on GitHub Actions after the push.

#### Local: `npm run sync`

The `sync` script in `package.json` is just `npx quartz sync`. npm automatically runs the `prebuild` script (`bash sync-slideshow.sh && bash sync-html.sh`) before any `build`/`sync`/`serve` script since it follows the `pre<script>` naming convention.

**1. Prebuild** (auto-triggered: `bash sync-slideshow.sh && bash sync-html.sh`)
- Generates Paige AI slideshow HTML files → `quartz/static/paige-slides/`
- Copies architecture HTML files (Spark, Docker, K8s, etc.) → `quartz/static/pages/`

**2. `npx quartz sync`** (defined in `quartz/cli/handlers.js`)
1. Backs up `content/` folder to `.quartz-cache/content-cache`
2. Commits all changes: `git add . && git commit -m "Quartz sync: <timestamp>"`
3. Pulls from `origin v4` (uses `--autostash -X ours` to keep local changes on conflicts)
4. Restores content from cache
5. Pushes to `origin v4`

#### GitHub Actions: Build & Deploy

The push to `v4` triggers `.github/workflows/deploy.yaml`:

1. `npm ci` — clean install dependencies
2. `npm run build` — npm auto-runs `prebuild` first, then `npx quartz build`:
   - Prebuild: copies slideshow + HTML files into `quartz/static/`
   - Parses all `.md` files from `content/`
   - Filters out drafts
   - Emits HTML/assets to `public/`
3. Uploads `public/` as a GitHub Pages artifact
4. Deploys to GitHub Pages → `https://prasanth.io/`

#### End-to-End Flow
```
Local                                GitHub Actions
─────                                ──────────────
npm run sync
  ├─ prebuild (slideshow + html)
  └─ npx quartz sync
       ├─ git commit
       ├─ git pull origin v4
       └─ git push origin v4 ──────→ deploy.yaml triggered
                                       ├─ npm ci
                                       ├─ npm run build
                                       │    ├─ prebuild (auto-triggered)
                                       │    └─ npx quartz build
                                       │         ├─ parse .md files
                                       │         ├─ filter drafts
                                       │         └─ emit → public/
                                       ├─ upload artifact
                                       └─ deploy to GitHub Pages
                                            └─ prasanth.io ✅
```

> [!note] How prebuild works
> The `prebuild` script in `package.json` uses npm's `pre<script>` convention — npm automatically runs it before `build`, `sync`, or `serve`. This means:
> - **Locally**: Prebuild runs before `serve`/`sync` so slideshow and HTML pages render correctly during development
> - **On CI**: Prebuild runs before `build` because the GitHub runner starts from a fresh `git clone` and needs to generate the static files from source
>
> Previously, `build`/`serve`/`sync` scripts also had an explicit `npm run prebuild &&` prefix, causing prebuild to run **twice**. This was fixed by removing the redundant explicit calls.
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
### `ContentMeta.tsx`
```
interface ContentMetaOptions {
  ...
  showAuthor: boolean
}

const defaultOptions: ContentMetaOptions = {
  ...
  showAuthor: true,
}

export default ((opts?: Partial<ContentMetaOptions>) => {
  ...
  
  function ContentMetadata({ cfg, fileData, displayClass }: QuartzComponentProps) {
      ...
      
      // Display author if enabled and available
      if (options.showAuthor && fileData.frontmatter?.author) {
        segments.push(<span>Book by {fileData.frontmatter.author}</span>)
      }
```
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