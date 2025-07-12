---
tags:
  - Python
  - Programming
  - Coding
  - Library
---

The purpose of `defaultdict` in Python (from the `collections` module) is to simplify handling missing keys in a dictionary by automatically assigning them a default value type when they’re first accessed.

`defaultdict` saves you from writing repetitive code to check and initialize missing keys, making your code cleaner and safer.

# **Common Use Cases**
- **Grouping items**:
```python
from collections import defaultdict
grouped = defaultdict(list)
for key, value in some_data:
    grouped[key].append(value)
```
    
- **Counting**:
```python
from collections import defaultdict
count = defaultdict(int)
for item in data:
    count[item] += 1
```

- **Set-based accumulations**:
```python
from collections import defaultdict
unique = defaultdict(set)
unique['a'].add('x')
```

# Examples
## Example 1: Grouping
**Without  `defaultdict`**
If you try to access a key that doesn’t exist in a normal dictionary, you’ll get a `KeyError`.

```python
d = {}
d['a']  # KeyError
```

You often have to use a pattern like:

```python
# Pattern 1
d = {}
if 'a' not in d:
    d['a'] = []
d['a'].append(1)

# Pattern 2
d = {}
d['a'] = d.get('a',[])
d['a'].append(1)
```


**With  `defaultdict`**
You can define what the default value should be for missing keys using a factory function (like list, int, set, etc.):

```python
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)  # No KeyError, creates d['a'] = [] automatically
```

## Example 2: Counting
```python
data = 'mississippi'
count_d = defaultdict(int)
for letter in data:
  count_d[letter] += 1
count_d.items()
```

```output
dict_items([('m', 1), ('i', 4), ('s', 4), ('p', 2)])
```