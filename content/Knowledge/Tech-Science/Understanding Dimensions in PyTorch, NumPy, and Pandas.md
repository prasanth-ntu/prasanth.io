---
tags:
  - machinelearning
  - datascience
  - Numpy
  - Pandas
  - PyTorch
---

# Basic Dimension Concepts

In PyTorch, NumPy, and pandas, dimensions (also called axes) follow a consistent ordering:
- First dimension (dim=0 or axis=0): Represents rows
- Second dimension (dim=1 or axis=1): Represents columns

![[Numpy axis explanation.png]]
Image credit: [Stack overflow post](https://stackoverflow.com/questions/35210647/clear-authoritative-explanation-of-numpy-axis-numbers)

# Visual Representation

For a matrix:
```
[1 2 3]  → dim=1/axis=1 operates along this direction (within each row)
[4 5 6]  ↓ dim=0/axis=0 operates along this direction (down columns)
[7 8 9]
```
# Library Comparison

The same operation across different libraries on a 2x3 array:

```python
import torch
import numpy as np
import pandas as pd
import tensorflow as tf

# PyTorch (uses 'dim')
torch_tensor = torch.tensor([[1, 2, 3],
							 [4, 5, 6]])
torch.sum(torch_tensor, dim=1)  # Sum along rows
# tensor([ 6, 15]) # 

# NumPy (uses 'axis')
np_array = np.array([[1, 2, 3],
                     [4, 5, 6]])
np.sum(np_array, axis=1)  # Sum along rows
# array([ 6, 15])

# Pandas (uses 'axis')
df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6]])
df.sum(axis=1)  # Sum along rows
# 0     6
# 1    15
# dtype: int64

# TensorFlow (uses 'axis')
tf_tensor = tf.constant([[1, 2, 3],
	                     [4, 5, 6]])
tf.reduce_sum(tf_tensor, axis=1) # Sum along rows
```



# Important Notes

1. The negative indexing (-1) refers to the last dimension:
   - `dim=-1` is equivalent to `dim=1` for a 2D matrix
   - This is commonly used in PyTorch as it works regardless of tensor dimensionality

2. In attention mechanisms:
   - We typically use `dim=-1` for softmax to operate row-wise
   - This ensures each token's attention weights sum to 1.0
   - Example: `torch.softmax(attention_scores, dim=-1)`