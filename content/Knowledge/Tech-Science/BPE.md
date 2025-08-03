---
tags:
  - artificialintelligence
  - machinelearning
  - LLM
  - AGI
  - datascience
  - NLP
title: Byte Pair Encoding (BPE)
---
# What's Byte Pair Encoding (BPE), and where is it used?
- The BPE tokenizer is a subword [[Tokenizer|tokenizer]], which means it can split words into smaller parts.
- The BPE tokenizer was used to train LLMs such as different [[GPT]]s, including [[GPT-2]], [[GPT-3]], and the original model used in ChatGPT.
  - <span style="color:#4ea9fb">Has a total vocabulary size of 50,257 tokens, with <code>&lt;|endoftext|&gt;</code> being assigned the largest token ID.</span>
- <span style="color:green"><b>The BPE tokenizer can handle any unknown words.</b></span>
  
# How does BPE work and handle unknown words?
- If the tokenizer encounters an unknown word, it can represent it as a sequence of subword tokens or characters.

## Extract from Wikipedia
> Suppose we are encoding the previous example of "aaabdaaabac", with a specified vocabulary size of 6, then we would first be encoded as "0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 3" with a vocabulary of "a=0, b=1, d=2, c=3". Then it would proceed as before, and obtain "4, 5, 2, 4, 5, 0, 3" with a vocabulary of "a=0, b=1, d=2, c=3, aa=4, ab=5".
> 
> So far this is essentially the same as before. However, if we only had specified a vocabulary size of 5, then the process would stop at vocabulary "a=0, b=1, d=2, c=3, aa=4", so that the example would be encoded as "4, 0, 1, 2, 4, 0, 1, 0, 3".Conversely, if we had specified a vocabulary size of 8, then it would be encoded as "7, 6, 0, 3", with a vocabulary of "a=0, b=1, d=2, c=3, aa=4, ab=5, aaab=6, aaabd=7". This is not maximally efficient, but the modified BPE does not aim to maximally compress a dataset, but aim to encode it efficiently for language model training.

### BPE example: Simplified
<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTxfquw4K2pMoJfb8igxMa-qaz4-aynUH9xi3ZuuByLDsboJd8EyqzvqqxDShuohNZa5yGvkCrflKJw/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false" style="max-width: 1000px; width: 100%; max-height: 400px; height:400px"></iframe>

# Additional resources
- https://platform.openai.com/tokenizer
- https://en.wikipedia.org/wiki/Byte_pair_encoding