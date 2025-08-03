---
tags:
  - machinelearning
  - datascience
  - DataAnalytics
  - IDE
  - softwareengineering
  - Programming
  - Coding
  - Tool
  - OpenSource
---

Source: https://jupyter.org/
# Jupyter notebook & its variants
# Extensions

# Magic commands or Instructions
## `%%capture`
Suppress the standard output and standard error of the cell it's used in.

For e.g.,`%%capture` can be applied to a cell that contains several `!pip install` commands. This means that when you run this cell, you won't see the typical output from pip, such as download progress, installation messages, or potential warnings/errors, unless the command explicitly fails and raises an exception.

It's often used when the output is very long and might clutter the notebook, or when you don't need to see the details of the installation process.

## `%load_ext sql`
This line prepares your Jupyter Notebook environment to understand and execute SQL commands by loading the `sql` extension.

## ## `%%sql`
Run SQL query in the current code cell.

## `%sql sqlite:///sample.db`
Create and connect to SQLite database in the same directory as our jupyter notebook.



