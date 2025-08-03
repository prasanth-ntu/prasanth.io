---
tags:
  - LLM
  - artificialintelligence
  - machinelearning
  - datascience
  - PromptingTechniques
---
> [!DANGER] Direct prompting on LLMs can return answers quickly and (in terms of output token usage) efficiently, but they can be prone to hallucination. The answer may "look" correct (in terms of language and syntax) but is incorrect in terms of factuality and reasoning.

> [!TIP] Chain-of-Thought prompting is a technique where you instruct the model to output intermediate reasoning steps, and it typically gets better results, especially when combined with few-shot examples. 

> [!WARNING] It is worth noting that this technique doesn't completely eliminate hallucinations, and that it tends to cost more to run, due to the increased token count.

Models like the [[Gemini comparison|Gemini]] family are trained to be "chatty" or "thoughtful" and will provide reasoning steps even without explicitly prompting.

# References
- [Chain-of-Thought (CoT) prompting](https://www.promptingguide.ai/techniques/cot)

