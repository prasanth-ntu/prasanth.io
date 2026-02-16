---
tags:
  - python
  - software-engineering
aliases:
  - Knowledge/Tech-Science/Ruff - Python linter and code formatter
---
Source: https://docs.astral.sh/ruff/
Alternative to linters (like Flake8) and formatters (like [[Black]]) 

# `noqa`

## What does `noqa` mean?
Resources: https://stackoverflow.com/questions/45346575/what-does-noqa-mean-in-python-comments

Adding `# noqa` to a line indicates that the linter (a program that automatically checks code quality) should not check this line. Any warnings that code may have generated will be ignored.

That line may have something that "looks bad" to the linter, but the developer understands and intends it to be there for some reason.


- `# noqa` has evolved from the `# nopep8` syntax used in previous releases of flake8
- `# noqa` is supported by IDEs, like PyCharm, for use with their built-in code inspection tools  
- `# noqa` can be used as a pre-commit directive, such that prior to new commits an inspection process must complete
- `# noqa` can be used to ignore all warnings or given specific warnings to ignore. For example, `# noqa: F401` will ignore an unused imported module warning.

### Example
Resources: https://www.alpharithms.com/noqa-python-501210/
As an example, consider the following code:
```python
import os
print("Hello, world!")
```

This code imports the `os` module but doesn't use it. If one wanted to use the `# noqa` tool to suppress a PEP8 warning, it could be written as such:

```python
import os  # noqa
print("Hello, world!")
```

This will ignore _all_ warnings. However, if one were only to want to ignore a specific warning (PEP8 F401 imported but not used), it could be done as such:

```python
import os  # noqa: F401
print("Hello, world!")
```

## `# noqa: N815`
This is a linting directive that tells the code linter to ignore a specific rule:
- `noqa` = "no quality assurance" - tells the linter to skip checking this line
- `N815` is a specific linting rule code

`N815` typically refers to a rule about variable naming conventions - it's probably complaining that `variableNameA` uses camelCase instead of snake_case (which would be `variable_name_a` in Python)

The comment is added to Suppress the linter warning about the camelCase naming convention (likely because this field name matches an external API or database schema).

This is a common pattern when working with external APIs or databases that use different naming conventions than your local codebase.