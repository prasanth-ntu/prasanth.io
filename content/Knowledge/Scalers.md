---
tags:
  - machinelearning
  - Statistics
  - Math
  - datascience
  - DataAnalytics
---
# StandardScaler

> [!SUMMARY] Standardize features by removing the mean and scaling to unit variance.

The standard score of a sample `x` is calculated as:
```python
z = (x - u) / s
```

where `u` is the mean of the training samples or zero if `with_mean=False`, and `s` is the standard deviation of the training samples or one if `with_std=False`.

Centering and scaling happen independently on each feature by computing the relevant statistics on the samples in the training set. Mean and standard deviation are then stored to be used on later data using [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.transform "sklearn.preprocessing.StandardScaler.transform").

> [!TIP] Standardization of a dataset is a common requirement for many machine learning estimators: they might behave badly if the individual features do not more or less look like standard normally distributed data (e.g. Gaussian with 0 mean and unit variance).

For instance many elements used in the objective function of a learning algorithm (such as the RBF kernel of Support Vector Machines or the L1 and L2 regularizers of linear models) assume that all features are centered around 0 and have variance in the same order. If a feature has a variance that is orders of magnitude larger than others, it might dominate the objective function and make the estimator unable to learn from other features correctly as expected.

> [!WARNING] `StandardScaler` is sensitive to outliers, and the features may scale differently from each other in the presence of outliers. For an example visualization, refer to [Compare StandardScaler with other scalers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#plot-all-scaling-standard-scaler-section).

This scaler can also be applied to sparse CSR or CSC matrices by passing `with_mean=False` to avoid breaking the sparsity structure of the data.

For more details, visit [^1]
# MinMaxScaler

> [!SUMMARY] Transform features by scaling each feature to a given range.

This estimator scales and translates each feature individually such that it is in the given range on the training set, e.g. between zero and one.

The transformation is given by:
```python
X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
X_scaled = X_std * (max - min) + min
```
where min, max = feature_range.

> [!TIP] This transformation is often used as an alternative to zero mean, unit variance scaling.

> [!WARNING] `MinMaxScaler` doesn’t reduce the effect of outliers, but it linearly scales them down into a fixed range, where the largest occurring data point corresponds to the maximum value and the smallest one corresponds to the minimum value. For an example visualization, refer to [Compare MinMaxScaler with other scalers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#plot-all-scaling-minmax-scaler-section).

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-scaler).

For more details, visit [^2]

# RobustScaler

> [!SUMMARY] Scale features using statistics (median and IQR range) that are robust to outliers.

This Scaler removes the median and scales the data according to the quantile range (defaults to IQR: Interquartile Range). The IQR is the range between the 1st quartile (25th quantile) and the 3rd quartile (75th quantile).

$X_{scaled} = \dfrac{X - \text{Median}(X)}{\text{IQR}(X)}$

> [!TIP] This process ensures that the median of the scaled data is 0 and the IQR is 1, while preserving the relative distances of non-outlying data points.

Centering and scaling happen independently on each feature by computing the relevant statistics on the samples in the training set. Median and interquartile range are then stored to be used on later data using the [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler.transform "sklearn.preprocessing.RobustScaler.transform") method.

Standardization of a dataset is a common preprocessing for many machine learning estimators. Typically this is done by removing the mean and scaling to unit variance. However, outliers can often influence the sample mean / variance in a negative way. In such cases, using the median and the interquartile range often give better results. For an example visualization and comparison to other scalers, refer to [Compare RobustScaler with other scalers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#plot-all-scaling-robust-scaler-section).

> [!TIP] It is a useful and robust alternative to `StandardScaler` or `MinMaxScaler` when your data contains many/prominent/extreme values/outliers that you prefer not to remove but gracefully handle them. Especially helpful when working with ML algos that are sensitive to scale of the features (e.g., SVMs, logistic regression or neur)

For more details, visit [^4]

# Comparison of different scalers

For more details, visit [^3]

# Footnote
[^1]: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html

[^2]: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler

[^3]: https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#plot-all-scaling-standard-scaler-section

[^4]: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler
