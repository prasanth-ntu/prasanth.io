---
tags:
  - softwareengineering
  - Programming
  - datascience
  - LLM
  - AI
  - AIAgent
description: Claude Code - Amazing agentic coding tool from Anthropic
---
Resources
- https://www.anthropic.com/claude-code#get-started
- https://docs.anthropic.com/en/docs/claude-code/overview

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
