---
tags:
  - data-science
  - machine-learning
  - statistics
aliases:
  - Knowledge/Tech-Science/Encodings
---
# OneHotEncoder
> [!SUMMARY] **`OneHotEncoder`** is a transformer that converts categorical variables into a binary matrix, where each unique category becomes a new column containing 1s and 0s. Unlike ordinal encoding, it does not assume a natural order between categories, making it ideal for nominal data like colors or city names. 

**Essential Parameters** 
- **`sparse_output`**: (Boolean, default=`True`) Determines whether the result is returned as a memory-efficient sparse matrix or a dense NumPy array.
    - _Note: In older versions, this was simply named `sparse`._
- **`handle_unknown`**: Set to `'ignore'` to handle categories in the test set that were not seen during training; this will result in a row of all zeros for that feature.
- **`drop`**: Used to avoid multicollinearity (the "dummy variable trap") by dropping one category per feature. Common values include `'first'` or `'if_binary'`.
- **`min_frequency` / `max_categories`**: Allows you to group infrequent categories into a single "Other" column to prevent the feature space from exploding. 

**Basic Implementation**
```python
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Data with 2 nominal features
df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green'], 'City': ['NY', 'LDN', 'NY']})

# Instantiate with dense output for visibility
encoder = OneHotEncoder(sparse_output=False)

# Fit and transform
encoded_data = encoder.fit_transform(df)

# Retrieve column names for the new binary features
feature_names = encoder.get_feature_names_out()
encoded_df = pd.DataFrame(encoded_data, columns=feature_names)
```

**When to Use**
- **Nominal Data**: When there is no inherent ranking (e.g., "Cat," "Dog," "Bird").
- **Linear Models / SVMs**: These algorithms often require one-hot encoding because they cannot handle categorical strings directly and need numeric binary inputs.
- **Low to Medium Cardinality**: For features with thousands of unique values (high cardinality), consider Target Encoding or Hashing to keep the dataset size manageable.

For more details, visit scikit-learn official API doc[^1]
# OrdinalEncoder

> [!TIP] **`OrdinalEncoder`** is a preprocessing transformer used to convert categorical features into numerical integers. It is specifically designed for features with a natural ranking (e.g., "low," "medium," "high"). 

Unlike `LabelEncoder`, which is meant for the **target variable** (𝑦), `OrdinalEncoder` is optimized for **input features** (𝑋) and can transform multiple columns simultaneously. 

![How to Perform Ordinal Encoding Using Sklearn - GeeksforGeeks](data:image/jpeg;base64,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)

![How to Perform Ordinal Encoding Using Sklearn - GeeksforGeeks](data:image/jpeg;base64,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)

Key Parameters and Usage 
- **`categories`**: By default (`'auto'`), it determines categories from the data and sorts them alphabetically. To specify a custom order, pass a **list of lists** where each inner list represents the ordered categories for a column.
- **`handle_unknown`**: Set to `'use_encoded_value'` to handle categories not seen during training. You must also provide an `unknown_value` (e.g., `-1`).
- **`encoded_missing_value`**: Allows you to explicitly set the integer value for missing data (e.g., `np.nan`).
- **`min_frequency` / `max_categories`**: Used to group infrequent categories into a single "other" category, reducing dimensionality (added in Scikit-learn 1.1+). 

*Python Example *
This example demonstrates how to set a custom order for a "Size" column: 

```python
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

# Sample data
df = pd.DataFrame({'Size': ['Medium', 'Small', 'Large', 'Medium']})

# Define the order: Small=0, Medium=1, Large=2
categories = [['Small', 'Medium', 'Large']]
encoder = OrdinalEncoder(categories=categories)

# Fit and transform
df['Size_Encoded'] = encoder.fit_transform(df[['Size']])
print(df)
```

