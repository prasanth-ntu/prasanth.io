---
tags:
  - ArtificialIntelligence
  - LLM
  - DataScience
  - DeepLearningAI
  - MachineLearning
---
> In [[Self-supervised learning]], the core idea is to leverage the structure within the data itself to create tasks that generate **pseudo-labels . These tasks allow the model to learn meaningful representations from the data without requiring manual labelling.
# What are Pseudo-Labels?
Pseudo-labels are <span style="color:green"><i>automatically generated labels derived from the data itself</i></span>. These labels are not manually annotated but are inferred based on the inherent structure or attributes of the data.
# How are Pseudo-Labels Created?

## 1. Masking/Prediction Tasks:
- Example: In [[NLP]], when training a model like [[BERT]], random words in a sentence are masked. The model is trained to predict these masked words using the context ([[MLM|masked language modeling]]).
	- Input: “The cat is ___ the table.”
	- Pseudo-label: “on.”
## 2.  Contrastive Tasks: 
 -  Example: In computer vision, contrastive learning involves generating two augmented views of the same image and training the model to recognize that they come from the same source.
	 -  Input: Original image and its augmented version.
	 -  Pseudo-labels: “Same” for these pairs, “Different” for unrelated images.
## 3.  Spatial Prediction: 
 -  Example: For images, patches from different regions can be swapped, and the task is to predict their correct positions.
	 -  Input: Image patches in shuffled order.
	 -  Pseudo-labels: Their actual positions.
## 4.  Temporal Prediction: 
 -  Example: In video data, frames are shuffled, and the model is trained to predict their correct sequence.
	 - Input: Frames `[3, 1, 2]`.
	 - Pseudo-labels: `[1, 2, 3]` (actual order).
## 5.  Clustering-based Labeling: 
 -  Example: For datasets like ImageNet, clustering algorithms (e.g., K-means) group similar samples. The model is then trained on these cluster assignments as pseudo-labels.
	 - Input: Images.
	 - Pseudo-labels: Cluster IDs.
# Why Use Pseudo-Labels?

-  **No Manual Annotation Required:** Removes the need for expensive and time-consuming manual labelling.
- **Rich Representations:** By solving these self-defined tasks, the model learns general and transferable features that are useful for downstream supervised tasks.
- **Scalability:** Enables training on massive datasets without the bottleneck of acquiring labels.
#  Examples in Practice: 
1. **NLP:**
	 -  **[[BERT]]:** Predicts masked tokens in a sentence and determines if two sentences are contiguous.
	 -  **[[GPT]]:** Predicts the next word in a sequence (causal language modeling).
2.  **Vision:**
	 -  **SimCLR:** Maximizes similarity between different augmented views of the same image and minimizes similarity with others.
	 -  **[[MAE]] (Masked Autoencoders):** Predicts the missing regions in an image.
3. **Speech:**
	 -  **Wav2Vec:** Predicts quantized representations of masked audio segments.
# How Does It Help?
These tasks train models to understand the underlying patterns and structures in data, enabling the learned representations to be applied to a variety of **downstream tasks**, such as classification, regression, or clustering, often requiring fewer labeled examples.