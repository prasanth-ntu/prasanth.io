---
tags:
  - writing
  - ml
  - interview
  - vibe-coding
aliases:
  - Writings/2026-03-28 How I Built an ML Interview Prep System
---
## Introduction
> [!SUMMARY] Over 6 months of interviewing, I went from scattered notes and forgotten topics to a system that tracked everything — 100+ ML topics, every company pipeline, and every round in one place. Then I open-sourced it.

<!-- TODO(human): Write 3-5 sentences about your personal motivation. What kicked off the interview journey? What was the emotional state — excitement, anxiety, impostor syndrome? The insurance post opened with your dad's story. This one should open with YOUR story. What's the equivalent of "it took me 15 years"? Example angle: "I'd been building ML systems for X years, but when I sat down to interview, I realized I couldn't explain half of what I did every day." -->

---
## The Problem with ML Interview Prep

Every ML engineer preparing for interviews eventually hits the same wall.

You open a browser tab for "ML interview questions." Then another for "system design ML." Then another for LeetCode. Then a YouTube playlist on transformers. Then a blog post on RAG. Then someone's GitHub repo with 200 starred links.

<span style="color:green">Three hours later, you have 47 tabs open and zero structured knowledge.</span>

The resources exist — they're scattered across hundreds of blog posts, courses, and repos. But no single system connects them. You can't see what you know, what you don't know, and what matters most for your next interview.

I tried:
- **Notion databases** — became a graveyard of half-finished pages
- **Markdown notes** — couldn't see the big picture
- **Anki flashcards** — great for memorization, terrible for understanding relationships between concepts
- **Other people's repos** — always missing the topics I needed, or organized in ways that didn't match how I think

> [!IMPORTANT] _"The problem isn't a lack of resources. It's the absence of a system that grows with you."_

---
## Building the System

What started as messy interview notes evolved into something much larger. Over months of real interviews — some that went well, many that taught me hard lessons — I built a system with five components:

### 1. Knowledge Base — The Core Reference

A single, massive Markdown file covering 100+ ML/AI/DS/LLM topics across 14 categories. But unlike typical study guides, every topic has a two-layer structure:

- **Quick reference tables** — one-liners, key formulas, interview phrasing you can actually say out loud
- **Detailed explanations** — derivations, code examples, edge cases, "what interviewers are really asking"

The topics aren't just textbook summaries. They're battle-tested against real interview questions. When an interviewer asked me something I couldn't answer well, I went back and added or expanded that topic.

<span style="color:green">The knowledge base is a living document — it grew with every interview, not before them.</span>

### 2. Interactive Mind Map — See Everything at Once

The knowledge base is for depth. The mind map is for breadth.

I built a D3.js visualization that renders all 100+ topics as an interactive, searchable, zoomable map. You can see at a glance how topics relate — how Transformers connect to Attention, how RAG connects to Vector Databases, how Feature Engineering connects to everything.

<a href="https://interview.prasanth.io" target="_blank">
<img src="posts/attachments/images/ml-interview-prep-kit-mindmap.png" alt="Interactive Mind Map — click to explore">
</a>
<p style="text-align:center; font-style:italic; color:#888; font-size:0.9em;">Click the image above to explore the live interactive mind map</p>

Features:
- **Search** — find any topic instantly
- **Focus mode** — click a topic to see its relationships
- **Dark mode** — because we all study at night
- **Export** — save as PNG for quick reference
- **Related topics** — navigate between connected concepts

The mind map isn't hand-drawn. It's auto-generated from metadata in the knowledge base using a sync script. Edit the markdown, run `make kb-sync`, and the map updates.

> [!IMPORTANT] _"The knowledge base is for reading. The mind map is for seeing. The sync script is the bridge."_

### 3. Interview Tracking System

<!-- TODO(human): Write 2-3 sentences about your experience tracking multiple company pipelines. How many companies were you tracking simultaneously? What broke when you tried to do it in your head or in a simple doc? This adds authenticity — the insurance post had "1,000 families." What's your equivalent? -->

