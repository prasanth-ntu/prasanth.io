---
tags:
  - Python
  - Programming
  - softwareengineering
draft: false
---
Source: https://python-poetry.org/docs/managing-environments/

`Poetry` is a ==tool for managing a single Python project==. It handles creating a virtual environment, installing the libraries your project needs (like `pandas` or `requests`), and packaging your project for distribution. It is an alternative to using `pip`, `venv`, and a `requirements.txt` file.

- **Primary Goal:** To manage the libraries and environment for a specific project in an isolated way.
- **What it Manages:** Project dependencies (the libraries your code uses) and the project's virtual environment. It uses a `pyproject.toml` file to track everything.
- **Use Case:** You start a new project and want to install `requests`. You run `poetry add requests`, and Poetry installs it into a dedicated virtual environment just for that project.

## Configs
Having the virtual environment in the project directory is better for maintenance and traceability. Poetry supports this through configuration as follows
```bash
poetry config virtualenvs.in-project true
```

# Useful commands
```bash
poetry init
poetry add <package>
poetry lock
poetry install
poetry env info
poetry env activate
poetry run <command>
```

## Setting up poetry
```bash
make setup
pyenv local 3.12.2
poetry env activate
source .venv/bin/activate 
poetry install
cp configs/secret.ini.example configs/secret.ini 
make dev
```

To remove existing virtual environment,
```
poetry env remove python3.11
```

To test venv works
```bash
poetry env info
```

Great question! If you manually edit `pyproject.toml`, you need to follow a specific workflow to ensure everything stays in sync. Here's the proper process:

## **Manual Edit Workflow Example**
**Step 1: Edit `pyproject.toml`**
Make your changes directly in the file (like adding dependencies, changing versions, etc.)

**Step 2: Update the Lock File**
```bash
poetry lock
```
This resolves dependencies and updates `poetry.lock` with exact versions, but **doesn't install anything yet**.

**Step 3: Install the Changes**
```bash
poetry install
```
This actually installs/updates/removes packages based on your changes.

**Summary: Manual Edit Workflow**
**The Two-Step Process:**
1. **`poetry lock`** - Resolves dependencies and updates lock file
2. **`poetry install`** - Actually installs/updates packages

**Why This Two-Step Process?**
- **`poetry lock`**: Resolves all dependencies and creates a deterministic lock file
- **`poetry install`**: Installs packages based on the lock file (faster and more reliable)

**When to Use Manual Edits vs `poetry add`:**
- **Use `poetry add`**: For adding new packages (recommended)
- **Use manual edits**: For complex changes like:
  - Changing version constraints
  - Adding development dependencies
  - Modifying project metadata
  - Adding dependency groups

**Other Manual Edit Examples:**
```toml
# Add development dependencies
[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
black = "^23.0.0"

# Add optional dependencies
[tool.poetry.group.optional.dependencies]
jupyter = "^1.0.0"
```

The key is always: **edit → lock → install**! 🔄

## `poetry env activate` explained
The poetry env activate command in Poetry 2.0+ doesn't actually activate the virtual environment directly. Instead, it just shows you the command you need to run to activate it.

For e.g., 
```bash
poetry env activate
source /Users/user/Projects/venvs/py311/.venv/bin/activate
```

Poetry is telling you the exact command you need to run to activate the virtual environment. It's a bit of an extra step compared to the old poetry shell command.

So the correct workflow with Poetry 2.0+ is:
1. `poetry env activate` - shows you the activation command
2. `source /path/to/.venv/bin/activate` - actually activates the environment

Alternatively, you can use `poetry run <command>` to run commands directly in the Poetry environment without manually activating it. For example:
```
poetry run open-webui serve
```

This would run the `open-webui` command in the Poetry virtual environment without needing to activate it first. Would you like me to try that approach instead?