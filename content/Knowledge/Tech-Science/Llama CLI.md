---
tags:
  - LLM
  - machinelearning
  - artificialintelligence
  - GAI
  - OpenSource
---
> [!SUMMARY] The main goal of `llama.cpp` is to enable LLM inference with minimal setup and state-of-the-art performance on a wide range of hardware - locally and in the cloud.

# Sources
- https://pypi.org/project/llama-cli/
- https://github.com/ggml-org/llama.cpp

# Useful Commands
```bash
llama-cli ...

llama-server ...
```

# Examples
- [[How to Fine-tune LLMs with Unsloth - Complete Guide by Pookie#Running the models locally in Mac]]

## Default Location for `llama-cli`
- For most **llama-cli** installations via Homebrew, the downloaded models are stored in default storage path: `~/Library/Caches/llama.cpp`

```bash
# To display the contents
ls -l -h ~/Library/Caches/llama.cpp
-rw-r--r--@ 1 user  staff   1.9G Sep  6 17:38 prasanthntu_Llama-3.2-3B-ascii-cats-lora-q4_k_m-GGUF_unsloth.Q4_K_M.gguf
-rw-r--r--@ 1 user  staff   233B Sep  6 17:38 prasanthntu_Llama-3.2-3B-ascii-cats-lora-q4_k_m-GGUF_unsloth.Q4_K_M.gguf.json
```

