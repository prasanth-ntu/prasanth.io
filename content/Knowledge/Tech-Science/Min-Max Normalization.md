---
tags:
  - machinelearning
  - datascience
  - DataAnalytics
  - featurescaling
  - Math
---

## The Min-Max Normalization Formula

Min-Max normalization (also known as feature scaling) performs a linear transformation on the original data. It rescales the data from its original range to a new range `[0, 1]`[^1][^2]. The formula is:

$X_{normalized}​=(X​−X_{min​})\div(X_{max}−X_{min​})​$

Where:
- $X$ is the original value.
- $X_{min}$​ is the minimum value in the dataset.
- $X_{max​}$ is the maximum value in the dataset.
- $X_{normalized}$ is the normalized/scaled value.

Min-max normalization preserves the relationships among the original data values. The cost of having this bounded range is that we will end up with smaller standard deviations, which can suppress the effect of outliers.
## How It Handles Negative Numbers

> [!HINT] The results will always be within the range [0, 1], and the negative values will not remain negative after normalization.

The formula works the same way regardless of whether the numbers are positive or negative. Let's walk through an example with negative values.

Suppose your dataset is: `$[-10, -5, 0, 15, 20]$`
1. **Identify the Min and Max:**
    - $X_{min}​=−10$
    - $X_{max}​=20$
2. **Calculate the Range:**
    - The range is $X_{max}​−X_{min}​=20−(−10)=30$
3. **Normalize Each Value:**
    - For the minimum value ($-10$):
        $\frac{-10−(−10)}{30}=\frac{0}{30}​=0$
        The minimum value always becomes $0$.
    - For a negative value ($-5$):
        $\frac{-5−(−10)}{30}=\frac{5}{30}​\approx 0.167$
    - For the maximum value ($20$):
        $\frac{20−(−10)}{30}=\frac{30}{30}​=1$
        The maximum value always becomes $1$.
        
As you can see, the negative number −5 was successfully transformed into a positive value between 0 and 1. The key is that by subtracting the minimum value (which is negative in this case), you are effectively shifting all the data points up so that the lowest value starts at zero.

---

[^1]: https://www.oreilly.com/library/view/hands-on-machine-learning/9781788393485/fd5b8a44-e9d3-4c19-bebb-c2fa5a5ebfee.xhtml

[^2]: https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization)