**When to Use** 
- **Ordinal Data**: Use when the relative order matters (e.g., Education levels: High School < Bachelor's < PhD).
- **Tree-based Models**: Random Forests and Gradient Boosting models often perform better with `OrdinalEncoder` than `OneHotEncoder` because it keeps the feature space compact.
- **Avoid for Linear Models**: If there is no inherent order, using `OrdinalEncoder` can introduce a fake relationship that confuses linear models; use [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) instead. 

For more detailed technical specifications, refer to the official Scikit-learn OrdinalEncoder documentation[^2].

# Target Encoder
> [!SUMMARY] `TargetEncoder` is a preprocessing transformer designed to encode categorical features into numerical values based on the target variable. It is specifically useful for high-cardinality features where techniques like one-hot encoding would create too many sparse columns. 

**Core Functionality** 
- **Encoding Logic:** Each category is replaced with a **shrunk mean** of the target variable for that specific category.
    - **Regression:** Replaced by the mean value of the target for the category.
    - **Classification:** Replaced by the conditional probability (expected value) of the target given that category.
- **Smoothing:** It applies a shrinkage/smoothing parameter to move categorical means toward the global target mean, which helps handle rare categories and prevents extreme values.
- **Automatic Overfitting Prevention:** In `fit_transform`, it uses an **internal cross-fitting scheme**. It splits training data into 𝑘 folds and encodes each fold using the values learned from the other 𝑘−1 folds, preventing the model from "memorizing" labels. 

**Usage Example**: Regression
```python
from sklearn.preprocessing import TargetEncoder
import pandas as pd

# Sample data with categories and a target
X = pd.DataFrame({'city': ['New York', 'London', 'New York', 'Paris', 'London']})
y = [10, 20, 15, 30, 25]

# Initialize with 'auto' smoothing and target detection
encoder = TargetEncoder(smooth="auto", target_type="continuous")

# Use fit_transform on training data to enable cross-fitting
X_encoded = encoder.fit_transform(X, y)

# Use transform on new data (uses the global means learned during fit)
new_data = pd.DataFrame({'city': ['New York', 'Tokyo']})
new_encoded = encoder.transform(new_data) # Tokyo will use the global mean

print(new_encoded) 

# Output
# array([[12.94117647],
#       [20.        ]])
```

Here is the exact breakdown of how those numbers are calculated.
 1. The Value for 'Tokyo' (20.0)
	- **Logic:** 'Tokyo' is a category that the encoder never saw during the training phase.
	- **Formula:** When a category is unknown (count = 0), the encoder defaults entirely to the **Global Mean**.
	- **Calculation:**    
	    - Target `y` values: `[10, 20, 15, 30, 25]`
	    - Sum: 100
	    - Count: 5
	    - Global Mean = $100 / 5 = \mathbf{20.0}$
2. The Value for 'New York' (12.9411...)
	- This value comes from mixing the **Local Mean** of New York with the **Global Mean**. This is done to prevent overfitting (e.g., if New York only had 1 data point, we wouldn't want to trust it 100%).
	- Sklearn uses this formula for the encoding:

$$\text{Encoded Value} = \frac{n \times \text{LocalMean} + m \times \text{GlobalMean}}{n + m}$$
	
- Where:
	- $n$: The count of the category (For 'New York', $n=2$).
	- $\text{LocalMean}$: The average of 'New York' values ($[10, 15]$), so $12.5$.
	- $\text{GlobalMean}$: $20.0$.
	- $m$: The **smoothing parameter**. (Since you set `smooth="auto"`, sklearn calculated a specific value for $m$ based on the variance of your data).

**Usage Example: Classification**
```python
from sklearn.preprocessing import TargetEncoder
import pandas as pd
import numpy as np

# 1. Generate a robust synthetic dataset (300 rows)
np.random.seed(42)
n_samples = 300

# Create categories with different underlying probabilities of success (1)
# High: ~80% success, Medium: ~50% success, Low: ~20% success
categories = np.random.choice(['High_Prob', 'Medium_Prob', 'Low_Prob'], size=n_samples)
y = []


for cat in categories:
    if cat == 'High_Prob':
        y.append(np.random.choice([0, 1], p=[0.2, 0.8]))
    elif cat == 'Medium_Prob':
        y.append(np.random.choice([0, 1], p=[0.5, 0.5]))
    else: # Low_Prob
        y.append(np.random.choice([0, 1], p=[0.8, 0.2]))

X = pd.DataFrame({'category': categories})
y = np.array(y)

print("--- Data Summary ---")
print(X['category'].value_counts())
print(f"Global Target Mean: {np.mean(y):.4f}\n")

# 2. Initialize TargetEncoder
# With sufficient data, we can use the default cv=5 safely.
# This splits data into 5 folds: training on 4, encoding the 5th.
encoder = TargetEncoder(smooth="auto", cv=5)

# 3. Fit and Transform (Training Phase)
# The values here represent the probability of the target being 1.
# Because of CV=5, different rows of the same category will get slightly different values
# depending on which fold they fell into.
X_encoded = encoder.fit_transform(X, y)

# 4. Analyze the Results
# TargetEncoder returns a 2D array (n_samples, 1). We need to flatten it for the DataFrame.
results = pd.DataFrame({
    'Category': X['category'],
    'Target': y,
    'Encoded_Value': X_encoded.ravel()
})

print("--- Comparison: Raw Mean vs Encoded Value ---")
# We group by category to see how the encoder handled each group
summary = results.groupby('Category').agg(
    Count=('Target', 'count'),
    Raw_Mean=('Target', 'mean'),       # The actual average in the data
    Encoded_Mean=('Encoded_Value', 'mean'), # The average of the encoded values
    Encoded_Min=('Encoded_Value', 'min'),   # SHOWS VARIATION
    Encoded_Max=('Encoded_Value', 'max')    # SHOWS VARIATION
)
print(summary)
print("\nNotice: 'Encoded_Min' and 'Encoded_Max' are different for the same category.")
print("This confirms that fit_transform produced different values for the same category")
print("because it calculated means using different Cross-Validation folds.\n")

# 5. Transform New Data (Test Phase)
# 'Unknown_City' is a category the model has never seen.
new_data = pd.DataFrame({'category': ['High_Prob', 'Medium_Prob', 'Low_Prob', 'Unknown_City']})
new_encoded = encoder.transform(new_data)

print("--- New Data Transformation ---")
# When using .transform(), the variance disappears. Every 'High_Prob' gets the same value.
new_data['encoded_value'] = new_encoded.ravel()
print(new_data)
print("\nNote: During .transform(), the encoder uses the full training set average,")
print("so there is no variance for the same category anymore.")
```

Output
```
--- Data Summary ---
category
Low_Prob       107
High_Prob       99
Medium_Prob     94
Name: count, dtype: int64
Global Target Mean: 0.4933

--- Comparison: Raw Mean vs Encoded Value ---
             Count  Raw_Mean  Encoded_Mean  Encoded_Min  Encoded_Max
Category                                                            
High_Prob       99  0.868687      0.866779     0.856706     0.877825
Low_Prob       107  0.214953      0.216307     0.197529     0.246293
Medium_Prob     94  0.414894      0.414476     0.393589     0.442245

Notice: 'Encoded_Min' and 'Encoded_Max' are different for the same category.
This confirms that fit_transform produced different values for the same category
because it calculated means using different Cross-Validation folds.

--- New Data Transformation ---
       category  encoded_value
0     High_Prob       0.866965
1   Medium_Prob       0.415696
2      Low_Prob       0.216699
3  Unknown_City       0.493333

Note: During .transform(), the encoder uses the full training set average,
so there is no variance for the same category anymore.
```

**Key Advantages & Disadvantages** 
- **Pros:**
    - Keeps the feature space compact (retains one column instead of 𝑁 columns).
    - Captures a direct relationship between the feature and the target.
- **Cons:**
    - High risk of **data leakage** if not used with internal cross-fitting (handled automatically by `fit_transform` in Scikit-learn).
    - Can lead to overfitting if categorical cardinality is extremely high relative to the number of samples. 

**Related Libraries** 
For advanced target encoding methods (like Leave-One-Out, James-Stein, or M-estimate), many practitioners use the [Category Encoders](https://contrib.scikit-learn.org/category_encoders/) library, a Scikit-learn-contrib package.

# Label Encoder

Encode target labels with value between 0 and n_classes-1.

> [!WARNING] This transformer should be used to encode target values, _i.e._ `y`, and not the input `X`.

Converts categorical text labels (like "cat", "dog") into unique numbers (0, 1, 2...) essential for machine learning models that need numerical input, assigning each category a distinct integer without implying order, though it's best for encoding target variables (y) rather than input features (X) to avoid misinterpreting numerical order. 

**How it works**
- **Encoding:** It maps each unique category to an integer from 0 to n-1 (where 'n' is the number of classes).
- **`fit_transform()`:** Combines learning the categories and applying the transformation.
- **`classes_` attribute:** Shows the original categories learned.
- **`inverse_transform()`:**
     Converts numbers back to original labels    

**Example (Python)**
```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
labels = ["cat", "dog", "bird", "cat"]
encoded_labels = le.fit_transform(labels)
print(encoded_labels) # Output: [1 2 0 1] (order depends on alphabetical sort)
```

- **Note:** It's typically for the _target_ variable (y) because assigning numbers to features (X) can wrongly imply order (e.g., 2 > 1), which might confuse some models. For features, One-Hot Encoding is often preferred.
 
Scikit-learn's `LabelEncoder` sorts labels in **alphabetical (lexicographical) order** before assigning integer values, starting from 0. 
For example, if you have the labels `['cat', 'dog', 'bird']`:
- `'bird'` will be assigned `0`
- `'cat'` will be assigned `1`
- `'dog'` will be assigned `2`

For more details, visit official scikit-learn doc [^3].
# Summary Comparison

| Encoder            | Used For                | Feature Type       | Cardinality | Purpose                                | Why?                                                                                                             |
| ------------------ | ----------------------- | ------------------ | ----------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **OrdinalEncoder** | **Input Features (𝑋)** | Ordinal (Ordered)  | Any         | Ranking categories (Low=0, High=2)     | Preserves meaningful hierarchy (e.g., Cold < Warm < Hot).                                                        |
| **OneHotEncoder**  | **Input Features (𝑋)** | Nominal (No order) | Low (< 15)  | Creating binary columns (0s and 1s)    | Prevents model from assuming a fake rank without creating too many columns.                                      |
| **TargetEncoder**  | **Input Features (𝑋)** | Nominal (No order) | High (> 15) | Replacing categories with target means | Efficiently handles many categories (e.g., Zip Codes, bank account numbers) by linking them to the outcome (𝑦). |
| **LabelEncoder**   | **Only Target (𝑦)**    | Nominal            | Low         | Simple integer mapping (0, 1, 2)       | Standardizes the output labels into integers (0, 1, 2) for classification algorithms.                            |

> [!WARNING] **High Cardinality:** If you have millions of unique identifiers (like banking account number), even `TargetEncoder` can struggle. In those cases, **Feature Engineering** (extracting parts of the ID) or **Feature Hashing** is preferred.
# Footnote

[^1]: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html

[^2]: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html

[^3]: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
