---
longform: 
tags:
  - ArtificialIntelligence
  - DataScience
  - GAI
  - LLM
  - AGI
author: Leopold Aschenbrenner
---
- We can read it here: [situational-awareness.ai](https://situational-awareness.ai/?ref=forourposterity.com).  
- Or find [the full series as a 165-page PDF here](https://situational-awareness.ai/wp-content/uploads/2024/06/situationalawareness.pdf?ref=forourposterity.com).

# My notes
![[Situational-Awareness.pdf]]

## Key terminologies
| Term               | Explanation                           |                                                             |
| ------------------ | ------------------------------------- | ----------------------------------------------------------- |
| OOM                | Order of Magnitude.<br>               | 3x is 0.5 OOM<br>10x is 1 OOM (i.e., 1 order of magnitude). |
| [[FLOPS\|FLOP]](S) | Floating Point Operation (per Second) |                                                             |
 
## Chapter 1: From GPT-4 to AGI: Counting the OOMs

> The author claims that "achieving AGI by 2027 is plausible". 

GPT-2 to GPT-4 took us from ~preschooler to ~smart high-schooler abilities in  4 years. So, we should expect preschooler-to-high-schooler-sized-qualitative jump by 2027 by tracing the trend lines in **three categories of scale ups**:
1. *compute* (~0.5 OOMs/year)
2. *algorithmic efficiencies* (~0.5 OOMs/year)
3. *unhobbling* (from chatbots to agents)

Here are some of the figures used by the author to support his claim.
 
![[Situational-Awareness---Rough-estimates-of-past-future-scaleup-of-effective-compute.png||700]]
*Figure: Rough estimates of past and future scaleup of effective compute (both physical compute and algorithmic efficiencies).*

![[Situational Awareness - Progress over 4 years.png]]
*Figure: Progress over just 4 years.*

![[Situational Awareness - GPT-4 vs GPT 3.5 scores on standardized tests.png|400]]
*Figure: GPT-4 scores on standardized tests*

![[Situational Awareness - Professional forecast made in 2021 for 2022.png]]
*Figure: Gray: Professional forecasts, made in August 2021, for June 2022 performance on the MATH benchmark (difficult mathematics problems from high-school math competitions). Red star: actual state-of-the-art performance by June 2022, far exceeding even the upper range forecasters gave.*

### *Compute*
GPT-2 to GPT-4 roughly has training compute growth of ~4 OOMs (10,000x) in less than 4 years.
![[Situational Awareness - Estimates of compute for GPT-2 to GPT-4.png]]
*Table: Estimates of compute in [[FLOPS|FLOP]] for [[GPT-2]] to [[GPT-4]] by Epoch AI.*

![[GPT comparison]]

---
![[Situational Awareness - Epoch AI - Data Inishgts.png]]
*Source: [Epoch AI](https://epochai.org/data/epochdb/table)*

> In a nut shell, GPT-2 to GPT-4 jump included 3.5-4 OOMs of compute gains over 4 years period (i.e., ~1 OOMs/year of algorithmic efficiency).
### Algorithmic efficiencies
There have been many tweaks and gains in architecture, data, training stack, etc, collectively called as algorithmic progress, which is probably a similarly important driver of progress along with compute. <span style="color:red">However, unlike compute, algorithmic progress do not get all the attention and are dramatically underrated.</span>

Inference efficiency improved by nearly 3 OOMs (1000x) in less than 2 years.
![[Situational Awareness - Rough estimate on relative inference cost.png|700]]
*Figure: Rough estimate on relative inference cost of attaining ~50% MATH performance.*

| Date                                                                               | Model    | Cost per 1M Input Tokens | Cost per 1M Output Tokens |
| ---------------------------------------------------------------------------------- | -------- | ------------------------ | ------------------------- |
| N.A. [Source](https://the-decoder.com/openai-cuts-prices-for-gpt-3-by-two-thirds/) | GPT-3    | $30.0                    | $60.0                     |
| Dec-2024 ([Source](https://openai.com/api/pricing/))                               | GPT-4o\* | $2.5 (12x reduction)     | $10.0 (6x reduction)      |
\*Cost further drops by half for Batch API.

![[Situational Awareness - Decomposing compute and algorithmic progress.png]]
*Figure: Decomposing progress: compute and algorithmic efficiencies. (Rough illustration)*

> In a nut shell, GPT-2 to GPT-4 jump included 1-2 OOMs of algorithmic efficiency gains over 4 years period (i.e., ~0.5 OOMs/year of algorithmic efficiency).

#### Data wall
