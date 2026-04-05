# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Build and Development

- **Start development server**: `npm run dev` or `npm run serve`
- **Build the site**: `npm run build`
- **Build docs**: `npm run docs`
- **Sync content**: `npm run sync`
- **Format code**: `npm run format`
- **Type checking**: `npm run check`
- **Run tests**: `npm run test`

### Custom Commands

- **Generate slideshow**: `npm run slideshow` (runs `scripts/sync-slideshow.sh`)
- **Sync HTML**: `npm run html` (runs `scripts/sync-html.sh`)

## Architecture Overview

Quartz is a static site generator for digital gardens, built with a plugin-based architecture. It transforms Markdown content into an interactive website.

### Core Components

1. **CLI Interface**: Entry point through `bootstrap-cli.mjs` which handles command parsing and builds the site
2. **Build Process**:
   - Content parsing using unified/remark/rehype ecosystem
   - Plugin system for transformations and emitters
   - Concurrency handling for large content sets

3. **Plugin System**:
   - **Transformers**: Modify content (Markdown → Markdown or HTML → HTML)
   - **Filters**: Control which content is published
   - **Emitters**: Generate output files

4. **Component System**:
   - React/Preact-like components for layouts
   - CSS handled through SCSS with Lightning CSS for optimization

### Project Structure

- `/quartz`: Core framework code
  - `/components`: UI components
  - `/plugins`: Plugin implementations
  - `/processors`: Content processors
  - `/styles`: Global styles
  - `/util`: Utilities

- `/content`: Where user content lives (Markdown files)
  - `notes/`: All knowledge — tech, tools, books, courses, papers, talks, finance, health (~285 files, flat). Content type is distinguished by tags, not folders.
  - `posts/`: Original writings (date-prefixed filenames, flat)
  - `projects/`: Things built (~8 files, flat)
  - Root files: `index.md` (content hub), `about.md` (CV)
- `/scripts`: Custom build/utility scripts (not part of upstream Quartz)
  - `sync-slideshow.sh`: Prebuild script for Paige AI slideshow (source: `content/notes/paige-ai-report/`)
  - `sync-html.sh`: Prebuild script for architecture HTML pages (source: `content/notes/*.html`)
  - `standardize_tags.py`: Tag standardization script (lowercase kebab-case)
  - `restructure_folders.py`: Folder migration script (used during reorganization)
  - `convert_all_canvas.py`, `convert_canvas_to_mermaid.py`: Canvas → Mermaid converters
- `/docs`: Documentation for Quartz itself

### Key Files

- `quartz.config.ts`: Main configuration for site settings, plugins, etc.
- `quartz.layout.ts`: Layout configuration for different page types
- `package.json`: Project dependencies and scripts
- `quartz/plugins/transformers/links.ts`: Link transformer (custom fix: skips slugification for `/static/` paths)

### Build Pipeline

1. Content is loaded from the content directory
2. Markdown is parsed and processed through transformers
3. Content is filtered based on filter plugins
4. HTML/assets are generated using emitter plugins
5. Static files are bundled and optimized

## Custom Graph Component

The graph view (`quartz/components/Graph.tsx` + `quartz/components/scripts/graph.inline.ts` + `quartz/components/styles/graph.scss`) has been customized beyond upstream Quartz:

### Features
- **Global/Focused toggle**: Full-screen graph modal has a segmented toggle (Global = all nodes, Focused = 2-hop neighbourhood from current page). Mode persists in `sessionStorage`.
- **Tag-based coloring**: Nodes are colored by their primary (first) frontmatter tag using golden angle hue distribution (137.508°) with FNV-1a hashing for maximum visual separation. Tag nodes also get their tag's color.
- **Depth-based opacity**: In focused mode (`depth >= 0`), nodes fade based on BFS distance from the current page. Formula: `1 - (nodeDepth / (originalDepth + 1)) * 0.75`.
- **Visual indicators**: Current page gets a dark ring/border. Visited nodes get a subtle darkgray stroke. Tag nodes get a colored stroke.

### Config (`D3Config` in `Graph.tsx`)
- `tagColors?: Record<string, string>` — Override auto-generated tag colors, e.g. `{ "book": "#4a90d9" }`
- `depth: -1` = all nodes (global), `depth: 2` = 2-hop neighbourhood (focused)
- `showTags` / `removeTags` — Control tag node visibility

### Key implementation details
- Rendering uses D3.js force simulation + Pixi.js (WebGPU/WebGL canvas)
- `removeAllChildren(graph)` clears the graph container on re-render; toggle controls are a sibling div to survive this
- `registerEscapeHandler` (util.ts) checks `e.target !== this`, so child clicks don't close the modal
- The `color()` function maps `NodeData.tags[0]` → palette color via `tagToColor()` (golden angle + FNV-1a hash → HSL → hex)

## Development Notes

- Node.js v22+ and npm v10.9.2+ are required
- TypeScript is used for type safety
- Preact is used for component rendering
- SCSS is used for styling
- esbuild handles bundling and transpilation
- The codebase uses a plugin architecture for extensibility

When working on Quartz code, be aware of the separation between server-side code (Node.js environment) and client-side code (browser environment). Components can have both server and client aspects.