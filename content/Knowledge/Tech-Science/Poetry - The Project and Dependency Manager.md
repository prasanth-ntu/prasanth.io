---
tags:
  - Python
  - Programming
  - softwareengineering
draft: false
---

# Poetry - The Project and Dependency Manager

**Source:** [Poetry Documentation](https://python-poetry.org/docs/)

## What is Poetry?

`Poetry` is a ==modern tool for managing Python projects==. It handles creating virtual environments, installing dependencies (like `pandas` or `requests`), and packaging projects for distribution. It's an alternative to using `pip`, `venv`, and `requirements.txt`.

- **Primary Goal:** Manage libraries and environments for a specific project in isolation
- **What it Manages:** Project dependencies and virtual environments using `pyproject.toml` and `poetry.lock`
- **Use Case:** Start a new project and run `poetry add requests` to install it into a dedicated virtual environment

## Installation

**Install Poetry:**

```bash
# macOS/Linux (recommended)
curl -sSL https://install.python-poetry.org | python3 -

# Or using pip
pip install poetry
```

**Make sure Poetry is in your PATH:**

```bash
export PATH="$HOME/.local/bin:$PATH"
```

**Verify installation:**

```bash
poetry --version
```

## Configuration

**Set virtual environment to be created in project directory** (recommended for better maintenance and traceability):

```bash
poetry config virtualenvs.in-project true
```

This creates a `.venv` folder in your project root instead of a centralized location.

## Getting Started with a New Project

1. **Initialize a new project:**

```bash
poetry init
```

This creates a `pyproject.toml` file interactively.

2. **Install dependencies:**

```bash
poetry install
```

This creates a virtual environment and installs all dependencies listed in `pyproject.toml`.

## Managing Dependencies

### Adding Dependencies

```bash
# Add a production dependency
poetry add requests

# Add a development dependency
poetry add --group dev pytest black

# Add with version constraint
poetry add "numpy>=1.20,<2.0"
```

### Removing Dependencies

```bash
poetry remove requests
```

### Updating Dependencies

```bash
# Update all dependencies
poetry update

# Update specific package
poetry update requests
```

## Working with Virtual Environments

### Environment Commands

```bash
# Show environment information
poetry env info

# List all environments for the project
poetry env list

# Remove an environment
poetry env remove python3.11
```

### Activating the Environment

> [!WARNING] **Poetry 2.0+ behavior:** `poetry env activate` shows you the activation command but doesn't activate it directly:

```bash
# Get the activation command
poetry env activate
# Output: source /path/to/project/.venv/bin/activate

# Then run the command it shows
source .venv/bin/activate
```

**Alternative: Use `poetry run`** (no activation needed):

```bash
poetry run python script.py
poetry run jupyter lab
poetry run pytest
```

This is often the preferred approach for running commands in the Poetry environment.

## Using Jupyter Notebooks with Poetry

### Option 1: Using VSCode/Cursor (Recommended)

1. Open a notebook
2. Click the kernel selector (top-right corner)
3. Select `.venv (Python 3.x.x)` from the list
4. The IDE automatically uses the Poetry environment with all dependencies

No additional setup needed!

### Option 2: Using Jupyter Lab in Browser

```bash
poetry run jupyter lab
```

This launches Jupyter with the Poetry virtual environment active.

**Optional:** Register a named kernel (only if running Jupyter Lab outside of `poetry run`):

```bash
poetry run python -m ipykernel install --user --name my-project --display-name "My Project"
```

## Manual Editing of `pyproject.toml`

If you manually edit `pyproject.toml`, follow this workflow:

### The Edit → Lock → Install Workflow

1. **Edit `pyproject.toml`** - Make your changes (add dependencies, change versions, etc.)

2. **Update the lock file:**

```bash
poetry lock
```

This resolves dependencies and updates `poetry.lock` with exact versions, but **doesn't install anything yet**.

3. **Install the changes:**

```bash
poetry install
```

This actually installs/updates/removes packages based on your changes.

### When to Use Manual Edits vs `poetry add`

- **Use `poetry add`**: For adding new packages (recommended)
- **Use manual edits**: For complex changes like:
  - Changing version constraints
  - Adding development dependencies
  - Modifying project metadata
  - Adding dependency groups

### Manual Edit Examples

```toml
# Add development dependencies
[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
black = "^23.0.0"
mypy = "^1.0.0"

# Add optional dependencies
[tool.poetry.group.docs.dependencies]
mkdocs = "^1.5.0"
sphinx = "^7.0.0"
```

**Remember:** Always follow the **edit → lock → install** workflow! 🔄

## Essential Commands Reference

```bash
# Project setup
poetry init                    # Create new pyproject.toml
poetry install                 # Install dependencies from lock file
poetry install --no-root       # Install dependencies without installing the project itself

# Dependencies
poetry add <package>           # Add a package
poetry add --group dev <pkg>   # Add dev dependency
poetry remove <package>        # Remove a package
poetry update                  # Update all dependencies
poetry show                    # List all installed packages
poetry show --tree             # Show dependency tree

# Environment
poetry env info                # Show environment info
poetry env list                # List environments
poetry env remove <name>       # Remove an environment
poetry env activate            # Show activation command
poetry run <command>           # Run command in virtual environment

# Lock file
poetry lock                    # Update lock file (no install)
poetry lock --check            # Check if lock file is up to date

# Build and publish
poetry build                   # Build source and wheel archives
poetry publish                 # Publish to PyPI
```

## Daily Workflow

### Starting a New Project

```bash
# 1. Set Python version (if using pyenv)
pyenv local 3.11

# 2. Initialize Poetry project
poetry init

# 3. Configure to use in-project venv
poetry config virtualenvs.in-project true

# 4. Install dependencies
poetry install

# 5. Add packages as needed
poetry add pandas numpy requests
```

### Working on an Existing Project

```bash
# 1. Clone the repository
git clone <repo-url>
cd <project>

# 2. Install dependencies
poetry install

# 3. Run your code
poetry run python main.py
# OR activate the environment
source .venv/bin/activate
python main.py
```

## Advantages of Poetry

### Over pip + requirements.txt

- ✅ Automatic virtual environment management
- ✅ Lock files ensure reproducibility
- ✅ Dependency resolution (handles conflicts automatically)
- ✅ Separates dev and production dependencies
- ✅ Single configuration file (`pyproject.toml`)

### Over Conda

- ✅ Faster dependency resolution
- ✅ Better integration with modern Python tooling
- ✅ No need for separate conda installation
- ✅ Simpler configuration

### Over Docker (for development)

- ✅ Faster startup time
- ✅ Direct access to local files
- ✅ Better IDE integration
- ✅ Easier debugging
- ✅ No container overhead

## Troubleshooting

### Jupyter Can't Find Packages

**In VSCode/Cursor:**
Make sure you selected the `.venv` kernel in the kernel selector.

**In Jupyter Lab:**
Always use `poetry run jupyter lab` to ensure the Poetry environment is active.

### Dependency Conflicts

```bash
# Try updating
poetry update

# Or check lock file status
poetry lock --check

# Force re-lock
poetry lock --no-update
```

### Environment Issues

```bash
# Remove and recreate environment
poetry env remove python
poetry install
```

## Additional Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [Managing Environments](https://python-poetry.org/docs/managing-environments/)
- [Dependency Specification](https://python-poetry.org/docs/dependency-specification/)