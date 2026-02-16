# Key components
- [[Glossary#Video RAM (VRAM)|VRAM]]
- [[Glossary#Random Access Memory (RAM)|RAM]]

# RAM vs. VRAM 

|Feature|RAM (System Memory)|VRAM (GPU Memory)|
|---|---|---|
|Location|Motherboard, accessed by CPU|On the GPU card|
|Speed and bandwidth|Slower, lower bandwidth|Much faster, high bandwidth|
|Primary use in LLMs|Loading model data, OS and CPU tasks|Storing model weights, gradients, KV cache|
|Critical for|Model loading, data pipelines, background tasks|Model training and inference performance|
|Size consideration|Should be at least as large as model size|Must be sufficient to fit model + context|
> [!TIP] Without enough VRAM, large models cannot be run effectively, while insufficient RAM can bottleneck loading and system stability[](https://dev.to/mitchell_cheng/my-learning-notes-choosing-the-right-ai-model-and-hardware-237)[](https://www.sabrepc.com/blog/Deep-Learning-and-AI/machine-learning-memory-requirements)[](https://www.reddit.com/r/StableDiffusion/comments/15meq08/does_ram_help_at_all_or_is_vram_the_most/). Both memories are essential, but VRAM is the key limiting factor for large model training and inference.