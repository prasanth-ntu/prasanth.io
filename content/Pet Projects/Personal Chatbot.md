---
tags:
  - softwareengineering
  - Projects
  - Hacks
  - OpenSource
  - Chatbot
  - GAI
  - LLM
  - Agents
---
🤖 Personal Chatbot connected to my Personal Blog.

**Useful links**
- [Source code](https://github.com/prasanth-ntu/personal-chatbot)


```mermaid
graph TD
    subgraph "Data Processing Pipeline"
        A[GitHub Repository] -->|Clone| B[Local Storage]
        B -->|Parse| C[Markdown Parser]
        C -->|Chunk| D[Document Chunker]
        D -->|Generate| E[Embeddings]
    end

    subgraph "Vectors"
        E -->|Store| F[Pinecone/FAISS]
        F -->|Query| G[Search Engine]
    end

    subgraph "RAG System"
        H[User Query] -->|Process| I[Query Processor]
        I -->|Search| G
        G -->|Retrieve| J[Relevant Documents]
        J -->|Format| K[Context Builder]
        K -->|Send| L[LLM]
        L -->|Generate| M[Response]
        M -->|Extract| N[Citations]
    end

    subgraph "UI Layer"
        O[Streamlit UI] -->|Send| H
        M -->|Display| O
        N -->|Show| O
    end

    subgraph "Monitoring & Debugging"
        P[Tracing Tool] -->|Monitor| I
        P -->|Monitor| L
        Q[Vector Visualizer] -->|Debug| F
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style O fill:#bbf,stroke:#333,stroke-width:2px
    style P fill:#dfd,stroke:#333,stroke-width:2px
    style Q fill:#dfd,stroke:#333,stroke-width:2px

```