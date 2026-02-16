---
tags:
  - data-science
  - learning
  - machine-learning
  - statistics
aliases:
  - Knowledge/Tech-Science/Cartesian Product
---
## What is Cartesian Product?
The Cartesian product of two sets $A$ and $B$, denoted $A \times B$, is the set of all **ordered pairs** $(a, b)$ where $a \in A$ and $b \in B$.

Example:
Let
$A = \{a_1, a_2\}$
$B = \{b_1, b_2, b_3\}$

Then
$A \times B = \{ (a_1, b_1), (a_1, b_2), (a_1, b_3), (a_2, b_1), (a_2, b_2), (a_2, b_3) \}$

It grows combinatorially: if $|A| = m$ and $|B| = n$, then $|A \times B| = m \times n$.

## How is Cartesian Product Used in Categorical Data: Feature Crosses?

**🧠 Feature Crosses (aka combinatorial features) are:**
New features created by combining two or more categorical features into a single categorical feature representing joint levels (interactions).

🚀 Example:
Suppose you have two categorical features:
	•	`Country = {US, UK}`
	•	`Device = {Mobile, Desktop}`

A **feature cross** (i.e., Cartesian product) would generate:
`{(US, Mobile), (US, Desktop), (UK, Mobile), (UK, Desktop)}`

Which becomes a new categorical feature like:
	•	`US_Mobile`
	•	`US_Desktop`
	•	`UK_Mobile`
	•	`UK_Desktop`

> [!TIP] You can then:
> •	One-hot encode these combined categories
> •	Feed them to tree-based models, embedding layers, or wide & deep models

## Why use Feature Crosses?
1.	**Capture interactions** between categories that have joint effects (e.g., “users in US on mobile” behave differently from “users in UK on desktop”).
2.	**Improve model accuracy**, especially for models like logistic regression or neural nets that otherwise assume independence.

## ⚠️ Trade-Offs:

| Pros                                    | Cons                                       |
| --------------------------------------- | ------------------------------------------ |
| Can improve expressiveness              | High cardinality explosion (combinatorial) |
| Captures important patterns             | May lead to overfitting or sparsity        |
| Especially useful in Wide & Deep Models | Need embedding or hashing to manage        |
## In Practice:
•	**Manual Crosses**: You select features to cross based on domain knowledge.
•	**Automated Crosses:** Libraries like `tf.feature_column.crossed_column` (TensorFlow), or via embedding layers in deep learning.
•	**Hashed Crosses**: Avoids exploding dimensions by hashing crossed features into fixed buckets.

# Resources
- Google > Machine Learning > Crash Course > Working with categorical data > [Feature Crosses](https://developers.google.com/machine-learning/crash-course/categorical-data/feature-crosses)