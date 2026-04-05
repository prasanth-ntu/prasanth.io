---
tags:
  - ai
  - ai-agents
  - data-science
  - llm
  - software-engineering
  - tool
description: Claude Code - Amazing agentic coding tool from Anthropic
aliases:
  - Knowledge/Tools/Claude Code
---
## Resources
- https://www.anthropic.com/claude-code#get-started
- https://docs.anthropic.com/en/docs/claude-code/overview
- Pricing: https://platform.claude.com/docs/en/about-claude/pricing
- Models Overview: https://platform.claude.com/docs/en/about-claude/models/overview

# Keyboard Shortcuts
- `Cmd + Esc`: Opens Claude Code Session inside our Code Editor.
	- Alternatively, we can click on the "Claude Code" icon shown in the code editor toolbar 

# Extensions
- VSCode and Cursor IDEs
- Browser

# Monitoring tools

Claude Code MAX doesn't have built-in daily/monthly overall token usage tracking in the native interface. The `/cost` command shows API token usage and is intended for API users. Claude Max [Claude](https://code.claude.com/docs/en/costs) and Pro subscribers have usage included in their subscription, so `/cost` data isn't relevant for billing purposes. Subscribers can use `/stats` to view usage patterns.

For daily and monthly tracking, you'll need third-party tools:
## ccusage
For more details, refer https://ccusage.com/

```bash
# Global installation (optional)
bun install -g ccusage
```

After global installation, run commands directly:

```
ccusage daily
ccusage monthly --breakdown
ccusage blocks --live
```

### Output Column Breakdown

| Column           | What it means                                                   |
| ---------------- | --------------------------------------------------------------- |
| **Input**        | Tokens you sent to Claude (your prompts, code context)          |
| **Output**       | Tokens Claude generated (responses, code)                       |
| **Cache Create** | Context being cached for first time                             |
| **Cache Read**   | Context reused from cache (the savings!)                        |
| **Total Tokens** | Everything combined                                             |
| **Cost (USD)**   | What this would cost at **API rates** (not what you pay on MAX) |

### Why Cache Read Dominates (~90-96% of tokens)

When you look at `ccusage daily` output, cache read tokens overwhelmingly dominate. This is expected and means prompt caching is working efficiently.

**What happens on every API round-trip:**

1. Claude Code sends the **entire conversation context** as input: system prompt, CLAUDE.md, all prior messages, all file contents that were `Read`, all tool results — everything.
2. Anthropic's prompt caching recognises that most of this context (the prefix) is identical to the previous call, so it serves it from cache.
3. Only the **delta** (your latest message + new tool results) counts as fresh **Input** tokens.

**Typical breakdown per turn:**

| Category | Typical Size | Why |
|----------|-------------|-----|
| **Cache Read** | ~500K-2M tokens | Full conversation context re-sent from cache |
| **Cache Write** | ~50-200K tokens | New context prefix portion being cached for the first time |
| **Input** | ~200-1K tokens | Only the genuinely new part (your latest message) |
| **Output** | ~1-5K tokens | What Claude generates in response |

**Long editing sessions amplify this pattern** — each `Read` of a large file (e.g. a knowledge base doc) loads its full contents into context, and on subsequent turns that whole file is re-sent from cache. The more files loaded and the longer the conversation, the higher the cache-read ratio.

**Cost implication:** Cache read tokens are priced at 1/10th of regular input tokens, so this high cache-read ratio actually represents significant cost savings. A session showing 50M total tokens at 95% cache read costs far less than 50M tokens of fresh input would.

### API Pricing Breakdown (Opus 4.6 example)

