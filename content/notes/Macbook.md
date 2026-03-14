---
tags:
  - tool
aliases:
  - Knowledge/Tools/Macbook
---
# Homebrew
[Homebrew](https://brew.sh/) installs [the stuff you need](https://formulae.brew.sh/formula/ "List of Homebrew packages") that Apple (or your Linux system) didn’t.

# Useful libs
```bash
#  Gives you the exact Linux `watch` command.
brew install watch

# 
brew install grafana

# 
brew install prometheus

# CatBoost requires Ninja for building from source
brew install ninja

# Bun is an all-in-one toolkit for developing modern JavaScript/TypeScript applications.
brew install oven-sh/bun/bun

# Handle/Merge images
brew install imagemagick
```

# Other Libraries

```bash
# 

```
# Useful commands & Shortcuts

## Ports related
### Check all ports in use:

```bash
lsof -i -P -n | grep LISTEN
```

- `lsof`: Lists open files (including network connections)
- `-i`: Shows internet connections
- `-P`: Shows port numbers (not service names)
- `-n`: Shows IP addresses (not hostnames)
- `grep LISTEN`: Filters to show only listening ports

### Check a specific port:

```bash
lsof -i :PORT_NUMBER
```

For example, to check what's using port 8080:

```bash
lsof -i :8080
```

### Alternative using netstat:

```bash
netstat -anv | grep LISTEN
```

### More detailed view with process names:

```bash
sudo lsof -iTCP -sTCP:LISTEN -n -P
```

The output shows:

- **COMMAND**: The process name
- **PID**: Process ID
- **USER**: User running the process
- **NAME**: The port being used (e.g., `*:8080`)

## Show hidden files
To show hidden files on a Mac, press `Command + Shift + .` (the period key) in any Finder window to make hidden items visible as translucent files, then press the same shortcut again to hide them.[^1]


# Footnote 
[^1]: https://discussions.apple.com/thread/7581737?sortBy=rank
