---
tags:
  - writing
  - insurance
  - vibe-coding
aliases:
  - Writings/2026-03-14 What My Dad Taught Me About Insurance
---
## Introduction
> [!SUMMARY] வாழும் போதும், வாழ்க்கைக்கு பிறகும் - "In life and beyond life." 
> This is the tagline of Life Insurance Corporation of India, the largest insurance company in the world by number of policies. Growing up, I heard it so often that it became background noise. It took me 15 years to understand what it truly meant.

My philosophy on insurance is simple: <span style="color:green">never be a financial burden on the people you love - whether you're alive (old age, accident, critical illness) or after you're gone.</span>

I've been trying to demystify insurance since my teens. Watching my dad navigate the world of policies, premiums, and claims gave me a front-row seat to an industry that is equal parts essential and opaque. But understanding it - truly understanding it, enough to make informed decisions for my own family - took me 15 years and an AI to finally get there.

---
## The Insurance Agent

My dad was an insurance agent. Let me tell you what that meant in small-town India two decades ago.

> [!WARNING] Insurance agents were - and in many places, still are - mistrusted, misunderstood, and disrespected.

Think of Gandalf - a mystical figure, not easily understood or trusted, yet one of the guiding lights for all of Middle-earth, from the powerful to the humble hobbits. Insurance agents occupy a strangely similar space: misunderstood by most, yet indispensable to those who need them most.

For the prior generation, especially lower and middle-class families struggling to make ends meet, insurance was a far-fetched concept. Monthly premiums felt like money thrown into a void. And the agents who came knocking? They were seen as leeches living off commission - scolded at doorsteps, avoided at markets, their calls blocked and ignored.

My dad entered this profession with no background in finance or insurance. His English was limited. He had no network of wealthy clients. Yet he chose to serve the people around him - farmers, daily wage workers, small shopkeepers - folks whose premiums were modest and whose commissions would barely cover his travel costs.

<span style="color:green">What set him apart was a set of principles that most agents would consider bad business:</span>

- **No lies, no bluffs.** He never exaggerated benefits or hid exclusions. If a policy wasn't right for someone, he said so - even if it meant losing a sale.
- **Never oversold.** He recommended what the customer needed, not what would earn him the highest commission. Many agents push endowment plans and ULIPs because they pay 30-40% first-year commission. My dad would recommend pure term life when that was the right answer - even though it paid almost nothing.
- **Stayed the course.** Most agents disappear after the first year, when commissions drop from 30% to 5%. My dad helped customers throughout the entire policy term and beyond - renewals, claims, nominations, surrenders.
- **Never mishandled money.** In rural India, agents often collect premiums in cash. People trusted my dad with large sums. He never once violated that trust.
- **Kept learning.** Despite his background, he studied every new product, attended every training, and understood the fine print that even branch managers sometimes got wrong.

He managed roughly 1,000 families. He knew their birthdays, their children's milestones, their financial anxieties. He wasn't selling insurance - he was providing a safety net.

> _"The best insurance agent is the one whose customers never feel like they were sold something."_

---
## The Contradiction Triangle

Here's what I've come to understand about the insurance industry. There are three parties, and their interests are fundamentally in conflict:

1. **The Insurance Company** - maximize profit (collect premiums, minimize payouts)
2. **The Insurance Agent** - maximize commission (sell high-commission products, regardless of fit)
3. **The Insurance Holder** - maximize protection at minimal cost

<span style="color:green">My dad consistently chose the holder's side. That's why he was never the top-selling agent - but it's also why his customers stayed for life. Some even became multi-generational clients, with children and grandchildren trusting him the same way their parents did.</span>

Financial products are intentionally complex. Jargon-filled brochures, opaque riders, convoluted claim processes - all designed to make normal people feel like they need an expert. And when that expert is incentivized to sell you the wrong thing, the system breaks.

Browse any personal finance forum and you'll find the same pattern: someone asks a simple question about insurance, and gets 70 conflicting replies - half from agents defending their products, half from strangers trying to reverse-engineer what they were never meant to understand.

> [!IMPORTANT] _"The complexity of financial products is not a bug - it's a feature. For the company, not for you."_

---
## Stories That Stay With You

These stories shaped how I think about insurance. They are real. They happened to people I knew.

**The breadwinner who didn't come home.** A family in our neighbourhood - two young kids, a homemaker wife, and a father who was the sole earner. He died in a road accident. No warning, no illness, just gone. My dad had sold him a life insurance policy years earlier. In the weeks that followed, while the family was still in shock, my dad handled every piece of paperwork - the death certificate, the claim forms, the bank coordination. The family received roughly ₹10 lakhs (about $12,000 at the time - this was 15 years ago). It wasn't a fortune, but it kept the family afloat while they rebuilt their lives. <span style="color:green">Without that policy, they would have had nothing.</span>

**The man who was turned away.** A well-known working professional in our area wanted term insurance - a product that was virtually unheard of in our region two decades ago. During the mandatory medical examination, an unknown condition was discovered. The application was rejected. He passed away two years later. The family had no cover.

