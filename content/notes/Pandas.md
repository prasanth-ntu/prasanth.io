---
tags:
  - data-science
  - python
  - software-engineering
  - statistics
  - tool
aliases:
  - Knowledge/Tech-Science/Pandas
---
Parent Doc: [[Python Documentation]]
# API reference
| Module/Function/Attribute           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Example                                                                                                                                                                                                                              |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `pandas.testing.assert_frame_equal` | Check that left and right DataFrame are equal.<br><br>This function is intended to compare two DataFrames and output any differences. It is mostly intended for use in unit tests. Additional parameters allow varying the strictness of the equality checks performed.<br><br>[API reference](https://pandas.pydata.org/docs/dev/reference/api/pandas.testing.assert_frame_equal.html)                                                                                                                                                                       | Especially handy when comparing floating point values, where we can leverage `check_exact` and relative or absolute tolerance (`rtol`  or `atol`) parameters.<br><br>To compare without tolerance, we can just use `df1.equals(df2). |
| `pandas.date_range`                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [[Pandas#Generate date range]]                                                                                                                                                                                                       |
| `pandas.set_option`                 | Sets the value of the specified option.<br><br>Available options:<br>- `compute`<br>- `display`<br>- ...<br><br>My most used ones are <br>- `display.max_rows`<br>- `display.max_columns`<br>- `display.float_format`<br><br>[API reference](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html)                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                      |
| `pandas.option.context`             | Context manager to temporarily set options in the `with` statement context.<br><br>Need to invoke as need to invoke as `option_context(pat, val, [(pat, val), ...])`<br><br>[API reference](https://pandas.pydata.org/docs/reference/api/pandas.option_context.html)                                                                                                                                                                                                                                                                                          | [[Pandas#Displaying all the rows in Pandas DF]]                                                                                                                                                                                      |
| `pandas.merge`                      | Merge DataFrame or named Series objects with a database-style join.<br><br>A named Series object is treated as a DataFrame with a single named column.<br><br>The join is done on columns or indexes. If joining columns on columns, the DataFrame indexes _will be ignored_. Otherwise if joining indexes on indexes or indexes on a column or columns, the index will be passed on. When performing a cross merge, no column specifications to merge on are allowed.<br><br>[API reference](https://pandas.pydata.org/docs/reference/api/pandas.merge.html) |                                                                                                                                                                                                                                      |
# Examples
## Generate date range
```python
import pandas as pd

start_date_str = '2025-05-01'
end_date_str = '2025-05-15'
date_range = pd.date_range(start=start_date_str, end=end_date_str, freq='D')
date_range
```

```output
DatetimeIndex(['2025-05-01', '2025-05-02', '2025-05-03', '2025-05-04',
               '2025-05-05', '2025-05-06', '2025-05-07', '2025-05-08',
               '2025-05-09', '2025-05-10', '2025-05-11', '2025-05-12',
               '2025-05-13', '2025-05-14', '2025-05-15'],
              dtype='datetime64[ns]', freq='D')
```

```python
date_range_str = date_range.strftime('%Y-%m-%d')
date_range_str
```

```output
Index(['2025-05-01', '2025-05-02', '2025-05-03', '2025-05-04', '2025-05-05',
       '2025-05-06', '2025-05-07', '2025-05-08', '2025-05-09', '2025-05-10',
       '2025-05-11', '2025-05-12', '2025-05-13', '2025-05-14', '2025-05-15'],
      dtype='object')
```

> [!NOTE] The difference is in the `dtype` of the two variables

```python
print (date_range.dtype)
print(date_range_str.dtype)
```

```output
datetime64[ns] 
object
```

## Displaying all the rows in Pandas DF
```python
from IPython.display import display

with pd.option_context('display.max_rows', None):
    display(pdf.head().T)
```