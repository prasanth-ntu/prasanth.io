# `.zshrc` vs  `.zprofile`
Here's the key differences between `.zshrc` and `.zprofile` in Zsh:
## `.zshrc` (Zsh Run Commands)
- **When it loads**: Every time you start an **interactive** shell session
- **Purpose**: Configuration for interactive shell sessions
- **Use cases**:
  - Aliases and functions
  - Prompt customization
  - Key bindings
  - Interactive features (like Oh My Zsh, syntax highlighting, autosuggestions)
  - Environment variables needed for interactive work
## `.zprofile` (Zsh Profile)
- **When it loads**: Only when you **log in** (login shells)
- **Purpose**: Login-time configuration
- **Use cases**:
  - Setting up environment variables that should be available system-wide
  - PATH modifications
  - One-time setup tasks
  - Variables that need to be available to GUI applications
## Key Differences

| Aspect | `.zshrc` | `.zprofile` |
|--------|----------|-------------|
| **Frequency** | Every interactive shell | Only at login |
| **Scope** | Interactive sessions | System-wide environment |
| **GUI Apps** | Not inherited | Inherited by GUI apps |
| **Performance** | Loads frequently | Loads once per login |
## Practical Example
Looking at your current `.zshrc`, you have:
```bash
# These should probably be in .zprofile instead:
export ANTHROPIC_AUTH_TOKEN=...
export ANTHROPIC_BEDROCK_BASE_URL=...
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
export CLAUDE_CODE_USE_BEDROCK=1
```
These environment variables would be better in `.zprofile` because:
1. They're needed system-wide (for GUI apps, other terminals)
2. They don't change often
3. They don't need to be reloaded every time you open a new terminal
## Recommendation
You might want to move those Claude-related environment variables to `.zprofile` and keep interactive features (Oh My Zsh, syntax highlighting, etc.) in `.zshrc`.