I built a template system with 10 explicit design decisions — from how to name files to how to handle transcripts to how to separate prep from post-interview review. Five reusable templates cover the full lifecycle:

- **Research template** — company intel, team context, tech stack
- **Round template** — prep, live notes, post-interview review
- **Prep tracker** — rolling checklist across all rounds
- **Quick reference** — consolidated study material per company
- **Postmortem** — cross-round analysis after a pipeline completes

<span style="color:green">The system is designed so that 15 minutes after an interview, you can do a brain dump and have everything you need for an AI-assisted debrief later.</span>

### 4. Career Frameworks

Beyond technical prep, interviews require strategic thinking:
- **Offer decision matrix** — structured framework for comparing offers across dimensions (compensation, growth, team, culture)
- **Negotiation strategy** — tactics and scripts for salary negotiation
- **STAR story methodology** — templates for behavioral interviews with a systematic approach to crafting stories
- **Career strategy** — "Domain-First Prep" and "T-Shape Audit" frameworks

### 5. AI Prompt Templates

Every workflow I used during prep — debriefing after interviews, drilling before them, setting up tracking for a new company — I converted into platform-agnostic prompt templates. They work with Claude, Gemini, ChatGPT, or any LLM.

---
## The Mind Map: Seeing What You Know

<!-- TODO(human): Write 2-3 sentences about the "aha moment" when you first saw all your topics visualized as a mind map. What surprised you? Did you notice gaps? Did the connections between topics reveal something you hadn't seen before? This is the emotional beat of the post — the insurance post had the "complete picture" moment. -->

<img src="posts/attachments/images/ml-interview-prep-kit-overview.png" alt="Knowledge base topics organized across 14 categories">

The 14 categories span the full ML interview surface area:

| Category | Example Topics |
|----------|---------------|
| ML Foundations | Gradient Descent, Bias-Variance, Cross-Validation |
| Classical Algorithms | Decision Trees, SVM, KNN, Naive Bayes |
| Ensemble Methods | Random Forest, XGBoost, Gradient Boosting |
| Deep Learning | CNN, RNN, Attention, Batch Norm |
| NLP & LLMs | Transformers, Tokenization, Fine-tuning, RLHF |
| Agentic AI | LangChain, LangGraph, RAG, Tool Calling |
| MLOps | CI/CD, K8s, Monitoring, Feature Stores |

---
## Open-Source

I've open-sourced the entire system:

**[ml-interview-prep-kit](https://github.com/prasanth-ntu/ml-interview-prep-kit)** — Knowledge base + mind map + templates + tooling

What you get:
- **100+ topic knowledge base** with interview-ready phrasing
- **Interactive mind map** at [interview.prasanth.io](https://interview.prasanth.io)
- **5 interview tracking templates** with a worked example
- **Career frameworks** — offer matrix, negotiation, STAR stories
- **AI prompt templates** for prep workflows
- **Build tooling** — mind map sync, link validator, PII scanner

The PII scanner is worth highlighting: when you add your own notes — real company names, real interview details — the scanner catches confidential terms before you accidentally commit them.

```bash
# Get started in 3 commands
gh repo fork prasanth-ntu/ml-interview-prep-kit --clone
open knowledge-base/ml-ds-llm-fundamentals.md
make mindmap
```

---
## Closing

<!-- TODO(human): Write 3-5 closing sentences. The insurance post ended with the LIC tagline callback and "I built this system because I wanted clarity for my own family." What's your equivalent? What do you want readers to take away? Possible angles: "If I could go back and hand my past self one thing..." / "The best time to start building your system is before your first interview. The second best time is now." / Connect back to your opening. -->

---

*Built with [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [D3.js](https://d3js.org/). Open-sourced at [ml-interview-prep-kit](https://github.com/prasanth-ntu/ml-interview-prep-kit). Live mind map at [interview.prasanth.io](https://interview.prasanth.io).*