[Official pricing](https://platform.claude.com/docs/en/about-claude/pricing). Prices are per million tokens (MTok):

| Component | Rate | Multiplier | What it covers |
|-----------|------|------------|----------------|
| **Base Input** | $5/MTok | 1x | Fresh tokens not in any cache — your new message, new tool results |
| **5m Cache Write** | $6.25/MTok | 1.25x base | First time a context prefix is cached (default 5-min TTL) |
| **1h Cache Write** | $10/MTok | 2x base | Same but with extended 1-hour TTL (opt-in, not default) |
| **Cache Read** | $0.50/MTok | 0.1x base | Reusing cached prefix on subsequent turns — the big savings |
| **Output** | $25/MTok | 5x base | Tokens Claude generates (responses, code, tool calls) |

Claude Code uses 5-minute cache writes by default.

**Real example — Feb 13, 2026 (Opus 4.6, full day):**

| Component | Tokens | Rate | Cost | Cost w/o Caching | Savings |
|-----------|--------|------|------|------------------|---------|
| Input | 8,887 (0.02%) | $5/MTok | $0.04 | $0.04 | — |
| Output | 6,311 (0.01%) | $25/MTok | $0.16 | $0.16 | — |
| Cache Write | 1,570,068 (3.5%) | $6.25/MTok | $9.81 | $7.85 (as input) | -$1.96 |
| Cache Read | 43,369,984 (96.5%) | $0.50/MTok | $21.68 | $216.85 (as input) | $195.17 |
| **Total** | **44,955,250** | | **$31.70** | **$224.90** | **$193.20 (86%)** |

**Key takeaway:** Cache read is 96.5% of tokens but only 68% of cost — because it's priced at 0.1x base input. Without caching, those 43M tokens would cost $216.85 instead of $21.68. Cache write actually costs *more* than base input (1.25x), but the trade-off is worth it: you pay a small premium once to cache, then save 90% on every subsequent read.

> [!note] ccusage `--offline` gotcha
> As of v18.0.5, `ccusage --offline` doesn't have Opus 4.6 in its bundled pricing, reporting $0 for those rows. Run without `--offline` to fetch live pricing from LiteLLM.

# Memory Management

Claude Code has persistent memory across sessions. [Official docs](https://code.claude.com/docs/en/memory)

## Memory Hierarchy

| Memory Type | Location | Purpose | Synced via Git? |
|-------------|----------|---------|-----------------|
| **Project memory** | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team-shared project instructions | Yes |
| **Project rules** | `./.claude/rules/*.md` | Modular, topic-specific instructions | Yes |
| **User memory** | `~/.claude/CLAUDE.md` | Personal preferences (all projects) | No |
| **Project local** | `./CLAUDE.local.md` | Personal project-specific (auto-gitignored) | No |
| **Auto memory** | `~/.claude/projects/<project>/memory/` | Claude's automatic notes/learnings | No |

More specific instructions take precedence over broader ones.

## @ Import Syntax

CLAUDE.md files can import other files using `@path/to/import` syntax:

```markdown
See @README for project overview.

**User context:** @.claude/user-context.md

# Additional Instructions
- git workflow @docs/git-instructions.md
```

**Key behaviors:**
- Both relative and absolute paths allowed
- Relative paths resolve from the file containing the import
- Max depth: 5 hops (imports can recursively import)
- First-time approval dialog for external imports
- Not evaluated inside code blocks (prevents false positives)
- Home directory supported: `@~/.claude/my-instructions.md`

## Path-Specific Rules

Scope rules to specific file types using YAML frontmatter:

```markdown
---
paths:
  - "src/api/**/*.ts"
  - "tests/**/*.test.ts"
---

# API Development Rules
- All endpoints must include input validation
- Use standard error response format
```

Rules without `paths` frontmatter load unconditionally.

## Best Practices

| File | What Goes Here |
|------|----------------|
| **CLAUDE.md** | Imperatives ("do X when Y"), workflow rules, conventions |
| **Imported files** | Reference material, user context/preferences |
| **Auto memory** | Ephemeral session notes (Claude manages this) |
| **rules/*.md** | Topic-specific rules, optionally path-scoped |

**Tips:**
- Keep CLAUDE.md lean — it loads into context every session
- Use imports to modularize detailed instructions
- Put cross-machine persistent preferences in repo (imported file)
- Let auto memory handle ad-hoc session learnings

## Useful Commands

| Command | Purpose |
|---------|---------|
| `/memory` | Open memory files in editor |
| `/init` | Bootstrap a CLAUDE.md for your codebase |
| "remember that..." | Ask Claude to save something to auto memory |
# Learning Resources
[[freeCodeCamp.org - Claude Code Essentials]]