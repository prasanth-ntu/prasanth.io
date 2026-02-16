---
tags:
  - python
  - software-engineering
aliases:
  - Knowledge/Tech-Science/uv - Python Package and Project Manager
---
> [!Example] Resources
> - [Official uv Documentation](https://docs.astral.sh/uv/)

## Capability Comparison: uv vs Poetry

| Capability | uv | Poetry |
|----------|----|--------|
| Dependency resolution | ✅ | ✅ |
| Dependency installation | ✅ (very fast) | ✅ |
| Lockfile | ✅ (`uv.lock`) | ✅ (`poetry.lock`) |
| Virtual environment management | ✅ | ✅ |
| Uses `pyproject.toml` | ✅ | ✅ |
| Project scaffolding | ✅ | ✅ |
| CLI tool installation | ✅ (`uv tool`, `uvx`) | ✅ |
| Package building | ❌ | ✅ |
| Package publishing (PyPI / private registry) | ❌ | ✅ |
| Opinionated all-in-one workflow | ❌ | ✅ |
| Speed (resolver + installer) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

> [!NOTE]
> - **uv** focuses on ultra-fast dependency and environment management and intentionally does *not* handle package publishing.  
> - **Poetry** is an all-in-one project tool that also supports building and publishing Python packages to PyPI or private registries.

## Recommended Default Stack (uv-first)

A practical, modern default stack for most Python projects (apps, APIs, data/LLM work):

- **uv** — dependency + venv management (fast installs, lockfile)
- **ruff** — formatting + linting (fast; replaces black/isort/flake8 in many setups)
- **pytest** — testing
- **mypy** — optional static typing (especially useful as projects grow)
- **pre-commit** — run ruff/pytest (and others) automatically on commits

### Quick start (commands)

Install core dev tools (as project deps):
```bash
uv add --dev ruff pytest
```

Optional typing + pre-commit:
```bash
uv add --dev mypy pre-commit
```

Install ruff as a global CLI tool (optional alternative to project dev dep):
```bash
uv tool install ruff
```

Set up pre-commit (if you added it):
```bash
pre-commit install
```

### Notes

- For libraries you plan to publish, add **build** + **twine** (or use Poetry) for packaging/publishing.
- If you use Jupyter heavily, consider `uv add --dev ipykernel` and/or `jupyterlab`.

# Useful Commands
## Creating a Project

For more details, visit [Working on Projects](https://docs.astral.sh/uv/guides/projects/#uvlock)

Create a new Python project
```bash
$ uv init new-ap
```

Alternatively, you can initialize a project in the working directory:
```bash
$ uv init
```

uv will create the following files:
```bash
├── .gitignore
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

Run the main file/script
```bash
$ uv run main.py
```

## Managing Dependencies
Add dependencies
```bash
$ uv add requests
```

Remove a package
```bash
$ uv remove requests
```

Visualise dependencies
```bash
$ uv tree
```
## Running Commands
Manually update the environment
```bash
$ uv sync
```

## Tools
> [!SUMMARY] Tools are Python packages that provide command-line interfaces.

For more details, visit [Tools](https://docs.astral.sh/uv/concepts/tools/)

Install a tool
```bash
$ uv tool install ruff
```

Check the specific tool
```bash
$ which ruff
```

Check the list of tools installed
```bash
$ uv tool list
```

Use the tool
```bash
$ ruff format
$ ruff check
```

Use the tool without installation
```bash
$ uvx ruff format
$ uvx ruff check
```