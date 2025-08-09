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
git checkout custom-branch
```

Now let's merge the master changes into our current branch. You have two options:
1. Merge (creates a merge commit) - preserves the branch history
2. Rebase (replays your commits on top of master) - creates a linear history

```bash
# Let me merge master into your branch (this is generally safer and preserves history):
git merge master

# Let me check if there might be any potential conflicts first by looking at what files have changed:
git log --oneline custom-branch ^master

# It looks like your feature branch doesn't have any commits that aren't in master, which means it was created from an older version of master. Let me check the current status and try a different approach:
git status
# Perfect! Now I can see the branch is clean except for untracked files. Let's merge master into your branch:

git merge master
```

```bash
# Restore stashed changes and resolve any conflicts
git stash pop

# We have merge conflicts in two files! This is expected since both your stashed changes and the master branch have modifications to the same files. Let me check the conflicts and help you resolve them:
git add file_1 file_2 ... file_N

git status
```