---
tags:
  - DataScience
---
> The ideas is that **encoders are very powerful at extracting vectors (features) that carry meaningful information of the sequence**

- [What is an encoder model?](#What%20is%20an%20encoder%20model?)
- [What  does the encoder model do?](#What%20%20does%20the%20encoder%20model%20do?)
- [What is "self-attention" and "bi-directional" attention component of an encoder model?](#What%20is%20%22self-attention%22%20and%20%22bi-directional%22%20attention%20component%20of%20an%20encoder%20model?)
- [How does encoder model pre-training work?](#How%20does%20encoder%20model%20pre-training%20work?)
- [What does the encoder model output?](#What%20does%20the%20encoder%20model%20output?)
- [Why should we use an encoder? What are they best suited for?](#Why%20should%20we%20use%20an%20encoder?%20What%20are%20they%20best%20suited%20for?)
	- [Example - MLM - Predicting the missing word](#Example%20-%20MLM%20-%20Predicting%20the%20missing%20word)
	- [Example - Sentiment analysis](#Example%20-%20Sentiment%20analysis)
	- [Example - NER](#Example%20-%20NER)
	- [Example - Extractive Question Answering](#Example%20-%20Extractive%20Question%20Answering)
- [Real-world examples](#Real-world%20examples)

> Encoder models use only the encoder of a [[Transformer Model|Transformer model]].

# What is an encoder model?
It's a neural network model designed to <span style="color:green"><b>process/understand input text (sequences) by converting each word into a feature-rich vector representation that <i>captures both the meaning of the word and its context within the sentence</i></b></span>. These models are commonly used in [[NLP|NLP]] (NLP) tasks because they excel at understanding and representing textual data in a way that can be used for 
- sentence classification, 
- named entity recognition, and 
- question answering. 
**Encoder models typically form the first half of the [[Transformer Model|Transformer]] architecture, designed to "encode" the entire input sequence into contextualised embeddings.**

# What does the encoder model do?
The encoder model processes input sequences of text, creating a set of context-aware representations (feature vectors) for each word. It does this by analyzing the relationships between words through the [[Self-attention|self-attention]] mechanism, effectively capturing the meaning of words based on their surrounding context. These encoded representations can then be used for various downstream tasks, such as classification, prediction, or information retrieval.
![Encoder model - Input and Output Example](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/a63a17957a1bc65116173443a552344611a98679/1-Transformer-Models/images/Encoder-Models-2.png)

# What is "self-attention" and "bi-directional" attention component of an encoder model?
_[[Self-attention|Self-attention]]_ is the mechanism that allows each word (or token) in a sequence to attend to, or focus on, every other word, *including itself*, assigning attention scores based on the relevance between words. This helps capture dependencies and relationships within the sentence, enabling a nuanced understanding of context.  
The _[[Bi-directional attention|bi-directional component]]_ refers to how encoder models, such as BERT, **utilize [[Self-attention|self-attention]] to process words in both directions**—considering both the left (preceding) and right (succeeding) words for each word in the sentence. **This means each word’s context is fully represented, allowing the model to understand the meaning of words that may depend on both past and future information within the sentence.**
![Encoder model - Components](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/a63a17957a1bc65116173443a552344611a98679/1-Transformer-Models/images/Encoder-Models-1.png)

# How does encoder model pre-training work?
The **pretraining** of these models usually revolves around somehow **corrupting a given sentence (for instance, by masking random words in it) and tasking the model with finding** or reconstructing the initial sentence.

During [[Pre-training|pre-training]], encoder models learn language patterns through tasks that require understanding context. 
- One common approach is the _[[MLM|masked language modeling]]_ (MLM) task, used in models like BERT. **In MLM, the model masks (hides) some words in the sentence and tries to predict them based on the surrounding context**. By repeatedly solving this task on a large text corpus, the model learns rich, contextual representations for words. 
- Another approach, as used in [[ELECTRA]], involves training the model to detect whether words in a sentence are real or replaced, adding robustness to the model’s understanding of language.

# What does the encoder model output?
Encoder models output a _feature vector_ (or embedding) for each word in the input sequence. This **feature vector** is a high-dimensional numerical representation that **encodes the word’s meaning along with its context**. 

For example, in the **base [[BERT]] model, *each word's feature vector has 768 dimensions***. The values in these vectors represent the model’s learned understanding of each word's meaning in relation to the other words in the sentence, allowing downstream tasks to utilize this contextualized information for better performance.
![Encoder model - Input and Output Example](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/a63a17957a1bc65116173443a552344611a98679/1-Transformer-Models/images/Encoder-Models-2.png)

![Encoder model - Input and Output Example - P2](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/a63a17957a1bc65116173443a552344611a98679/1-Transformer-Models/images/Encoder-Models-3.png)![Encoder model - Input and Output Example - P3](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/a63a17957a1bc65116173443a552344611a98679/1-Transformer-Models/images/Encoder-Models-4.png)

# Why should we use an encoder? What are they best suited for?
![Why should we use an encoder model?](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/a63a17957a1bc65116173443a552344611a98679/1-Transformer-Models/images/Encoder-Models-5.png)

They excel at tasks that require a deep understanding of sentence structure and context. They are particularly effective in:
## Example - MLM - Predicting the missing word
Encoders ([[MLM]]), with bi-directional context, are good at guessing words in the middle of a sequence. This requires both semantic and syntacting understanding.
![Encoders (MLM) are good at predicting the missing word](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/a63a17957a1bc65116173443a552344611a98679/1-Transformer-Models/images/Encoder-Models-6.png)

## Example - Sentiment analysis
**Sentence Classification** (e.g., sentiment analysis) where the entire sentence’s meaning is needed.
![Encoders are good at Sentiment analysis](https://raw.githubusercontent.com/prasanth-ntu/huggingface-nlp-course/a63a17957a1bc65116173443a552344611a98679/1-Transformer-Models/images/Encoder-Models-7.png)


## Example - NER 
Identifying specific entities within a sentence, such as names of people, locations, and organizations. For more details, refer [[NER]]

## Example - Extractive Question Answering
The model must locate the relevant parts of a text to answer specific questions by identifying spans in the text, often by looking at context across the sentence.

# Real-world examples
1. **Customer Support Chatbots**: Encoder models are widely used in chatbots to accurately interpret user questions and requests. For instance, a chatbot may use an encoder model to classify whether a user inquiry is about billing, technical support, or general questions, and then provide contextually relevant responses.
2. **Legal Document Analysis**: In legal tech, encoder models help identify and extract named entities, such as names of parties, case references, or legal terms, from contracts and other documents. This enables automatic document tagging, faster information retrieval, and helps legal professionals in conducting more efficient document reviews.