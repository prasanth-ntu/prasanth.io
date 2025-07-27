---
tags:
  - Python
  - Jupyter
  - Notebooks
  - GitHub
  - VersionControl
description: nbdime – diffing and merging of Jupyter Notebooks
---
Source: https://nbdime.readthedocs.io/en/latest/
# Web based GUI viewers of notebook diffs
```
nbdiff-web [<commit> [<commit>]] [<path>]
```
## Example: 
For this project, https://github.com/prasanth-ntu/DeepLearningAI-Practical-Multi-AI-Agents-and-Advanced, 

- For comparing the un-staged or staged local commit with remote:
```
nbdiff-web L6/L_6.ipynb 
```

- For comparing (diffing) the notebook between two different commits:
```
nbdiff-web 546e302bd7b527b8640c22f45512936239425612 0ac7e11cc81e8e8f0808ed8103e149a2d372a34b
```

![[nbdime - diffing notebooks - example.pdf]]
