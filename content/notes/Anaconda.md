---
tags:
  - data-science
  - machine-learning
  - software-engineering
  - tool
aliases:
  - Knowledge/Tools/Anaconda
---
https://www.anaconda.com/

# Anaconda or Miniconda
Refer [here](https://www.anaconda.com/docs/getting-started/getting-started#should-i-use-anaconda-distribution-or-miniconda%3F) to compare and decide which variant to install.

# Useful commands
Refer to [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) for useful commands.

```bash
# Get list of environments
conda env list

# Creating an Environment with Specific Python Version and/or Packages:
conda create -n myenv python=3.9 numpy pandas

# Activating the environment
conda activate myenv

# Deactivating the environment
conda deactivate
```


```bash
# To disable auto activation of conda at terminal start
conda config --set auto_activate_base false
```