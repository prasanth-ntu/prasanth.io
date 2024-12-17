---
longform: 
tags:
  - ArtificialIntelligence
  - DataScience
  - LLM
  - AGI
author: Leopold Aschenbrenner
---
Read the book here: [situational-awareness.ai](https://situational-awareness.ai/?ref=forourposterity.com) or find [the full series as a 165-page PDF here](https://situational-awareness.ai/wp-content/uploads/2024/06/situationalawareness.pdf?ref=forourposterity.com).

*I have summarised & highlighted the important concepts covered in the book for speed reading.*
# Chapter 1: From GPT-4 to AGI: Counting the OOMs

> TL;DR <br>
> <span style="color:green">The author outright claims that "<b><i>achieving AGI by 2027 is plausible</i></b>", which took me aback. However, the data points presented in this chapter convinced me of his argument.</span>

GPT-2 to GPT-4 took us from ~preschooler to ~smart high-schooler abilities in  4 years. So, we should expect preschooler-to-high-schooler-sized-qualitative jump by 2027 by tracing the trend lines in **three categories of scale ups**:
1. [[#Compute]] (~0.5 OOMs/year) 
2. [[#Algorithmic efficiencies]] (~0.5 OOMs/year)
3. *Unhobbling* (from chatbots to agents)

Here are some of the figures used by the author to support his claim.
 
![[Situational-Awareness---Rough-estimates-of-past-future-scaleup-of-effective-compute.png||700]]
*Figure: Rough estimates of past and future scaleup of effective compute (both physical compute and algorithmic efficiencies).*

![[Situational Awareness - Progress over 4 years.png]]
*Figure: Progress over just 4 years.*

![[Situational Awareness - GPT-4 vs GPT 3.5 scores on standardized tests.png|400]]
*Figure: GPT-4 scores on standardized tests*.

![[Situational Awareness - Professional forecast made in 2021 for 2022.png]]
*Figure: Gray: Professional forecasts, made in August 2021, for June 2022 performance on the MATH benchmark (difficult mathematics problems from high-school math competitions). Red star: actual state-of-the-art performance by June 2022, far exceeding even the upper range forecasters gave.*

## Compute
GPT-2 to GPT-4 roughly has training compute growth of ~4 OOMs (10,000x) in less than 4 years.
![[Situational Awareness - Estimates of compute for GPT-2 to GPT-4.png]]
*Table: Estimates of compute in [[FLOPS|FLOP]] for [[GPT-2]] to [[GPT-4]] by Epoch AI.*

![[GPT comparison]]

---
![[Situational Awareness - Epoch AI - Data Inishgts.png]]
*Source: [Epoch AI](https://epochai.org/data/epochdb/table)*

> <span style="color:green">In a nut shell, GPT-2 to GPT-4 jump included 3.5-4 OOMs of compute gains over 4 years period (i.e., ~1 OOMs/year of compute efficiency).</span>
## Algorithmic efficiencies
There have been many tweaks and gains in architecture, data, training stack, etc, collectively called as algorithmic progress, which is probably a similarly important driver of progress along with compute. <span style="color:red">However, unlike compute, algorithmic progress do not get all the attention and are dramatically underrated.</span>

Inference efficiency improved by nearly 3 OOMs (1000x) in less than 2 years.
![[Situational Awareness - Rough estimate on relative inference cost.png|700]]
*Figure: Rough estimate on relative inference cost of attaining ~50% MATH performance.*

| Date                                                                               | Model    | Cost per 1M Input Tokens | Cost per 1M Output Tokens |
| ---------------------------------------------------------------------------------- | -------- | ------------------------ | ------------------------- |
| N.A. [Source](https://the-decoder.com/openai-cuts-prices-for-gpt-3-by-two-thirds/) | GPT-3    | $30.0                    | $60.0                     |
| Dec-2024 ([Source](https://openai.com/api/pricing/))                               | GPT-4o\* | $2.5 (12x reduction)     | $10.0 (6x reduction)      |
\*Cost further drops by half for Batch API.

![[Situational Awareness - Decomposing compute and algorithmic progress.png|600]]
*Figure: Decomposing progress: compute and algorithmic efficiencies. (Rough illustration)*

> <span style="color:green">In a nut shell, GPT-2 to GPT-4 jump included 1-2 OOMs of algorithmic efficiency gains over 4 years period (i.e., ~0.5 OOMs/year of algorithmic efficiency).</span>

#### Data wall
<span style="color:red">We're running out of interent data.</span>

<span style="color:red">Frontier models are already trained on much of the internet data</span>. For e.g., Llama 3, was trained over [15T tokens](https://ai.meta.com/blog/meta-llama-3/). Common Crawl, dump of much of internet, [used for LLM training](https://foundation.mozilla.org/en/blog/Mozilla-Report-How-Common-Crawl-Data-Infrastructure-Shaped-the-Battle-Royale-over-Generative-AI/), is >100T tokens raw, and a relatively simple deduplication leads to 30T tokens.
For more specific domains like code, there are fewer tokens. For e.g., [public github repos](https://arxiv.org/pdf/2211.04325) are estimated to be in low trillions of tokens. 

After 16 epochs, repeating the data for pre-training returns extremely diminishing results.

<span style="color:green">That being said, all of the labs are rumoured to make massive bets on new algorithmic improvements/approaches to get around this</span>.

<span style="color:red">What a modern LLM does during training is, essentially, very very quickly skim the textbook, the words just flying by, not spending much brain power on it. Just reading the same textbook over and over again might result in memorization, and not understanding</span>. This is in contrast to how read a (say, math) textbook, where we read a couple of pages slowly; then digest it, ponder over it; discuss with our friends; try few practice problems; fail, try again in a different way, get some feedback, try again until we get it right; and so on, until, it <i>"clicks"</i>.  So, <span style="color:red">there's a "missing middle" between "pre-training" and "in-context learning"</span>. <span style="color:green">When a human learns from a textbook, they’re able to distill their short-term memory/learnings into long-term memory/long-term skills with practice</span>; <span style="color:red">however, we don’t have an equivalent way to distill in-context learning “back to the weights.”</span> <span style="color:green">Synthetic data/self-play/RL/etc. are trying to fix that: let the model learn by itself, then think about it and practice what it learned, distilling that learning back into the weights.</span>. One such example would be AlphaGo, which was initially trained to imitate learning on expert human Go games, and then by playing millions of games against itself.

> <span style="color:green">In a nut shell, though we are hitting the data well, we will have unconver enough (near and long term) tricks to continue with our ~X OOMs/year  progress in this space.</span>
## Unhobbling

Despite excellent raw capabilities, LLMs are much worse than they could be because they are hobbled, and it takes some algorithmic tweak (e.g., Chain-of-thought) to unlock much greater capabilities. 

# Key terminologies
| Term            | Explanation                         |                                                             |
| --------------- | ----------------------------------- | ----------------------------------------------------------- |
| OOM             | Order of Magnitude.<br>             | 3x is 0.5 OOM<br>10x is 1 OOM (i.e., 1 order of magnitude). |
| [[FLOPS\|FLOP]] | Floating Point Operation            |                                                             |
| [[FLOPS]]       | Floating Point Operation per Second |                                                             |
 
## Appendix
[[Situational-Awareness.pdf]]