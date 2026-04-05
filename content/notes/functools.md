---
tags:
  - python
  - software-engineering
aliases:
  - Knowledge/Tech-Science/functools
---

# `@functools.total_ordering`
`@total_ordering` lets you define **just `__eq__` and one other comparison method** (like `__lt__`), and it will automatically generate the rest for you.

It reduces boilerplate and ensures consistency between comparison methods.

With `@total_ordering`, you just need:
```python
__eq__, __ne__, __lt__, __le__, __gt__, __ge__
```

Without `@total_ordering`, you’d need to define all the following for full ordering:
```python
__eq__ + one of (__lt__, __le__, __gt__, __ge__)
```

## Examples 
**Without `total_ordering`**
```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __repr__(self):
        return f"{self.name}: {self.gpa}"

a = Student("Alice", 3.5)
b = Student("Bob", 3.7)

print(a < b)   # True
print(a > b)   # False # Python uses fallback mechanism
print(a == b)  # False
print(a <= b)  # True  # TypeError: '<=' not supported between instances of 'Student' and 'Student'
```
> [!NOTE] Even without defining `__gt__`, `a>b` works because Python **uses a fallback mechanism**, when one comparison method isn't defined, *but its reflected counterpart is.*

**With `total_ordering`**
```python
import functools

@functools.total_ordering
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __repr__(self):
        return f"{self.name}: {self.gpa}"

a = Student("Alice", 3.5)
b = Student("Bob", 3.7)

print(a < b)   # True
print(a > b)   # False
print(a == b)  # False
print(a <= b)  # True
```

# Additional resources
[[Caching & Memoization]]


# Examples: `functools.cache`
## Example 1
```python
# Without cache
def add(a: int,b: int) -> int:
  print(f"Running 'add' fn for a={a} & b={b}")
  return a + b


for i in range(5):
  print(add(1,2))
```


```output
Running 'add' fn for a=1 & b=2 
3 
Running 'add' fn for a=1 & b=2 
3 
Running 'add' fn for a=1 & b=2 
3 
Running 'add' fn for a=1 & b=2 
3 
Running 'add' fn for a=1 & b=2 
3
```

```python
@functools.cache
def add(a: int,b: int) -> int:
  print(f"Running 'add' fn for a={a} & b={b}")
  return a + b

for i in range(5):
  print(add(1,2))
```

```output
Running 'add' fn for a=1 & b=2
3
3
3
3
3
```

## Example 2
```python
@functools.cache
def factorial(n):
  print(f'Calculating factorial({n})')
  return n * factorial(n-1) if n else 1

factorial(10) # no previously cached result, makes 11 recursive calls
factorial(5) # just looks up cached value result
factorial(12) # makes two new recursive calls, the other 10 are cached
