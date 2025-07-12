---
tags:
  - DataScience
---
> Where the **decoder differs from the [[Encoder Models|encoder]] is principally with its [[Self-attention|self-attention]] mechanism**. It's using **"[[Masked Self-Attention|masked self-attention]]"**.
# What is a decoder model?
A decoder model is a component of the Transformer architecture that is ***specifically designed for generating text sequences***. **It takes a sequence of input words and generates an output sequence, predicting the next word based on the words that came before it**. Unlike encoder models, which process input sequences in a way that allows access to all words simultaneously, <span style="color:green">decoder models use previous words to predict the next word in a sequence, making them ideal for tasks involving text generation.</span>

# What does the decoder model do?  
The primary function of a decoder model is to **generate text by predicting the next word in a sequence based on the context provided by preceding words**. It does this through a process called **_auto-regression_**, where the **model uses its previous outputs as part of the input for generating subsequent words**. This allows the model to create coherent and contextually relevant text, making it suitable for applications like story generation, conversation, and more

# What are "masked self-attention," "cross attention," "uni-directional," and "auto-regressive" components of the decoder?
    
- **[[Masked Self-Attention]]:** This mechanism allows the model to focus on previous words while generating the next word. In masked self-attention, **the model is restricted from accessing future words in the sequence by applying a mask**, ensuring that the predictions depend only on past and current words.
- **Cross Attention:** In some architectures, decoders can utilize cross attention to incorporate information from encoder outputs, allowing the model to consider both the generated sequence and the context provided by an encoder. 
	- Cross attention is a mechanism that applies specifically to [[Encoder-Decoder Models| encoder-decoder models]], such as those used in translation tasks, where the [[Decoder Models|decoder]] needs to reference the [[Encoder Models|encoder]]'s outputs for context.
- **Uni-directional:** Decoder models operate in a uni-directional manner, meaning they only consider the context from the left (previous words) when making predictions. They do not access future words, in contrast to the bidirectional attention used in encoder models.
- **Auto-Regressive:** This aspect refers to the way decoder models generate text sequentially, **using previous outputs as inputs for generating the next word**. Each prediction is based on the previously generated words, allowing for coherent text production.
![Decoder model components](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/5d041f7a2baddc9e3adfa1a03e1deaa42fa3ebad/1-Transformer-Models/images/Decoder-Models-1.png)

# How does decoder model pre-training work?
Decoder-only models primarily use _causal language modeling ([[CLM]])_, also known as _next-token prediction_, for pretraining

Pre-training of decoder models typically involves t**raining on large text corpora to predict the next word in a sequence**. For example, in models like GPT-2, the model is exposed to vast amounts of text and learns to identify patterns and relationships between words. **During training, the model is presented with a sequence of words and tasked with predicting the next word**. This process <span style="color:green"><b>enables the model to develop an understanding of language structure, grammar, and contextual relevance.</b></span>
    
# What does the decoder model output?  
The decoder model outputs a numerical representation (feature vector) for each word in the input sequence. Decoder outputs 1-sequence of numbers per input word (a.k.a. feature vectors, or feature tensor). The dimension of the feature vector is defined by the architecture of the model.

## Difference from the encoder
For e.g., for the word "to" in "Welcome to NYC", the feature vector is unmodified by the word "NYC" as all the words on the right (a.k.a. right context words) are masked. Rather than benefitting from all the words on the left and right (i.e., [[Bi-directional attention|bidirectional]] context), decoders only have access to the words on [[Uni-directional attention|single]] context, either left context words or right context words). The **[[Masked Self-Attention|masked self-attention mechanism]]** differs from the [[Self-attention|self-attention]] mechanism by **using an additional mask to hide the context on either side of the words**. The words numerical representation will not be affected by words in the hidden context.
![Words can only see the words on their left side](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/5d041f7a2baddc9e3adfa1a03e1deaa42fa3ebad/1-Transformer-Models/images/Decoder-Models-3b.png)


## An example in the context of GPT-2 along with the feature vector/context size in detail
For GPT-2, the output is a sequence of numbers that represent predicted words based on the previous context. Each feature vector in GPT-2 has a dimensionality of 768 for the base model.  

**Example in Context of GPT-2:**
- **Step 1:** Input: "My" → Output: The model predicts "name" as the next (probably following) word based on its learned context. Further explanation
	- Input to decoder model: "My"
	- Output of decoder model: Predicted feature vector (sequence of numbers) that represent a single word > Small transformation to map the predicted vector to the actual word known by model.
- **Step 2:** Input: "My name" → Output: The model predicts "is" as the next word.
- **Step 3:** This process continues until the desired text length is achieved.  
![Guessing the next work in a sentence: Example](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/5d041f7a2baddc9e3adfa1a03e1deaa42fa3ebad/1-Transformer-Models/images/Decoder-Models-4.png)

> GPT-2 has a maximum context size of 1024 tokens, meaning it can consider up to 1024 tokens in the preceding context when making predictions.

# Why should we use a decoder model and what are they best suited for?
![Why should we use a decoder model?](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/5d041f7a2baddc9e3adfa1a03e1deaa42fa3ebad/1-Transformer-Models/images/Decoder-Models-3.png)

Decoder models are ideal for tasks involving text generation because they are designed to produce coherent and contextually relevant sequences. They excel in applications such as:

- **Creative Writing:** Generating stories, poems, or articles based on a given prompt.
- **Chatbots and Conversational Agents:** Producing natural and engaging dialogue in response to user inputs.
- **Completion Tasks:** Auto-completing sentences or paragraphs based on initial text.  
	Overall, decoder models are best suited for any application where generating human-like text is desired.