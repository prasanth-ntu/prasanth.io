---
tags:
  - Python
  - Programming
  - Coding
  - Documentation
---
# Examples
```python
from IPython.display import HTML, Markdown, display
```

```python
# start a new terminal
import os
from IPython.display import IFrame

IFrame(f"{os.environ.get('DLAI_LOCAL_URL').format(port=8888)}terminals/1", 
       width=600, height=768)
```