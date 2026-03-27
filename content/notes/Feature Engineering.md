
## Standarization vs. Normalization

> [!QUESTION] Why standardization is more robust to outliers than normalization.

**Normalization (Min-Max Scaling)**

Normalization rescales values to a fixed range, typically [0, 1], using the formula:

**X_norm = (X - X_min) / (X_max - X_min)**

The problem is that this formula depends entirely on X_min and X_max. If you have even a single extreme outlier, it drastically stretches the denominator. For example, imagine most of your data falls between 10 and 50, but one outlier is 1000. Now X_max - X_min = 990, and all of your "normal" data points get compressed into a tiny range near 0 (roughly 0 to 0.04), losing almost all their granularity. One outlier effectively squashes the useful variation in the rest of your data.

**Standardization (Z-Score Scaling)**

Standardization transforms values using the mean and standard deviation:

**X_std = (X - μ) / σ**

This is more resilient because the mean and standard deviation are computed across *all* data points, not just the two extremes. An outlier will influence μ and σ to some degree, but it won't dominate them the way it dominates min and max. The bulk of your data still retains meaningful spread after the transformation. The outlier will simply show up as a point with a large z-score (e.g., z = 5 or 6), which clearly signals that it's unusual — but it doesn't crush the rest of the distribution into a narrow band.

**In short:**

Normalization is sensitive to outliers because it's anchored to the two most extreme values in the data, meaning a single outlier can distort the entire scaled distribution. Standardization uses aggregate statistics (mean and standard deviation) that are influenced by all observations, making it far less susceptible to being thrown off by a few extreme values.

That said, standardization isn't *immune* to outliers — the mean and standard deviation can still be pulled by extreme values. If outliers are a major concern, you might also consider **robust scaling**, which uses the median and interquartile range (IQR) instead, making it even more resistant to outliers.

# Additional resources
[[Encodings]]
[[Min-Max Normalization]]
[[AWS ML Engineer Associate Learning Plan#1.2 Transform Data]]
