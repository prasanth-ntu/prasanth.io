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
- `/scripts`: Custom build/utility scripts (not part of upstream Quartz)
  - `sync-slideshow.sh`: Prebuild script for Paige AI slideshow
  - `sync-html.sh`: Prebuild script for architecture HTML pages
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

## Development Notes

- Node.js v22+ and npm v10.9.2+ are required
- TypeScript is used for type safety
- Preact is used for component rendering
- SCSS is used for styling
- esbuild handles bundling and transpilation
- The codebase uses a plugin architecture for extensibility

When working on Quartz code, be aware of the separation between server-side code (Node.js environment) and client-side code (browser environment). Components can have both server and client aspects.