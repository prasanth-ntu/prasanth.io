---
tags:
  - DataScience
---
In CLM, **the model learns to predict the next word in a sequence based on the preceding context**, training the model to generate coherent sequences. This method is auto-regressive, meaning the model generates each token based on all tokens to its left in the sequence.

Some variations and strategies within CLM for [[Decoder Models|decoder-only models]] include:

1. **[[Uni-directional attention]]:** Only looks at previous tokens, masking future tokens to prevent leakage.
2. **Prompt-Based Training:** Using prompts or templates to guide the generation, especially for downstream tasks.

These [[Pre-training|pre-training]] approaches align with the objectives of models like GPT, designed for tasks like text completion, dialogue, and story generation.

<img src="https://huggingface.co/datasets/huggingface-course/documentation-images/resolve/main/en/chapter1/causal_modeling.svg">
![Casual Language Modelling - Example](https://huggingface.co/datasets/huggingface-course/documentation-images/resolve/main/en/chapter1/causal_modeling.svg)

While CLM and [[NLG]]  they are related, they are not synonymous; CLM is a specific approach used for certain types of NLG applications. In other words, CLM is a method within NLG.