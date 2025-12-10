---
tags:
  - softwareengineering
  - VSCode
  - Tool
  - OpenSource
  - IDE
title: Cursor - Awesome IDE for Vibe Coding
---
https://www.cursor.com/

# Macbook Shortcuts
## Code Folding
- **Fold innermost uncollapsed region at the cursor:** ⌥ + ⌘ + [
- **Unfold collapsed region at the cursor:** ⌥ + ⌘ + ]

- **Fold all regions in the editor:** ⌘ + R , ⌘ + 0 (zero)
- **Unfold all regions in the editor:** ⌘ + R , ⌘ + J

# Keyboard Shortcuts
- ⌘ + R, ⌘ + S

# Rules
> [!TIP] Rules provide system-level instructions to Agent. They are persistent context, preferences, or workflows for your projects.

**There are 4 types of rules**
1. Project Rules - Scoped to our codebase
2. User Rules - Global to our Cursor env
3. Team Rules - Team-wide rules
4. AGENTS.md - Simple alternative to `.cursor/rules`

**How rules work**
Rules provide persistent, reusable context at the prompt level.

When applied, rule contents are included at the start of the model context. This gives the AI consistent guidance for generating code, interpreting edits, or helping with workflows.

**Best practices**
Good rules are focused, actionable, and scoped.
- Keep rules under 500 lines
- Split large rules into multiple, composable rules
- Provide concrete examples or referenced files
- Avoid vague guidance. Write rules like clear internal docs
- Reuse rules when repeating prompts in chat

**Resources**
- For more details, visit official cursor documentation: https://cursor.com/docs/context/rules 
- Example rules
	- [Cursor AI Prompting Rules](https://gist.github.com/aashari/07cc9c1b6c0debbeb4f4d94a3a81339e) - This gist provides structured prompting rules for optimizing Cursor AI interactions. It includes three key files to streamline AI behavior for different tasks. Medium post from the same author: [Getting Better Results from Cursor AI with Simple Rules](https://medium.com/@aashari/getting-better-results-from-cursor-ai-with-simple-rules-cbc87346ad88)
> [!TODO] Read through the prompting rules in the gist and try it out for first-hand experience.