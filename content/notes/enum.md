---
tags:
  - documentation
  - python
  - software-engineering
  - tool
aliases:
  - Knowledge/Tech-Science/enum
---
# Example
```python
import enum

# Define a structured enum class to capture the result.
class SummaryRating(enum.Enum):
  VERY_GOOD = '5'
  GOOD = '4'
  OK = '3'
  BAD = '2'
  VERY_BAD = '1'

  rating = SummaryRating.VERY_GOOD

print(rating)
print(type(rating))
print(rating.name)
print(rating.value)
```

```output
SummaryRating.VERY_GOOD 
<enum 'SummaryRating'>
VERY_GOOD 
5
```