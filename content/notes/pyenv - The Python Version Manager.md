---
tags:
  - python
  - software-engineering
draft: false
aliases:
  - Knowledge/Tech-Science/pyenv - The Python Version Manager
---

# pyenv - The Python Version Manager

## What is pyenv?

`pyenv` lets you ==install, manage, and switch between multiple versions of Python== itself. You can have Python 3.8, 3.9, 3.10, and 3.11 all installed on the same machine without them interfering with each other.

- **Primary Goal:** Select which version of Python your computer or a specific project should use
- **What it Manages:** The Python interpreters installed on your system
- **Use Case:** Work on an old project requiring Python 3.7 while your new project needs Python 3.11

## Installation

### macOS

```bash
# Using Homebrew (recommended)
brew install pyenv

# Add to shell configuration (~/.zshrc or ~/.bashrc)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Restart shell or source config
source ~/.zshrc
```

### Linux

```bash
# Using installer
curl https://pyenv.run | bash

# Add to shell configuration (~/.bashrc or ~/.zshrc)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Restart shell or source config
source ~/.bashrc
```

**Verify installation:**

```bash
pyenv --version
```

## Managing Python Versions

### Installing Python Versions

```bash
# List all available Python versions
pyenv install --list

# Install a specific version
pyenv install 3.11.7

# Install the latest 3.11 version
pyenv install 3.11

# Install multiple versions
pyenv install 3.10.13
pyenv install 3.12.1
```

### Viewing Installed Versions

```bash
# List all installed Python versions
pyenv versions

# Show the currently active version
pyenv version
```

### Uninstalling Python Versions

```bash
# Uninstall a specific version
pyenv uninstall 3.9.0
```

## Setting Python Versions

pyenv lets you set Python versions at three different levels:

### 1. Global (System-wide)

Sets the default Python version for your entire user account:

```bash
# Set global Python version
pyenv global 3.11.7

# Verify
python --version  # Python 3.11.7
```

### 2. Local (Per-Project) - Most Common

Creates a `.python-version` file in your project directory:

```bash
# Navigate to your project
cd ~/Projects/my-project

# Set local Python version
pyenv local 3.11.7

# This creates a .python-version file
# Now this directory and subdirectories use Python 3.11.7
python --version  # Python 3.11.7
```

**How it works:** When you run Python commands in this directory, pyenv automatically uses the version specified in `.python-version`.

### 3. Shell (Current Session)

Sets the Python version for only the current terminal session:

```bash
# Set for current shell session
pyenv shell 3.10.13

# Verify
python --version  # Python 3.10.13

# Unset shell-specific version
pyenv shell --unset
```

## Version Priority

pyenv checks for Python versions in this order:

1. **Shell** - `PYENV_VERSION` environment variable (set by `pyenv shell`)
2. **Local** - `.python-version` file in current directory or parent directories
3. **Global** - `~/.pyenv/version` file (set by `pyenv global`)
4. **System** - System's default Python (if pyenv can't find a version)

## Common Workflows

### Starting a New Project

```bash
# 1. Install desired Python version (if not already installed)
pyenv install 3.11.7

# 2. Create project directory
mkdir my-project && cd my-project

# 3. Set local Python version
pyenv local 3.11.7

# 4. Verify
python --version  # Python 3.11.7

# 5. Now use Poetry or venv to create virtual environment
poetry init  # or python -m venv .venv
```

### Switching Between Projects

```bash
# Project A uses Python 3.10
cd ~/Projects/project-a
pyenv local 3.10.13
python --version  # Python 3.10.13

# Project B uses Python 3.11
cd ~/Projects/project-b
pyenv local 3.11.7
python --version  # Python 3.11.7
```

### Working with Multiple Python Versions

```bash
# Set multiple Python versions globally
pyenv global 3.11.7 3.10.13 3.9.18

# This makes all versions available
python3.11 --version  # Python 3.11.7
python3.10 --version  # Python 3.10.13
python3.9 --version   # Python 3.9.18

# The first one is the default
python --version      # Python 3.11.7
```

## Using pyenv with Poetry

pyenv and [[Poetry - The Project and Dependency Manager|poetry]] work great together:

1. **pyenv** sets which Python version to use
2. **Poetry** creates a virtual environment with that Python version

```bash
# Set Python version for project
pyenv local 3.11.7

# Initialize Poetry (uses Python 3.11.7)
poetry init
poetry install

# Poetry creates .venv with Python 3.11.7
poetry env info
```

## Essential Commands Reference

```bash
# Installation
pyenv install --list           # List available versions
pyenv install <version>        # Install a Python version
pyenv uninstall <version>      # Uninstall a Python version

# Viewing versions
pyenv versions                 # List installed versions
pyenv version                  # Show active version
pyenv which python             # Show path to active Python

# Setting versions
pyenv global <version>         # Set global version
pyenv local <version>          # Set local version (.python-version)
pyenv shell <version>          # Set shell session version
pyenv shell --unset            # Unset shell version

# Other commands
pyenv rehash                   # Rehash shims (run after installing packages)
pyenv commands                 # List all pyenv commands
```

## Understanding .python-version

The `.python-version` file is a simple text file created by `pyenv local`:

```
3.11.7
```

**Benefits:**
- ✅ Version controlled (commit to git)
- ✅ Team members automatically use the same Python version
- ✅ CI/CD systems can read it
- ✅ Works automatically when you `cd` into the directory

## Troubleshooting

### Python version not changing

```bash
# Check which version is active and why
pyenv version

# Check for .python-version files in parent directories
find . -name ".python-version"

# Rehash shims
pyenv rehash
```

### Command not found after installing package

```bash
# Rehash shims after installing packages with pip
pyenv rehash
```

### Poetry not using pyenv Python

```bash
# Check pyenv is active
pyenv version

# Remove existing Poetry environment
poetry env remove python

# Reinstall with current pyenv Python
poetry install
```

## pyenv vs Poetry vs venv

Understanding the differences:

| Tool | Purpose | What it Manages |
|------|---------|-----------------|
| **pyenv** | Python version manager | Multiple Python installations (3.9, 3.10, 3.11, etc.) |
| **Poetry** | Project dependency manager | Project dependencies and virtual environments |
| **venv** | Virtual environment creator | Isolated Python environments (built-in to Python) |

**Typical workflow:**
1. Use **pyenv** to install and select Python 3.11
2. Use **Poetry** (or venv) to create an isolated environment for your project
3. Install project dependencies into that environment

## Additional Resources

- [pyenv GitHub Repository](https://github.com/pyenv/pyenv)
- [pyenv Documentation](https://github.com/pyenv/pyenv#readme)
- [Common Build Problems](https://github.com/pyenv/pyenv/wiki/Common-build-problems)