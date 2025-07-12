---
title: datetime - Basic date and time types
tags:
  - Python
  - Programming
  - Coding
  - Library
  - Documentation
---
# Examples
## Convert string dates to datetime objects  & vice versa 
```python
from datetime import datetime, timedelta

date_str = '2025-05-01'
# string to datetime object
date_obj = datetime.strptime(date_str, '%Y-%m-%d')
# datetime object to string
date_str_2 = datetime.strftime(date_obj, '%Y-%m-%d')
print(f"date str to object: {date_obj}")
print(f"date object to str: {date_str_2}")
```

```output
date str to object: 2025-05-01 00:00:00
date object to str: 2025-05-01
```

> [!NOTE] The difference is in the date `type` of the two variables

```python
print(type(date_obj))
print(type(date_str_2))
```

```output
<class 'datetime.datetime'>
<class 'str'>
```

> [!TIP] This `strftime` can be even used on `pandas.series`
> For more details, refer [[Pandas#Generate date range]]

