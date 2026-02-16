---
tags:
  - ai
  - data-science
  - llm
  - machine-learning
  - open-source
aliases:
  - Knowledge/Tech-Science/Ollama
---
> [!SUMMARY] Chat & build with open LLMs

# Sources
- https://ollama.com/
- https://github.com/ollama/ollama/tree/main

# Useful Commands
```bash
# Importing GGUF models in model files
ollama create model-name -f Modelfile

# To run and chat with Gemma 3
ollama run gemma3

# To view the list of models available
ollama list
```


# Default Location for `ollama`
The downloaded models are stored in default storage path: `~/.ollama/model`

```bash
# To display the contents
ls -l -h ~/.ollama/model
total 0
drwxr-xr-x@ 17 user  staff   544B Sep  6 18:18 blobs
drwxr-xr-x@  3 user  staff    96B Sep  4 23:18 manifests

# To display the contents of the blobs (where model files are stored)
ls -l -h ~/.ollama/model
-rw-r--r--@ 1 user  staff   487B Sep  6 18:18 sha256-3f8cf9ff3845233047d261d75e08d263a0f0aac162332e7c0ee0ceea763c6118
-rw-r--r--@ 1 user  staff   4.6G Sep  6 18:18 sha256-61d75d8730d50b5846a4c4e00d52e0cfb2226ffcb24e1ffc27a01784fefc1de1
...

# To see the app and server logs
cat ~/.ollama/logs/app.log
cat ~/.ollama/logs/server.log



```





