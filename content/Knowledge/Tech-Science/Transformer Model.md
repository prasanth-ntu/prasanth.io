---
tags:
  - DataScience
  - ArtificialIntelligence
  - MachineLearning
  - LLM
---

> Most model LLMs rely on the *transformer* architecture, which is a DNN architecture introduced in the [[A Vaswani - Attention Is All You Need - 2017]]"
## Transformers are language models
All the Transformer models (such as GPT, BERT, BART, T5, etc.) have been trained as language models. This means they have been trained on large amounts of raw text in a **[[Self-supervised learning|self-supervised learning]]**. Self-supervised learning is a type of training in which the objective is automatically computed from the inputs of the model. That means that humans are not needed to label the data!

This type of model develops a statistical understanding of the language it has been trained on, but it’s not very useful for specific practical tasks. **Because of this, the general pre-trained model then goes through a process called _[[Transfer learning|transfer learning]]_**. During this process, the model is fine-tuned in a supervised way — that is, using human-annotated labels — on a given task.

## Transformer are big models
General strategy: *As the model's sizes increases and the amount of data increases, the model achieves better performance*
![Model parameters](https://huggingface.co/datasets/huggingface-course/documentation-images/resolve/main/en/chapter1/model_parameters.png)

![Transformer timeline](https://arxiv.org/html/2302.07730v4/extracted/2302.07730v4/02-06.png)

## Categories of transformer models
1. [[Auto-regressive transformer models]] (GPT-like)
2. [[Auto-encoding transformer models]] (BERT-like)
3. [[Sequence-to-sequence transformer models]] (BART/T5 like)

## General architecture of the transformer model
The transformer model is primarily composed of two blocks:
- **Encoder**: The encoder receives an input and builds a representation of it (its features). This means that the model is **optimized to acquire understanding from the input.**
- **Decoder**: The decoder uses the encoder’s representation (features) along with other inputs to generate a target sequence. This means that the model is **optimized for generating outputs**.
![Transformer blocks](https://huggingface.co/datasets/huggingface-course/documentation-images/resolve/main/en/chapter1/transformers_blocks.svg)

Each of these parts can be used independently, depending on the task:

- **[[Encoder Models|Encoder-only models]]**: 
	- Good for tasks that **require understanding of the input**, such as **_sentence classification_** and **_named entity recognition_**.
- **Decoder-only models**: 
	- Good for **generative tasks** such as **_text generation_**.
- **Encoder-decoder models** or **sequence-to-sequence models**: 
	- Good for **generative tasks that require an input**, such as **_translation_** or **_summarization_**.

## Attention layers

![[Attention layers]]

## The original transformer architecture
The Transformer architecture was originally designed for **translation**. During training, the encoder receives inputs (sentences) in a certain language, while the decoder receives the same sentences in the desired target language. **In the encoder, the attention layers can use all the words in a sentence** (since, as we just saw, the translation of a given word can be dependent on what is after as well as before it in the sentence). **The decoder, however, works sequentially and can only pay attention to the words in the sentence that it has already translated (so, only the words before the word currently being generated**). For example, when we have predicted the first three words of the translated target, we give them to the decoder which then uses all the inputs of the encoder to try to predict the fourth word.

To speed things up during training (when the model has access to target sentences), the decoder is fed the whole target, but it is not allowed to use future words (if it had access to the word at position 2 when trying to predict the word at position 2, the problem would not be very hard!). For instance, when trying to predict the fourth word, the attention layer will only have access to the words in positions 1 to 3.

The original Transformer architecture looked like this, with the encoder on the left and the decoder on the right:

![Original transformer architecture](https://huggingface.co/datasets/huggingface-course/documentation-images/resolve/main/en/chapter1/transformers.svg)

Note that **the first attention layer in a decoder block pays attention to all (past) inputs to the decoder,** but **the second attention layer uses the output of the encoder**. It can thus access the whole input sentence to best predict the current word. This is very useful as different languages can have grammatical rules that put the words in different orders, or some context provided later in the sentence may be helpful to determine the best translation of a given word.

The _attention mask_ can also be used in the encoder/decoder to prevent the model from paying attention to some special words — for instance, the special padding word used to make all the inputs the same length when batching together sentences.

## Architectures vs. Checkpoints

These terms all have slightly different meanings:

- **Architecture**: This is the skeleton of the model — the definition of each layer and each operation that happens within the model.
- **Checkpoints**: These are the weights that will be loaded in a given architecture.
- **Model**: This is an umbrella term that isn’t as precise as _“architecture”_ or _“checkpoint”_: it can mean both.

For example, BERT is an architecture while `bert-base-cased`, a set of weights trained by the Google team for the first release of BERT, is a checkpoint. However, one can say “the BERT model” and “the `bert-base-cased` model.”