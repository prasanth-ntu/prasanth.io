---
tags:
  - datascience
  - machinelearning
  - Learning
  - Concepts
---
# Multi-class vs Multi-label vs Multi-output Classification
> [!HINT] ✅ **Key Distinction:**
> - _Multi-class_ → 1 categorical output.
> - _Multi-label_ → multiple binary outputs.
> - _Multi-output_ → multiple outputs, each possibly multi-class.

```vbnet
Classification
│
├── Single-output
│   ├── Binary classification
│   └── Multi-class classification
│
└── Multi-output
    ├── Multi-label (all outputs are binary)
    └── General multi-output (outputs can be multi-class)
```

![[Venn diagram - Binary vs Multi class vs Multi label.png]][^3]

---
### **Classification Types (with MNIST examples)**

| **Type**                                        | **Definition**                                                                         | **Output Format**                                 | **MNIST Example**                                                                   | **Other Examples**                                                                             |
| ----------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Binary Classification**                       | Each instance belongs to exactly **one of two classes**.                               | Single binary label (0/1).                        | Predict “Even vs Odd” digit.                                                        | Spam detection (spam / not spam).                                                              |
| **Multi-class Classification**                  | Each instance belongs to exactly **one class** among 3 or more.                        | Single categorical label (e.g., one-hot encoded). | Predict digit ∈ {0–9}.                                                              | Fruit classification (apple, banana, orange).                                                  |
| **Multi-label Classification**                  | Each instance can belong to **multiple binary classes at once**.                       | Vector of binary labels.                          | Predict [Odd?, ≥7?] → e.g., “9” → [True, True].                                     | Face recognition with multiple people per photo.                                               |
| **Multi-output (Binary variant = Multi-label)** | Predicts **multiple targets**, each of which is binary. (This is exactly multi-label.) | Multiple binary outputs.                          | Same as multi-label: [Odd?, ≥7?].                                                   | Medical tests (Positive/Negative for multiple conditions).                                     |
| **Multi-output (General)**                      | Predicts **multiple targets**, each target may be binary _or_ multi-class.             | Multiple categorical outputs.                     | Predict: Digit ∈ {0–9}, Stroke ∈ {Thin/Medium/Thick}, Angle ∈ {Left/Upright/Right}. | Medical diagnosis: Disease type ∈ {flu, cold, pneumonia}, Severity ∈ {mild, moderate, severe}. |

---
## 1. **Multi-class classification**
- Each instance (MNIST image) belongs to exactly one among _k_ classes (digits 0–9 → 10 classes). Output is one label from a finite set.
> [!TIP] Output is a probability distribution across all classes (sums to 1)

## 2. **Multi-label Classification** 
- Each instance can belong to _multiple_ classes at the same time. Output is typically a vector of independent binary indicators.
- MNIST example (“≥7?” and “Odd?”) fits here because each picture maps to **two independent yes/no outputs**.
> [!TIP] Output is a set of indepdenent probabilities for each classes (each between 0 and 1)

## 3. **Multi-output Classification**
This is the subtle one. Multi-output (a.k.a. multi-target) classification generalizes multi-label:
- **Multi-label** assumes each target is binary (yes/no).
- **Multi-output** allows each target to itself be multi-class.
Think of it like predicting _several categorical variables simultaneously_.[^2]

**Examples:**
- **Digit task (MNIST):** Instead of only predicting the digit, suppose you also want to predict its _stroke thickness_ (thin/medium/thick) and _rotation angle category_ (left, upright, right). That’s _three outputs_: digit ∈ {0–9}, thickness ∈ {3 classes}, rotation ∈ {3 classes}. Each output is a multi-class prediction.
- **Medical diagnosis:** Predict both the disease category (e.g., flu, cold, pneumonia) _and_ severity level (mild, moderate, severe).
- **Image denoising:** Each pixel’s value is a multi-class output (0–255). The system produces thousands of such outputs at once. That’s multi-output classification, because every pixel prediction is a categorical label with more than two possible values.
# Appendix
## Python Code
```python
from graphviz import Digraph

# Create a hierarchy diagram for classification types
dot = Digraph(comment="Classification Hierarchy")

# Root node
dot.node("C", "Classification")

# Single-output branch
dot.node("SO", "Single-output")
dot.edge("C", "SO")
dot.node("Bin", "Binary Classification\n(Yes/No)")
dot.node("MC", "Multi-class Classification\n(One out of many classes)")
dot.edges([("SO", "Bin"), ("SO", "MC")])

# Multi-output branch
dot.node("MO", "Multi-output")
dot.edge("C", "MO")
dot.node("ML", "Multi-label\n(Special case: all outputs binary)")
dot.node("GenMO", "General Multi-output\n(Outputs can be multi-class)")
dot.edges([("MO", "ML"), ("MO", "GenMO")])

# Render the diagram
dot.render("/content/classification_hierarchy", format="png", cleanup=True)
# "/mnt/data/classification_hierarchy.png"
```

![[classification_hierarchy.png]]

## Multi-class vs. Multi-label Classification


| Aspect                        | Multi-Class                                                        | Multi-Label                                                          |
| ----------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------- |
| **Output activation**         | Softmax                                                            | Sigmoid                                                              |
| **Loss function**             | CrossEntropyLoss                                                   | BCEWithLogitsLoss                                                    |
| **Constraint**                | Exactly one class per sample                                       | Any number of classes per sample                                     |
| **Prediction interpretation** | "Which animal exists in the image (dog or cat or horse or mouse)?" | "Which of the animals exists in the image (dog, cat, horse, mouse)?" |
| **Output sum**                | Probabilities sum up to 1                                          | Each probability is independent                                      |


![[multiclass vs multilabel classification.png]]
[^1]

# Footnote

[^1]: https://www.geeksforgeeks.org/machine-learning/multiclass-classification-vs-multi-label-classification/

[^2]: https://www.linkedin.com/pulse/multi-class-classification-vs-multi-label-aya-hesham/

[^3]: https://stats.stackexchange.com/questions/11859/what-is-the-difference-between-a-multiclass-and-a-multilabel-problem
