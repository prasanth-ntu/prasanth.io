---
tags:
  - ai
  - data-science
  - deep-learning
  - machine-learning
  - statistics
aliases:
  - Knowledge/Tech-Science/Activation Functions
---

# Rectified Linear Unit (ReLU)
- If the input is greater than zero, the output is equal to the input.
- If the input is zero or less than zero, the output is zero.

This can be written as: `f(x) = max(0, x)`  

# LeakyReLU

- If the input is greater than zero, the output is equal to the input (same as ReLU).
- If the input is less than or equal to zero, the output is a _small, non-zero multiple_ of the input. This small multiple is typically a constant like 0.01 or 0.1, often denoted by `α` (alpha).

This can be written as: `f(x) = max(αx, x)` where `α` is a small positive constant.  

**Example:**
- If `x = 5`, then `f(5) = max(0.01 * 5, 5) = 5`
- If `x = -2`, then `f(-2) = max(0.01 * -2, -2) = -0.02` (instead of 0 with standard ReLU)
## How LeakyReLU  helps prevent "dying ReLU" problems?
  
> [!WARNING] The "dying ReLU" problem occurs in standard ReLU when neurons get stuck in a state where they always output zero. This happens if the input to a ReLU neuron is consistently negative.

1. **Zero Gradient for Negative Inputs (ReLU):**
    - For any negative input, the output of a standard ReLU is 0.
    - More importantly, the _gradient_ (or derivative) of the ReLU function for any negative input is also 0.
    - During backpropagation (how neural networks learn by adjusting weights based on errors), the gradients are used to update the weights. If the gradient is 0, then the weights associated with that neuron will not be updated.
2. **The "Dying" State:**
    - If a neuron's weights are adjusted during training such that its input becomes consistently negative for many data samples, it will always output 0.
    - Since its output is 0, and its gradient is 0 for negative inputs, it effectively stops learning. No matter what data passes through it, it won't activate, and its weights won't change. It's "dead" or "dying" because it contributes nothing to the learning process.
3. **LeakyReLU's Solution:**
    - LeakyReLU introduces a small, non-zero gradient for negative inputs. Even if the input is negative, there's a slight slope (`α`).
    - This means that even when a neuron receives negative inputs, there's still a _non-zero gradient_ flowing back through it during backpropagation.
    - Because there's a non-zero gradient, the weights associated with that neuron can still be updated. This allows the neuron to potentially recover from a state where it was receiving consistently negative inputs, preventing it from becoming permanently "dead." It can still learn and adjust, even for negative activations, pulling it out of the zero-gradient trap.

> [!SUMMARY] In summary, LeakyReLU's small negative slope ensures that neurons always have _some_ gradient, allowing them to continue learning even when their inputs are negative, thus mitigating the "dying ReLU" problem that can hinder training.