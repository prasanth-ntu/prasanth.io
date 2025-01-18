---
tags:
  - MachineLearning
  - LLM
  - DataScience
  - GAI
  - ArtificialIntelligence
  - NLP
---
# Definition
...

# Different type of embeddings

| Type of Embedding                     | Definition                                                      | Purpose                                                                                   | Example                                           |
| :------------------------------------ | :-------------------------------------------------------------- | :---------------------------------------------------------------------------------------- | :------------------------------------------------ |
| Word Embeddings                       | Represent individual words as dense vector.                     | Capture semantic & synatic relationship between words.                                    | [[Word2Vec]], GloVe, FastText, ELMo, BERT         |
| Subword/Character Embeddings          | Represent subword units or characters                           | Handle rar or out-of-vocabulary words by breaking them into small units.                  | Pyte Pair Encoding (BPE), SentencePiece, FastText |
| Sentence Embeddings                   | Represent entire sentence as a single vector                    | Capture the overall meaning or intent of a sentence                                       | InferSent, Universal Sentence Encoder, SBERT      |
| Paragrah Embeddings                   | Represent a paragraph as a single vector, aggregating sentences | Summarize a collection of sentences in a coherent representation.                         | Doc2Vec(Paragraph Vector)                         |
| Document Embeddings                   | Represent an entire document or text as a single vector         | Enable document-level tasks like clustering, classification, and retrieval.               | Doc2Vec, Longformer, BigBird                      |
| Contextualized Token Embeddings       | Represent tokens in a sequence, influenced by their context     | Essential for tasks where token meaning depend on the surrounding context (e.g, NER)      | Outputs from BERT, GPT, RoBERTa                   |
| Multi-modal Embeddings                | Combine text with other modalities like images or audio.        | Enable tasks like image captioning, video description, or cross-modal retrieval           | CLIP, ALIGN                                       |
| Knowledge Graph Embeddings            | Represent entities and relationships in a knowledge graph.      | Enable reasoning over structured data like knowledge graphs.                              | TransE, TransR, Node2Vec, DeepWalk                |
| Cross-lingual/Multilingual Embeddings | Align semantic meaning across multiple languages.               | Useful for translation and multilingual NLP.                                              | mBERT, XLM-R                                      |
| Task-Specific Embeddings              | Embeddings tailored for specific NLP tasks or domains.          | Fine-tuned to optimize for specific tasks (e.g., sentiment analysis, question answering). | Fine-tuned BERT, GPT, BioBERT, SciBERT            |
# Word embeddings vs. Contextualised token embeddings

> [!summary]
> - **Word Embeddings** are simpler and static, making them fast and lightweight but limited in handling word ambiguity.
> - **Contextualized Token Embeddings** are dynamic and context-aware, making them powerful for nuanced tasks but computationally intensive.

The key difference between **word embeddings** (like Word2Vec or GloVe) and **contextualized token embeddings** (like those produced by BERT) lies in how they handle **context** and the resulting representation of words or tokens.
## 1. Context Awareness
| Aspect                  | Word Embedding                                                    | Contextualized Token Embedding                                      |
| ----------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Context Sensitivity** | **Static**: Same embedding for a word regardless of context.      | **Dynamic**: Embeddings depend on the surrounding context.          |
| **Example**             | "bank" has the same embedding in "river bank" and "bank account". | "bank" in "river bank" has different embedding than "bank account". |

## 2. Representation Type

| Aspect             | Word Embedding                                           | Contextualized Token Embedding                                        |
| ------------------ | -------------------------------------------------------- | --------------------------------------------------------------------- |
| **Representation** | A single fixed vector for each word in the vocabulary.   | A unique vector for each occurrence of a token, with varying context. |
| **Granularity**    | Focused on capturing global relationships between words. | Captures both global and local (context-dependant) relationships.     |
## 3. Model and Architecture

| Aspect           | Word Embedding                                    | Contextual Token Embedding                                                                                       |
| ---------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Underlying Model** | Simple architecture like shallow neural network.  | Deep architectures like [[Transformer Model\|transformers]] (e.g, [[BERT]], [[GPT]]).                            |
| **Training Method**  | Trained to predict nearby words or co-occurrence. | Pre-trained on massive corpora with tasks like masked language modelling ([[MLM]]), or predicting the next word. |
## 4. Flexibility and Use Cases

| Aspect          | Word Embedding                                                             | Contextual Token Embedding                                                                          |
| --------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Vocabulary Size** | Requires a predefined vocabulary, struggles with [[OOV]] words.            | Handles [[OOV]] words with subword tokenization (e.g., WordPiece, [[BPE]])                          |
| **Suitability**     | Good for simpler tasks where context isn't crucial (e.g., word similarity) | Essential for tasks requiring deep understanding of the context (e.g., [[NER]], question answering) |
## 5. Computational Complexity
| Aspect              | Word Embedding                                   | Contextual Token Embedding                                                                |
| ------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| **Efficiency**      | Lightweight and computationally efficient        | Computationally expensive due to the deep [[Transformer Model\|transformer]] architecture |
| **Inference Speed** | Faster as embeddings are precomputed and static. | Slower as embeddings are generated dynamically for each input                             |
