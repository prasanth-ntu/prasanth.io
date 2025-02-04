---
tags:
  - DataScience
  - MachineLearning
  - SoftwareEngineering
  - Programming
---
# Sources
- [How to Auto-Format Your Python Code with Black](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)

# Why formatting our python code is important
- Readability
- It will help in coding interviews
- Team support
- It makes it easy to spot bugs

# # Pylint and Flake8
> [!WARNING] The problem is that these tools only report the problems they identify in the source code and leave the burden to the Python developers to fix them!

# Introduction to Black
> [!TIP] **Black** is a tool that allows you to **identify errors** and **format your python code** at the same time.

## Key commands
- Format a single file: 
	- `black sample_code.py`
- Format multiple files: 
	- `black folder_name/`
- Checking files for formatting (doesn't modify the files): 
	- `black --check`
	- `black --check --diff file_name.py`
- Change number of characters per line
	- `black -l 60 python_file.py`

# Black in Jupyter Notebook
...
