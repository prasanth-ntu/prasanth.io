---
tags:
  - talk
aliases:
  - Talks/AI Engineers 2025 - Reinforcement Learning, Kernels, Reasoning, Quantization & Agents — Daniel Han from Unsloth
---
- Source: [YouTube](https://www.youtube.com/watch?v=OkEGJ5G3foU), [LinkedIn](https://www.linkedin.com/posts/danielhanchen_full-workshop-reinforcement-learning-kernels-activity-7353056071583748096-Srg_?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAcOLFMBUn1o8NEoEvAqJrA0ZzVgH3csPQ0, [Google Slides](), [Unsloth](https://docs.unsloth.ai/ai-engineers-2025), [Google Slides](https://docs.google.com/presentation/d/1Jh5p_JDXt4eLD0ireaHJjJNpzqSF8E1WTwIHeojyjNU/edit?slide=id.g35e7f1de1a9_1_5#slide=id.g35e7f1de1a9_1_5)
- Speaker: Daniel Han, Unsloth ([LinkedIn](https://www.linkedin.com/posts/danielhanchen_full-workshop-reinforcement-learning-kernels-activity-7353056071583748096-Srg_/))
- Additional Resources: [Unsloth - Reinforcement Learning (RL) Guide](https://docs.unsloth.ai/basics/reinforcement-learning-rl-guide)
---
# Presentation

**Llama 1 Models**
A very useful insight form original Llama 1 paper[^1], and is trained with 1.4T tokens (which is lower as 2025 standards)
<div style="text-align: center;">
<img src="llama-model-paper-loss-going-down-with-more-training.png" alt="llama-model-paper-loss-going-down-with-more-training.png" style="max-width: 400px; height: auto; background-color: white; display: block; margin: 0 auto;">
<p style="font-size: 0.9em; color: #666; margin: 4px 0 0 0; font-style: italic;">Figure: Llama pre-training data - Training loss going down with more training data and bigger models.</p>
</div>

In the figure below, we can see that the slope of open-source model is more dramatic than close-source model. In terms of MMLU (5-shot), we can see that open-source models have reached close to closed source (e.g., Llama 3.1 405B vs. GPT-4). 
![[closd-source-vs-open-weight-models.png]]
[Tweet](https://x.com/maximelabonne/status/1816416043511808259) posted on 2025-Jul in Twitter by Maxime. 

Additionally, we can find model performance comparison over time in other platforms as well: 
- https://artificialanalysis.ai/#frontier-language-model-intelligence-over-time
- https://openlm.ai/chatbot-arena/
- https://lmarena.ai/leaderboard

Around Sep 2024, open-source and closed-source models converged in terms of MMLU accuracy, and suddenly, with launch of OpenAI's o1-preview,  the model performance  and capability (reasoning, long reasoning traces) shot up. For 4 months, open-source community stalled. Then, suddenly, in Jan 2025 DeeSeek R1 came, and changed the entire world's perspective that open-source models can indeed perform as good as close-source ones.
![[Frontier Language Model Intelligence Over Time 6 Sep 25 1.png]]

Even before ChatGPT launch in Dec 2022, LLMs existed, but the pre-trained base models were terrible in performance. However, ChatGPT showed that we can make the LLMs very useful with
- good data
- good instructions
- good answers
- good SFT
- good RL

> [!SUMMARY] Open-source always try to catch up to close-source models.

Two huge jumps of open-source models
1. SFT, RLHF jump
2. RL jump
![[two-huge-jumps-in-opensource-llms.png]]

> [!Question] What's the next jump?
> We don't know yet!

> [!TIP] Yann LeCun's Analogy 
> - Pre-training is the "cake", 
> - SFT is the "icing",
> - Reinforcement Learning is the "cherry on top".

## Training  Phases
In the past
- **Pretraining**
- **SFT** (e.g., Instruction fine-tuning)
- **Post Training**

Recently,
- **Pretraining** - Predict the next word
- **"Mid" Training** - High quality data, long context extension, etc.
- SFT
- **Preference Finetuning** (DPO, RLHF)
- **Reinforcement Finetuning** (RLVR)

![[llm-finetuning-everywhere.png]]

**How do we get to our final model?**
0. Random init
1. Pretraining
2. SFT (IFT) - Not much data for SFT
3. PrefFT 
4. RLVR - e.g., gpt o3, o1 models

![[how-do-we-get-to-final-model.png]]

> [!TIP] New Paradigm: Bypass SFT an PrefFT
> Deepseek R1 has demonstrated this.
![[how-do-we-get-our-final-model-bypass.png]]

# Hands-on
- Github code: [prasanth-ntu/qwen3_-4b-grpo.ipynb](https://gist.github.com/prasanth-ntu/08a2028c46905f7f8b83f936f032ece1)
	- *Note: Open in Colab for free GPU access*
# Appendix
[^1]: https://arxiv.org/pdf/2302.13971
