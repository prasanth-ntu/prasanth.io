---
tags:
  - DataScience
---
**Self-Attention** is the **specific form of [[Attention layers|attention]]** used in [[Transformer Model|transformers]]. **Each word in the sequence attends to all other words in the sequence, *including itself***. In other words, it **highlights relationships between each word and every other word, enhancing context comprehension.**

**Steps in Self-Attention** (*Not clear yet*): 
1. **Query, Key, and Value Vectors**: Each word (or token) is transformed into three vectors: a query (Q), a key (K), and a value (V).
2. **Dot Product of Query and Key**: The query of each word is compared to the keys of all other words using a dot product, creating attention scores.
3. **Scaled and Softmaxed Scores**: The scores are scaled down (by the square root of the dimension) and then passed through a softmax to create a probability distribution.
4. **Weighted Sum of Values**: These scores are used to compute a weighted sum of the value vectors, which represents the attention output for each word.