---
tags:
  - softwareengineering
  - Programming
---
# Deep Learning
## float
Refer [[Glossary#Floating Point]]

## float32 (single-precision floating-point) or FP32
This is a standard data type that offers a good balance of range and precision. Most models are initially trained in float32.

## float16 (half-precision floating-point) or FP16
This uses half the memory of float32 and can significantly speed up computations on hardware that supports it (like modern GPUs). However, it has a smaller range and less precision than float32, which can sometimes lead to numerical instability or issues with very small or very large numbers.
## bfloat16 (brain floating-point) or BF16
This data type was designed specifically for deep learning. It also uses half the memory of float32 but has the same range as float32 while sacrificing some precision compared to float16. bfloat16 is generally considered more numerically stable than float16 for deep learning training.


> [!QUESTION] Why are these lower precision data types used?
> - **Reduced Memory Usage:** Using float16 or bfloat16 significantly reduces the amount of memory required to store the model and intermediate computations. This is crucial for training large models that might otherwise not fit into GPU memory.
>  - **Faster Computations:** Modern GPUs have specialized hardware (like Tensor Cores) that can perform calculations much faster using lower precision data types.

## FP32 vs. FP16 vs. BP16

| Feature               | float32 (FP32)                                                               | float16 (FP16)                                                                                       | bfloat16 (BF16)                                                                                                                          |
| --------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Bit width             | 32 bits                                                                      | 16 bits                                                                                              | 16 bits                                                                                                                                  |
| Structure             | 1 sign bit, 8 exponent bits, 23 mantissa bits                                | 1 sign bit, 5 exponent bits, 10 mantissa bits                                                        | 1 sign bit, 8 exponent bits, 7 mantissa bits                                                                                             |
| Dynamic range         | Large (exponent 8 bits)                                                      | Smaller (exponent 5 bits), less range                                                                | Similar to float32 (exponent 8 bits), wide range                                                                                         |
| Precision             | High precision                                                               | Lower precision, more rounding errors                                                                | Lower precision than float32 but better than float16 mantissa-wise                                                                       |
| Numerical stability   | Very stable, less prone to overflow/underflow                                | Prone to overflow or underflow due to smaller exponent range                                         | Better numerical stability than float16 due to same exponent size as float32                                                             |
| Memory usage          | Higher (4 bytes per number)                                                  | Lower (2 bytes per number)                                                                           | Lower (2 bytes per number)                                                                                                               |
| Training implications | Standard for many DL models, stable but more demanding on memory/computation | Saves memory and speeds computation but can cause instability (NaNs) and accuracy loss in some cases | Offers memory savings and faster training like float16 but with better stability and accuracy, often preferred for training large models |
> [!INFO] Empirically, **bfloat16** has been found to increase training throughput (e.g., +18% in some GPT-3 model experiments), and is less prone to numerical instabilities than float16. It also allows storing models and checkpoints more compactly without serious loss of accuracy

## Example
## Positive decimal number bol ↔ IEEE 754 single-precision FP32
#### Positive number (e.g., +1.0)
1. **Convert decimal to binary scientific notation:**  
    $1_{10}=1.0_2×2^0$
2. **Sign bit:**  
    Positive number → sign bit = 0
3. **Exponent:**  
	Exponent = 0 (since $2^0$)  
    Biased exponent = $127+0=127=(01111111)_2$
4. **Mantissa (fractional part):**  
    After the leading 1 (which is implicit), no fractional bits → all 0s  
    Mantissa = `00000000000000000000000` (23 bits)
5. **Combine all bits:**    $\text{sign∣exponent∣mantissa}=0$   $01111111$  $00000000000000000000000$
6.  **Hexadecimal representation:**  
    $0x3F800000$
7. **Interpretation:**  
    This is the float32 encoding of +1.0
#### Convert from float 32 binary to decimal
1. Extract bits:
    - Sign bit $S$: 0 means positive, 1 means negative
    - Exponent bits $E$: 8 bits, interpret as unsigned integer
    - Mantissa bits $M$: 23 bits fraction
2. Compute actual exponent, $e=E−127$ (bias of 127)
3. The mantissa value is $1+\text{fraction}$ represented by $\text{mantissa bits}$ (implicit leading one).
4. Calculate value: $(−1)^S×(1+M)×2^e$

| Decimal | Sign bit | Exponent bits (biased) | Mantissa bits             | Hex          | Explanation  |
| ------- | -------- | ---------------------- | ------------------------- | ------------ | ------------ |
| $+1.0$  | $0$      | $01111111$ (127)       | $00000000000000000000000$ | $0x3F800000$ | $+1×2^0$     |
| $-1.5$  | $1$      | $01111111$ (127)       | $10000000000000000000000$ | $0xBFC00000$ | $−1×1.5×2^0$ |
