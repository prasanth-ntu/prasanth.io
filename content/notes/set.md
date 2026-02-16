---
tags:
  - python
  - software-engineering
aliases:
  - Knowledge/Tech-Science/set
---
`issubset(_other)` or `set <= other`
- Test whether every element in the set is in _other_.

```python
import string
alphabet = string.ascii_lowercase
print (f"alphabet: {alphabet}")

a = "apple"
print (f"a.issubset(alphabet): {set(a).issubset(set(alphabet))}")
```

```output
alphabet: abcdefghijklmnopqrstuvwxyz 
a.issubset(alphabet): True

