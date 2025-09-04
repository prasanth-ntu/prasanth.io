---
tags:
  - Math
  - OptimizationTechniques
  - Programming
  - datascience
  - machinelearning
---
# Linear function
A function is strictly linear if it satisfies two properties:
1. **Homogeneity:** `f(cx) = cf(x)` (scaling the input scales the output by the same factor).
2. **Additivity:** `f(x + y) = f(x) + f(y)` (the function of a sum is the sum of the functions). 
   
A crucial consequence of these properties is that a linear function **must** pass through the origin. If you plug in `x=0`, you will always get `f(0)=0`. The general form of a linear function of one variable is **`f(x) = mx`**

# Affine function
An affine function is a linear function followed by a translation. It doesn't have to pass through the origin. The general form of an affine function of one variable is **`f(x) = mx + c`**, where 'c' is the translation constant (the y-intercept). If `c` is zero, the affine function is also a linear function.

An affine function is a mathematical expression formed by a linear transformation and a translation (or shift). In its simplest form, for a function from one real number to another, it can be expressed as f(x) = mx + b, where m is the slope and b is the y-intercept. Affine functions preserve collinearity and parallelism, meaning straight lines remain straight lines and parallel lines remain parallel after an affine transformation. 

![[linear-and-affine-functions-example.png]][^2]

> [!TIP] All linear functions are affine functions, but not all affine functions are linear

> [!WARNING] In many high school math classes, **anything that graphs as a straight line is called a linear function**. However, in more advanced mathematics, like linear algebra, the definitions become stricter.


# Convex and concave function
![[convex-and-concave-function.png]][^1]

> [!TIP] A straight line (so, linear and affine functions) is both concave and convex function.[^3]

For more details, refer [concave-convex.ipynb](https://colab.research.google.com/gist/prasanth-ntu/be0e982cce3f4f255f86d10c5924d9e4/concave-convex.ipynb)
# Concave function
...

# Convex function
...

**3 key properties of convex function:**

> [!NOTE] Property 1: The Pointwise Maximum of Convex Functions is Convex.

i.e., If you have a collection of convex functions $f_1(x), f_2(x), ..., f_k(x)$, then the new function $h(x) = \max(f_1(x), f_2(x), ..., f_k(x))$ is also convex. 

![[point-wise-max-of-convex-fn-is-convex.png]]

> [!NOTE] Property 2. The Sum of Convex Functions is Convex.

i.e., If $f_1(x)$ and $f_2(x)$ are convex functions, then their sum $f(x) = f_1(x) + f_2(x)$ is also convex. This extends to any finite sum of convex functions.

![[sum-of-convex-fn-is-convex.png]]

> [!NOTE] Property 3: Subtracting an Affine Function from a Convex Function Preserves Convexity.

![[subtracting-affine-fn-from-convex-fn-preerves-convexity.png]]

---
[^1]: https://www.xenonstack.com/glossary/concave-and-convex-function

[^2]: https://www.google.com/url?sa=i&url=https%3A%2F%2Fmath.stackexchange.com%2Fquestions%2F3361379%2Faffine-and-linear-functions&psig=AOvVaw2gytlwDDkWdFGVaWBLoz-6&ust=1755945282428000&source=images&cd=vfe&opi=89978449&ved=0CBkQ3YkBahgKEwjItJyInJ6PAxUAAAAAHQAAAAAQgwE

[^3]: https://math.stackexchange.com/questions/611633/is-linear-function-convex-or-concave
