---
tags:
  - artificialintelligence
  - datascience
  - machinelearning
  - LLM
  - PromptingTechniques
  - GAI
---
## Key parameters
### Temperature
> [!INFO] Controls the degree of randomness in token selection.
> - Higher temperatures result in a higher number of candidate tokens from which the next output token is selected, and can produce more diverse results.
> - A temperate of 0 results in **greedy decoding**, selecting the most probably token at each step

### Top-P
> [!INFO] Controls the diversity of model's ouputs.
> - Top-P defines the probability threshold that, once cumulatively exceeded, tokens stop being selected as candidates.
> - A top-P of 0 is typically equivalent to **greedy decoding**.
> - A top-P of 1 typically selects every token in the model's vocabulary.


### Top-k
> [!INFO] 
> - Top-K is a positive integer that defines the number of most probable tokens from which to select the output token. 
>   A top-K of 1 selects a single token, performing **greedy decoding**.

For further reading, check out 
- [# Mastering AI Creativity: A Guide to Temperature, Top-K, Top-P](https://www.thecloudgirl.dev/blog/mastering-ai-creativity-a-guide-to-temperature-top-k-and-top-p)
- [# Understanding OpenAI Parameters: Optimize your Prompts for Better Outputs](https://www.prompthub.us/blog/understanding-openai-parameters-how-to-optimize-your-prompts-for-better-outputs)

![AI creativity controls via parameters](https://images.squarespace-cdn.com/content/v1/65a6226068668c33fe4a4676/126aba55-766e-4dd1-828e-04dadb29a88e/Gen+AI+Blogs+%282%29.png?format=2500w)

## Prompting Techniques

<p>Prompt Engineering helps to effectively design and improve prompts to get better results on different tasks with LLMs.</p>

<div class="techniques-grid">
  <div class="technique-card"> <a href="Zero-shot Prompting.md">Zero-shot Prompting</a></div>
  <div class="technique-card"><a href="Few-shot Prompting..md">Few-shot Prompting</a></div>
  <div class="technique-card"><a href="CoT.md">Chain-of-Thought Prompting</a></div>
  <div class="technique-card">Meta Prompting</div>
  <div class="technique-card">Self-Consistency</div>
  <div class="technique-card">Generate Knowledge Prompting</div>
  <div class="technique-card">Prompt Chaining</div>
  <div class="technique-card">Tree of Thoughts</div>
  <div class="technique-card">Retrieval Augmented Generation</div>
  <div class="technique-card">Automatic Reasoning and Tool-use</div>
  <div class="technique-card">Automatic Prompt Engineer</div>
  <div class="technique-card">Active-Prompt</div>
  <div class="technique-card">Directional Stimulus Prompting</div>
  <div class="technique-card">Program-Aided Language Models</div>
  <div class="technique-card">ReAct</div>
  <div class="technique-card">Reflexion</div>
  <div class="technique-card">Multimodal CoT</div>
  <div class="technique-card">Graph Prompting</div>
</div>

# Resources
- [Prompting Techniques](https://www.promptingguide.ai/techniques)