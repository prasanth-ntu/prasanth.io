---
tags:
  - documentation
  - machine-learning
  - python
  - software-engineering
aliases:
  - Knowledge/Tech-Science/sklearn
---
# `sklearn.datasets`
Datasets that I have worked/used so far are from

| Dataset Name               | Loaders                                 | Description                                                                                                                                                                                                                                                                                                                                | Example/ Usage                                                     |
| -------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| 20 newsgroups text dataset | `fetch_20newsgroups` - Returns raw text | Comprises around 18000 newsgroups posts on 20 topics (such as 'alt.atheism',<br> 'comp.graphics', ...) split in two subsets: ~60% for training (or development) and the other ~40% for testing (or for performance evaluation). The split between the train and test set is based upon a messages posted before and after a specific date. | [[Google-5-Day-Gen-AI-Intensive-Course#Day 2 Embeddings & Vector]] |
|                            |                                         |                                                                                                                                                                                                                                                                                                                                            |                                                                    |

# sklearn.preprocessing

Methods for scaling, centering, normalization, binarization, and more.

| Methods            | Description                                                                                                      | Example/Usage                |
| ------------------ | ---------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **StandardScaler** |                                                                                                                  | [[Scalers#StandardScaler]]   |
| **MinMaxScaler**   |                                                                                                                  | [[Scalers#MinMaxScaler]]     |
| **RobustScaler**   |                                                                                                                  | [[Scalers#RobustScaler]]     |
| **OrdinalEncoder** | Encode categorical features as an integer array (0 to n-1 categories) preserving an inherent order if specified. | [[Encodings#OrdinalEncoder]] |
|                    |                                                                                                                  |                              |

For more details, refer scikit-learn API reference [^1]

# sklearn.pipeline

 ==A powerful tool used to **chain multiple data processing and modeling steps into a single, cohesive object**==. This streamlines machine learning workflows, making the code cleaner, more maintainable, and robust against common errors like data leakage during cross-validation.

**Core Concepts**
A pipeline consists of a sequence of steps, defined as a list of `(name, estimator)` tuples. 
- **Transformers:** All steps in the pipeline, except the last one, must be transformers. This means they must implement both the `fit` and `transform` methods (e.g., scalers, imputers, feature selectors).
- **Estimator:** The final step can be any type of estimator (e.g., a classifier, regressor, or even another transformer), and it must implement the `fit` method. 

When you call `fit` on the pipeline, each transformer's `fit_transform` method is called in sequence, and the output is passed to the next step. The final estimator then performs only the `fit` operation on the processed data. 

**Key Benefits**
- **Convenience and Encapsulation:** You only need to call `fit` and `predict` once on your data to execute the entire sequence of operations.
- **Reduced Data Leakage:** Pipelines ensure that transformations are fit only on the training data and then applied to both training and test data, preventing information from the test set from contaminating the model training process.
- **Efficient Hyperparameter Tuning:** Pipelines integrate seamlessly with scikit-learn's hyperparameter tuning tools like `GridSearchCV` and `RandomizedSearchCV`, allowing you to optimize parameters for both the preprocessing steps and the final model in a single search.
- **Code Readability and Reproducibility:** By encapsulating the entire workflow, pipelines make the code easier to understand, modify, and reproduce consistently.

**Example Usage**
Refer scikit-learn API reference[^2]

# sklearn.compose
### ColumnTransformer

The `ColumnTransformer` is ==a powerful tool for applying different data preprocessing techniques to specific columns of a dataset simultaneously==, particularly useful for heterogeneous data (e.g., mixed numerical and categorical features). 

**Key Features and Usage**
- **Selective Transformation**: It allows you to apply specific transformers (like `StandardScaler` for numerical data and `OneHotEncoder` for categorical data) to different subsets of columns.
- **Pipeline Integration**: `ColumnTransformer` can be seamlessly integrated into a `Pipeline` object, which ensures that all preprocessing steps are applied consistently to training, validation, and test data, preventing data leakage and simplifying the workflow.
- **Cleaner Code**: It replaces the need for manual, error-prone column selection and concatenation after individual transformations.
- **Column Selection**: Columns can be specified using indices, string names (for pandas DataFrames), boolean masks, or with the help of `make_column_selector` (which can select columns by data type). 

**How to Use It (Example)**
Here is a typical example of how to use `ColumnTransformer` to handle numerical and categorical columns:

```python
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# Sample Data (replace with your actual data)
data = {'numeric_feature': [1, 2, 3, 4, 5],
        'categorical_feature': ['A', 'B', 'A', 'C', 'B'],
        'target': [0, 1, 0, 1, 0]}
df = pd.DataFrame(data)
X = df.drop('target', axis=1)
y = df['target']

# Define which columns are numerical and categorical
numerical_cols = ['numeric_feature']
categorical_cols = ['categorical_feature']

# Define the transformers for numerical and categorical data
numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore') # ignore unknown categories in test set

# Create the ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ],
    remainder='drop' # By default, unspecified columns are dropped (can also be 'passthrough')
)

# Optional: integrate into a full Pipeline with a model
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression()) # Example classifier
])

# Split data and use the pipeline
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model_pipeline.fit(X_train, y_train)
score = model_pipeline.score(X_test, y_test)
print(f"Model score: {score:.3f}")
```

Refer sciki-learn API for more details [^3]

# Pipeline vs. ColumnTransformer

1. **Fundamental Difference**

| Component         | Direction             | Purpose                                                              | Analogy                                                                          |
| ----------------- | --------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Pipeline          | Sequential (Vertical) | Do Step A, then Step B, then Step C on the same data.                | An assembly line: Wash the car $\to$ Paint the car $\to$ Polish the car.         |
| ColumnTransformer | Parallel (Horizontal) | Do X to Column Group 1, and do Y to Column Group 2 at the same time. | A specialized workshop: One team fixes the engine, another team paints the body. |
2. **Can you achieve the same outcome with just one?**
- Using ONLY `Pipeline`:
	- You could try, but it applies every step to every column. If you put `StandardScaler` in a pipeline, it will try to scale your text columns (which will crash) unless you manually separate your dataframes beforehand.
- Using ONLY `ColumnTransformer`:
	- You can split columns, but you can only apply one estimator per column group. If you want to Impute AND Scale a specific column, `ColumnTransformer` alone cannot do that without a Pipeline.

3. **The "Best Practice" Way (Combining Them)**
- To achieve the outcome of "Impute AND Scale numeric columns" while "Impute AND Encode categorical columns," you should nest your pipelines inside the `ColumnTransformer`.

**Summary Checklist**
- Use `Pipeline` when: You have multiple steps for a specific set of data (e.g., Fill NaNs $\to$ Scale).
- Use `ColumnTransformer` when: You have mixed data types (Numeric vs. Categorical) that require different preprocessing.
- Use Both when: You have mixed data types, and each type needs multiple steps of preprocessing.

# sklearn.model_selection
### GridSearchCV

Exhaustive search over specified parameter values for an estimator.

Important members are fit, predict.

GridSearchCV implements a “fit” and a “score” method. It also implements “score_samples”, “predict”, “predict_proba”, “decision_function”, “transform” and “inverse_transform” if they are implemented in the estimator used.

The parameters of the estimator used to apply these methods are optimized by cross-validated grid-search over a parameter grid.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/grid_search.html#grid-search).

# Footnotes

[^1]: https://scikit-learn.org/stable/api/sklearn.preprocessing.html
[^2]: https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html

[^3]: https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html