**The agent who didn't insure himself.** My own dad - the man who spent his career convincing others to protect their families - ironically had no term insurance for himself. He trusted his health, his discipline, his savings. He passed away in his late 50s. But here's the thing: he had his finances so perfectly organized that my family could take over with no hiccups. Every policy, every bank account, every investment, every transaction - documented, accessible, and current. <span style="color:green">He practiced what he preached about financial organization, even if he didn't buy the product he sold.</span>

> _"These stories are why I care about getting insurance right. Not as an abstract financial exercise, but as a responsibility to the people who depend on me."_

---
## Vibe-Coding My Way to Clarity

For 15 years, I tried to understand insurance through conversations with agents, talking to friends, reading policy documents, and browsing comparison websites. I'd come away more confused each time. Every advisor had a different recommendation. Every product had a different structure. Every comparison was apples to oranges.

Then I started using [Claude](https://claude.ai) and what some people call "vibe-coding" - building software through natural conversation with AI. And something clicked.

Instead of trying to hold everything in my head, I built a system. Three components, each serving a distinct purpose:

### 1. Markdown as the Source of Truth

Every policy for every family member, tracked in a single structured Markdown file. Premiums, CPF splits, coverage periods, status annotations (active, proposed, declined, deferred) - all in one place.

The beauty of Markdown is that it's both human-readable and machine-parseable. I can review my insurance portfolio in any text editor, and Claude can extract structured data from it programmatically.

### 2. Interactive D3.js Dashboard

The markdown is for thinking. The dashboard is for seeing.

I built an interactive dashboard with 9 visualizations - from summary cards showing total premiums and CPF usage, to a 35-year premium projection showing how costs evolve as each family member ages, to a coverage matrix that reveals gaps at a glance.

<a href="https://insurance.prasanth.io/Family%20Insurance%20Dashboard.html" target="_blank">
<img src="posts/attachments/images/insurance-dashboard-overview.png" alt="Insurance Dashboard Overview - click to try the interactive demo">
</a>
<p style="text-align:center; font-style:italic; color:#888; font-size:0.9em;">Click the image above to try the live interactive demo (with anonymized sample data)</p>

The dashboard includes:
- **Summary cards** - active premiums, proposed costs, CPF vs. cash split
- **Person cards** - per-member breakdown at a glance
- **Premium treemap** - proportional view of where money goes, zoomable by person
- **Payment sources chart** - CPF MA vs. CPF OA vs. cash per member
- **Policy status donut** - active, proposed, declined, deferred
- **Coverage detail matrix** - expandable benefit comparison across family members
- **35-year premium projection** - how costs evolve with age milestones
- **Life-stage coverage Gantt** - which policies cover which life stages
- **Coverage matrix heatmap** - gaps and overlaps in one glance

<img src="posts/attachments/images/insurance-coverage-matrix.png" alt="Coverage Matrix showing policy types across family members">

### 3. The Sync Skill

One command - `/sync-insurance` - reads the markdown, extracts all policy data, validates it (premium totals, CPF splits, policy counts), and replaces the dashboard's data array. No manual transcription. No copy-paste errors. The markdown is always the source of truth.

> [!IMPORTANT] _"The markdown is for thinking, the dashboard is for seeing, and the sync skill is the bridge."_

This system gave me something I never had before: <span style="color:green">a complete, visual, always-current picture of my family's insurance portfolio.</span> I can see gaps instantly. I can project costs decades ahead. I can make decisions based on data, not anxiety.

This isn't just a technical exercise. It's the tool my dad never had - but would have loved.

---
## Open-Source Template

I've open-sourced the entire system as a template you can use for your own family:

**[insurance-dashboard-template](https://github.com/prasanth-ntu/insurance-dashboard-template)** - Markdown template + D3.js dashboard + sync skill

What you get:
- A structured **Markdown file** for tracking all family policies (with sample data to get started)
- A working **interactive dashboard** with all 9 visualizations
- The **sync skill** for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) that keeps everything in sync


<img src="posts/attachments/images/insurance-dashboard-walkthrough.gif" alt="Animated walkthrough of the insurance dashboard">
<p style="text-align:center; font-style:italic; color:#888; font-size:0.9em;">Animated walkthrough showing the dashboard's interactive features</p>

---
## Closing

> [!SUMMARY] வாழும் போதும், வாழ்க்கைக்கு பிறகும் - "In life and beyond life."

I started this post with the LIC tagline. Let me end with what it means to me now.

A life well lived is measured not just by what we achieve, but by how the people we love are taken care of after we are no longer around them. My dad understood this intuitively. He spent his career helping a thousand families prepare for the worst while hoping for the best.

<span style="color:green">He showed me that insurance isn't about products or premiums - it's about protection. It's about love expressed in the language of planning.</span>

I built this system because I wanted clarity for my own family. I'm sharing it because maybe it can help yours too.

> [!HINT] _If you've been meaning to review your family's insurance but keep putting it off - this is your sign. Start with a simple question: "If something happened to me tomorrow, would my family be okay?" The answer to that question is worth more than any dashboard._

---

*Built with [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [D3.js](https://d3js.org/). Open-sourced at [insurance-dashboard-template](https://github.com/prasanth-ntu/insurance-dashboard-template).*
