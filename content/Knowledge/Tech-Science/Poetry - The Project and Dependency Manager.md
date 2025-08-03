---
tags:
  - Python
  - Programming
  - softwareengineering
---
Source: https://python-poetry.org/docs/managing-environments/

`Poetry` is a ==tool for managing a single Python project==. It handles creating a virtual environment, installing the libraries your project needs (like `pandas` or `requests`), and packaging your project for distribution. It is an alternative to using `pip`, `venv`, and a `requirements.txt` file.

- **Primary Goal:** To manage the libraries and environment for a specific project in an isolated way.
- **What it Manages:** Project dependencies (the libraries your code uses) and the project's virtual environment. It uses a `pyproject.toml` file to track everything.
- **Use Case:** You start a new project and want to install `requests`. You run `poetry add requests`, and Poetry installs it into a dedicated virtual environment just for that project.
# Useful commands
```bash
poetry lock
poetry install

poetry add chromadb@latest


```

# Usual steps
```bash
make setup
pyenv local 3.12.2
poetry env activate
source .venv/bin/activate 
poetry install
cp configs/secret.ini.example configs/secret.ini 
make dev
```
