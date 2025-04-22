---
tags:
  - DataScience
  - LLM
  - GAI
  - ResearchPaper
  - Google
---

|                     |                                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| Original source     |                                                                                                        |
| My annotated source | [GDrive](https://drive.google.com/file/d/1qe2ZNZXsiGH1Cm94poa7qzupJKqDnV3R/view)                       |
| Podcast             | [YouTube](https://www.youtube.com/watch?v=Na3O4Pkbp-U&list=PLqFaTIg4myu_yKJpvF8WE2JfaG5kGuvoE&index=2) |
| Status              | #InProgress                                                                                            |
# A numbered summary of the topics covered in this video (from a youtube comment):
1. *([0:00](https://www.youtube.com/watch?v=Na3O4Pkbp-U)) Introduction:* Overview of the deep dive into Large Language Models (LLMs), their rapid advancement (up to Feb 2025), and the goal of understanding their architecture, evolution, training, evaluation, and optimization. 
2. *([0:48](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=48s)) Transformer Architecture Foundation:* Introduction to the Transformer architecture (originating from a 2017 Google translation project) as the basis for modern LLMs, including its original encoder-decoder structure. 
3. *([1:28](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=88s)) Input Processing for Transformers:* Explanation of how input text is prepared: tokenization (breaking text into words/subwords), embeddings (creating dense vector representations), and the necessity of positional encoding (sinusoidal, learned) to retain sequence information. 
4. *([2:16](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=136s)) Self-Attention Mechanism:* Detailed explanation of self-attention using the "Thirsty Tiger" example. Introduction of Query (Q), Key (K), and Value (V) vectors, how they are used to calculate attention weights, and how a weighted sum of values creates context-rich representations. Mention of parallel processing using matrices. 
5. *([3:58](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=238s)) Multi-Head Attention:* Explaining that multi-head attention involves running the self-attention process multiple times in parallel with different learned Q, K, V matrices, allowing the model to focus on different types of relationships (e.g., grammatical, semantic) simultaneously for deeper understanding. 
6. *([4:35](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=275s)) Layer Normalization & Residual Connections:* Describing the importance of these components for stable and effective training of deep networks. Layer normalization stabilizes activations, while residual connections act as shortcuts to prevent vanishing gradients and help retain learned information. 
7. *([5:20](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=320s)) Feed-Forward Network Layer:* Explanation of the position-wise feed-forward network applied to each token after attention, typically consisting of two linear transformations and a non-linear activation function (like ReLU or GeLU), to further enhance the model's representational power. 
8. *([5:49](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=349s)) Decoder-Only Architecture:* Discussing the trend towards decoder-only models for text generation tasks, explaining how they work using masked self-attention (only attending to previous tokens), and their suitability for tasks like writing and conversation. 
9. *([6:35](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=395s)) Mixture of Experts (MoE):* Introducing MoE as a technique to build larger models more efficiently by having specialized "expert" submodels and a "gating network" that routes input to only a fraction of the experts, saving computational cost. 
10. *([7:20](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=440s)) Evolution of LLMs - Timeline & Key Models:* A chronological overview of significant LLMs: 
	- GPT-1 (2018): Decoder-only, unsupervised pre-training, limitations. 
	- BERT (2018): Encoder-only, focus on understanding language. 
	- GPT-2 (2019): Scaled-up, better coherence, zero-shot learning. 
	- GPT-3 Family (2020+): Massive scale, few-shot learning, instruction tuning (InstructGPT), code (GPT-3.5), multimodality (GPT-4), large context windows. 
	- Lambda (2021): Focused on natural conversation. 
	- Gopher (2021): Emphasis on high-quality data, optimization, highlighted scaling limitations. 
	- GLAM: Used MoE. 
	- Chinchilla (2022): Showed the importance of data size relative to model size (compute-optimal scaling). 
	- PaLM & PaLM 2 (2022/2023): Strong benchmark performance, Pathway system, improved reasoning/coding/math. 
	- Gemini (Recent): Multimodal native, TPU optimized, MoE use, different sizes (Ultra, Pro, Nano, Flash), very large context window (1.5 Pro). 
	- Open Source Models: Gemma/Gemma 2, Llama family (1, 2, 3, 3.1), Mixtral (MoE), 01 (reasoning), DeepSeek-R1 (reasoning), Qwen, Yi, Grok. Importance of licenses. 
11. *([14:11](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=851s)) LLM Training Overview:* Description of the two main training stages: 
	- Pre-training: Unsupervised learning on massive raw text data to learn general language patterns. 
	- Fine-tuning: Training the pre-trained model on smaller, specific, often labeled datasets to specialize it for particular tasks. 
12. *([15:12](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=912s)) Fine-tuning Techniques:* Explanation of common fine-tuning methods: 
	- Supervised Fine-Tuning (SFT): Training on prompt-response pairs. 
	- Reinforcement Learning from Human Feedback (RLHF): Training a reward model based on human preferences and using RL to align the LLM's output. Also mentioned RLAIF and DPO. 
13. *([16:45](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=1005s)) Parameter-Efficient Fine-Tuning (PEFT):* Discussing techniques to fine-tune large models efficiently by only training a small subset of parameters: Adapters, LoRA, QLoRA, Soft Prompting.
14. *([18:22](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=1102s)) Prompt Engineering:* The importance of crafting effective input prompts to guide LLM output, including techniques like zero-shot, few-shot, and Chain-of-Thought prompting. 
15. *([19:18](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=1158s)) Sampling Techniques:* How LLMs generate text token by token and different strategies: Greedy Search, Random Sampling (with Temperature), Top-K Sampling, Top-P (Nucleus) Sampling, Best-of-N Sampling. 
16. *([20:20](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=1220s)) Evaluating LLMs:* The challenges of evaluating LLMs beyond traditional metrics. Need for multifaceted evaluation frameworks including task-specific data, system-level consideration, defining "good" metrics (accuracy, helpfulness, creativity, etc.). Methods include quantitative metrics (BLEU, ROUGE), human evaluation, and LLM-powered evaluators (auto-evaluators), requiring calibration and awareness of limitations. Mention of rubrics and subtask evaluation, especially for multimodal models. 
17. *([23:17](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=1397s)) Inference Acceleration:* Techniques to make LLM response generation faster and more efficient, balancing quality, speed, cost, latency, and throughput. 
	- Output Approximating Methods: 
		- Quantization (reducing numerical precision), 
		- Distillation (training smaller "student" models from larger "teacher" models). 
	- Output Preserving Methods: 
		- FlashAttention (optimizing attention calculation), 
		- Prefix Caching (reusing calculations for repeating input parts), 
		- Speculative Decoding (using a smaller "draft" model to predict tokens verified by the main model), 
		- Batching, 
		- Parallelization. 
18. *([27:10](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=1630s)) Applications of LLMs:* Wide range of current uses including code/math assistance, machine translation, summarization, question answering (RAG), chatbots, content creation, natural language inference, text classification, LLM evaluation, text analysis. Highlighting the growing impact of multimodal applications across various domains. 
19. *([29:00](https://www.youtube.com/watch?v=Na3O4Pkbp-U&t=1740s)) Conclusion and Future:* Recap of the topics covered and posing questions about future applications and challenges in the rapidly evolving field of LLMs.