---
tags:
  - Math
  - Statistics
  - DataAnalytics
  - datascience
draft: true
---
> [!TIP]  We use logarithmic transformations to reduce the skewness in data.


Logarithmic functions is crucial, especially when dealing with skewed data or when transformations are needed to handle specific types of data distributions.[^1]

|                   | `np.log`                                                                                                                                                                                      | `np.log1p`                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Formula           |                                                                                                                                                                                               | `np.log1p(x) = np.log(x+1)`                                                                                                                          |
| How does it work? | Any value less than 1 and close to 0 is outputted as negative.                                                                                                                                | It fixes this issue by shifting the input (adding 1). It ensures the stability even if we have zero value or small value.                            |
| Use case          | Often used in contexts where the natural logarithm is required, such as calculating growth rates, handling exponential data, or transforming data to achieve normality in statistical models. | Generally preferred when applying a log transformation to datasets that may contain values close to zero to ensure numerical stability and accuracy. |

# Footnote
 [^1]: https://medium.com/@noorfatimaafzalbutt/understanding-np-log-and-np-log1p-in-numpy-99cefa89cd30
