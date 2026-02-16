---
tags:
  - ai
  - data-science
  - llm
  - machine-learning
  - nlp
aliases:
  - Knowledge/Tech-Science/Tokenizer
---
# Tokenizing Text
> [!SUMMARY] Tokenizing: Split input text into smaller units, such as individual tokens or words or sub-words. An important step in generating [[Embeddings|embeddings]].

- [Tokenization](https://www.datacamp.com/blog/what-is-tokenization) is a fundamental task when working on NLP tasks. It involves breaking down text into smaller units, known as tokens, which can be words, subwords, or characters.
- Efficient tokenization is crucial for the performance of language models, making it an essential step in various NLP tasks such as text generation, translation, and summarization.
# Steps involved in Tokenizing Text
- Input text to Individual tokens or Tokenized Text
- Individual tokens to Token IDs (using Vocabulary or other techniques)
- Token IDs > Sliding window > Token Embeddings
- Token Embeddings + Positional Embeddings = Final Embeddings

# Additional resources
- [Build-a-LLM-from-Scratch/ch02/01_main-chapter-code/ch02_my_notes.ipynb](https://github.com/prasanth-ntu/Build-a-LLM-from-Scratch/blob/main/ch02/01_main-chapter-code/ch02_my_notes.ipynb)

