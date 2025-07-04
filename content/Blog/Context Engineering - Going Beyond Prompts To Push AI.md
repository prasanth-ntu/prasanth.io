---
description: Summarised the key points from the newsletter blog post by *Dharmesh Shah* about "Context Engineering" in simple.ai
author: Dharmesh Shah
date: 2025-07-02
---

| Author | Dharmesh Shah                                                                           |
| ------ | --------------------------------------------------------------------------------------- |
| Source | [simple.ai](https://simple.ai/p/the-skill-thats-replacing-prompt-engineering) blog post |

> [!SUMMARY] Prompting tells the model how to think, but context engineering gives the model the training and tools to get the job done.

---
# What's Context Window?

> [!QUOTE] Think of it as a big sheet of paper that you pass to the LLM.

  Context windows have a limit, usually expressed as a number of "tokens." A token is roughly ¾ of an English word or about four characters. "ChatGPT" is two tokens: "Chat" and "GPT." This matters because increase in token count will reflect in
  1. Billing
  2. Latency
  3. Memory

> [!INFO] But as context windows have exploded in token size over the last 2 years from 4K to over 1M tokens, we've gotten increasingly clever about what we put in that context window, such as:
> - How AI "Remembers" our conversation
> - RAG: Teaching AI on demand
> - Tool Calling: Extending AI's Capabilities

With a million-token context window, you can feed an 
- AI an entire codebase, 
  a complete business plan, or 
  months of customer support conversations, 
and it can reason across all of that information simultaneously.

---
# Why Context Engineering Matters?


> [!QUOTE] An (overly) simple explanation: Prompt engineering was like learning to ask really good questions. Context engineering is like being a librarian who decides what books someone has access to before they even start reading.

The shift from Prompt Engineering to Context Engineering may seem simple, but the framing is completely different--instead of optimizing how you ask, you're now optimizing what the AI has access to when it _thinks_.

> [!INFO] What context Engineers Actually Do:
> - **Curate**: Decide which documents, tools, APIs matter for each specific task
> - **Structure**: Layer system messages → tools → retrieved data → user prompt in optimal order
> - **Compress**: Summarize or chunk information to stay under token limits while preserving what matters
> - **Evaluate**: Measure accuracy and watch for "context dilution" where irrelevant info distracts the model

> [!QUOTE] More context means richer documents and longer conversations. But cost and latency rise roughly linearly with window length. This leaves a ton of room for Context Engineers to discover best practices (many of which are still emerging)

---
# The Context-First Future

> [!IMPORTANT] The *most valuable AI skill*
> It's about understanding how to architect intelligent systems that have access to the right information at the right time.
> It’s a fundamental shift from optimizing _sentences_ to optimizing _knowledge_.

---
