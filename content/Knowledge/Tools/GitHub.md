---
tags:
  - softwareengineering
  - Programming
  - Coding
---
# Examples
## Git pull from remote master into a local custom branch

```bash
# check the remote branches and fetch the latest changes
git remote -v && git fetch origin

# Check what branches are available
git branch -a

# Stash current changes to preserve work in progress
git stash push -m "WIP: Stashing changes before syncing with master"

# Pull latest changes from remote master branch
git checkout master
# Our local master is [X] commits behind the remote. Let's pull the latest changes:
git pull origin master

# Merge or rebase master changes into current branch
git checkout <custom-branch>
```

Now let's merge the master changes into our current branch. You have two options:
1. Merge (creates a merge commit) - preserves the branch history
2. Rebase (replays your commits on top of master) - creates a linear history

```bash
# Let me merge master into your branch (this is generally safer and preserves history):
git merge master

# Let me check if there might be any potential conflicts first by looking at what files have changed:
git log --oneline <custom-branch> ^master

# It looks like your feature branch doesn't have any commits that aren't in master, which means it was created from an older version of master. Let me check the current status and try a different approach:
git status
# Perfect! Now I can see the branch is clean except for untracked files. Let's merge master into your branch:

git merge master
```

```bash
# Restore stashed changes and resolve any conflicts
git stash pop

# We have merge conflicts in two files! This is expected since both your stashed changes and the master branch have modifications to the same files. Let me check the conflicts and help you resolve them:
git add <file_1> <file_2> ... <file_N>

git status
```

## Summary of Git Commands for Viewing Files in Commits:
To view the files generated or modified in a specific git commit locally, you can use several git commands. Here are the most useful ones:

Here are the most useful commands to view files in a specific git commit:
### **Basic Commands:**
1. **`git show --name-only <commit-hash>`** - Lists only the file names that were changed
2. **`git show --name-status <commit-hash>`** - Shows file names with status (M=Modified, A=Added, D=Deleted)
3. **`git show --stat <commit-hash>`** - Shows file names with change statistics (lines added/removed)
4. **`git show <commit-hash>`** - Shows the full diff with all changes

### **Alternative Commands:**
5. **`git diff --name-only <commit-hash>~1 <commit-hash>`** - Compare with previous commit
6. **`git log --name-only -1 <commit-hash>`** - Show commit info with file names
7. **`git diff-tree --no-commit-id --name-only -r <commit-hash>`** - List files in commit

### **For Multiple Commits:**
8. **`git log --name-only --oneline <commit-range>`** - Show files across multiple commits
9. **`git log --stat <commit-range>`** - Show statistics across multiple commits

### **Examples:**
```bash
# View files in the latest commit
git show --name-only HEAD

# View files in a specific commit
git show --name-only 22105542

# View files with changes between two commits
git diff --name-only commit1..commit2

# View files in the last 3 commits
git log --name-only --oneline -3
```

The most commonly used commands are `--name-only` for a simple list, `--name-status` to see what type of changes were made, and `--stat` to see the scope of changes.