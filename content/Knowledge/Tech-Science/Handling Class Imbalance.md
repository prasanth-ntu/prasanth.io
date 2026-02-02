---
tags:
  - machinelearning
  - datascience
  - Statistics
---
# Sampling Techniques
## SMOTE
SMOTE stands for Synthetic Minority Over-sampling Technique.

> [!WARNING] You must apply SMOTE **after** the train-test split, and only to the **training data**, to prevent data leakage and ensure a realistic model evaluation, as applying it before introduces synthetic data into the test set, invalidating performance metrics. The goal is to balance the training set to help the model learn minority patterns, while keeping the test set pristine to measure true generalization to unseen, imbalanced data, say [Kaggle users](https://www.kaggle.com/discussions/questions-and-answers/427399) and [Stack Overflow users](https://stackoverflow.com/questions/67750208/different-score-when-using-train-test-split-before-vs-after-smotetomek). 

**Why apply SMOTE after the split (to training data only)?**
- **Prevents Data Leakage**: Applying SMOTE before splitting means synthetic samples from the training set can end up in the test set, giving the model an unfair advantage and inflating performance scores.
- **Realistic Evaluation**: The test set should mirror real-world, imbalanced data to accurately assess how your model will perform in production.
- **Accurate Generalization**: By training on balanced data but testing on imbalanced data, you get a true measure of the model's ability to generalize and perform on unseen examples, not just on "cheated" synthetic data. 

**Correct Workflow**
1. **Split Data**: Divide your entire dataset into training and testing sets first (e.g., 80/20 split).
2. **Apply SMOTE**: Use SMOTE exclusively on the **training set** to generate synthetic minority samples.
3. **Train Model**: Train your machine learning model using the now-balanced training data.
4. **Evaluate**: Test the model on the original, untouched test set.

For more details, refer
- Official API documentation[^1]

## RandomUnderSampler

> [!TODO] TBA


## SMOTETomek

> [!TODO] TBA


### Should we remove Tomek links in AML scenarios?

> [!Question] What's the benefit of cleaning up the majoirty samples that are nearest neighbours to minority samples? Instead, those are hard examples with high likelihood for False Positives which the model should ideally learn right?

**The argument FOR removing Tomek links:**
- These ambiguous boundary samples create "noise" that confuses the classifier
- Removing them creates a cleaner decision boundary
- Theory: cleaner separation → better generalization

**Your counterargument (which is valid):**
- Those are exactly the _hard cases_ the model needs to learn
- Removing them artificially simplifies the problem
- In production, you'll encounter these boundary cases — the model should handle them
- For AML specifically: a transaction that "looks like fraud but isn't" is valuable training signal

**The reality:**

| Scenario                       | Tomek removal helps | Tomek removal hurts |
| ------------------------------ | ------------------- | ------------------- |
| Noisy labels (mislabeled data) | ✓ Cleans errors     |                     |
| Clean labels, hard examples    |                     | ✓ Loses information |
| Simple decision boundary       | ✓                   |                     |
| Complex/overlapping classes    |                     | ✓ Oversimplifies    |

**For AML detection:** Your intuition is correct — AML has genuinely overlapping classes (some fraud _looks_ legitimate by design). Removing Tomek links may:
1. Remove the most informative examples
2. Make the model overconfident on easy cases
3. Increase false negatives in production

**Better alternatives for hard examples:**
- Adjust class weights or threshold instead
- Use focal loss (down-weights easy examples)
- Keep the hard examples, let the model learn the uncertainty

## Sampling Techniques Comparison

|Technique|What it does|Result|
|---|---|---|
|**SMOTE**|Creates _synthetic_ minority samples by interpolating between existing minority points|Increases minority class size to match majority|
|**RandomUnderSampler**|Randomly _removes_ majority class samples|Decreases majority class size|
|**SMOTETomek**|SMOTE + removes "Tomek links" (majority samples that are nearest neighbors to minority samples)|Cleans decision boundary after oversampling|

**Visual example (starting with 1000 legit, 10 fraud):**

```
SMOTE:           1000 legit, 1000 fraud (synthetic)
Undersampling:   20 legit,   10 fraud   (with 0.5 ratio)
SMOTETomek:      ~950 legit, 1000 fraud (SMOTE + boundary cleanup)
```

# Loss-based Techniques

## Class weights vs. Focal Loss

**What's the difference between class weights vs. focal loss?**
Both address class imbalance, but they work differently:

|Aspect|Class Weights|Focal Loss|
|---|---|---|
|**What it does**|Multiplies loss by fixed weight per class|Down-weights _easy_ examples dynamically|
|**Focus**|Class membership|Prediction confidence|
|**Static vs Dynamic**|Static (same weight for all minority samples)|Dynamic (adapts per sample based on model's confidence)|

**Standard cross-entropy loss (for positive class):**

```
loss = -log(p)

When p = 0.95 (confident correct): -log(0.95) = 0.05  (low loss)
When p = 0.10 (confident wrong):   -log(0.10) = 2.30  (high loss)
```

**Focal loss:**

```
loss = -(1-p)^γ * log(p)
```

**Class Weights:**
```python
# Every fraud sample gets same 100x weight, regardless of difficulty
loss = -100 * y * log(p)  # fraud
loss = -1 * (1-y) * log(1-p)  # legit
```

**Focal Loss:**
```python
# Hard examples (low confidence) get higher weight
# Easy examples (high confidence) get down-weighted
loss = -α * (1-p)^γ * y * log(p)

# γ (gamma) controls focus on hard examples
# γ=0: same as regular cross-entropy
# γ=2: common default, strongly down-weights easy cases
```

**Example with γ=2:**

| Model confidence   | (1-p)^γ weight | -log(p) | Focal loss   | Effect         |
| ------------------ | -------------- | ------- | ------------ | -------------- |
| p=0.95 (easy)      | 0.0025         | 0.05    | **0.000125** | Almost ignored |
| p=0.50 (uncertain) | 0.25           | 0.69    | **0.173**    | Moderate       |
| p=0.10 (hard)      | 0.81           | 2.30    | **1.86**     | High focus     |

**When to use which:**

|Scenario|Better choice|
|---|---|
|Simple imbalance, similar difficulty|Class weights|
|Many easy negatives drowning signal|Focal loss|
|Object detection (RetinaNet origin)|Focal loss|
|Fraud detection with hard cases|Focal loss (learns boundary better)|

**For AML:** Focal loss could be better because:

1. Most legit transactions are "obviously legit" → down-weight them
2. Hard boundary cases get more attention
3. Complements your earlier point about keeping hard examples

XGBoost doesn't have built-in focal loss, but LightGBM does via custom objective, or you can use it with neural networks.

# Footnote 
 [^1]: https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html
