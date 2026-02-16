---
tags:
  - python
  - software-engineering
  - tool
aliases:
  - Knowledge/Tech-Science/chromadb
---
ChromaDB is an open-source vector database used for storing and querying embeddings (e.g., for LLM apps). It’s commonly used with tools like LangChain,  LlamaIndex, and other LLM applications/services.

# Running ChromaDB locally
```python
import chromadb
client = chromadb.Client()

# Or for persistent storage:
client = chromadb.PersistentClient(path="my_chroma_db")
```
This runs the ChromaDB entirely **in-process** - there's no server process running separately, unless we are building an API layer around it.

# Storage modes
- **Ephemeral (in-memory):** Fast, but data is lost on restart.
- **Persistent:** Stores to disk (via DuckDB under the hood) if you specify a path.

# Examples
[[Google-5-Day-Gen-AI-Intensive-Course#**Summary of the key points & callouts**]]