- Source: [YouTube](https://www.youtube.com/watch?v=Lt7KrFMcCis), [LinkedIn](https://www.linkedin.com/posts/,danielhanchen_heres-a-complete-guide-to-fine-tuning-llms-activity-7351251048226836480-Qa-z/?utm_source=share&utm_medium=member_android&rcm=ACoAAAcOLFMBUn1o8NEoEvAqJrA0ZzVgH3csPQ0), GitHub, [Presentation (SVG)](Pookie-official-guide-to-finetuning-LLMs.svg)
- Speaker: Wout Voseen ([LinkedIn](https://www.linkedin.com/in/wout-vossen/))
- My forked/modified code: [GitHub](https://github.com/prasanth-ntu/pookie-llm-finetuning-resources)

---
# Presentation
## Introduction

> [!QUESTION] Why fine-tune LLMs?
- **Add new knowledge**
	- medical/ legal/ industrial/ company secrets
	- domain specific knowledge 
- **Improve performance**
	- story telling
	- document classification
	- information extraction
	- summarisation
	- ...
- Give AI assistants a personality
- **Improve the usability of local models**
- **Overcome guardrails**
	- political bias
	- potentially dangerous research

> [!Question] Why not just prompt?
- Sometimes hard/impossible to write an instruction/prompt
 - LLMs have limited context size & performance drops when context gets larger
 - Prompted behaviour might not meet performance requirements 

> [!Question] How about RAG?
- RAG is easier If we want to answer questions about knowledge base that changes frequently
- Quality of RAG is very dependent on retrieval process
> [!TIP] Most interesting combination: ==RAG + Finetuning==

## LLM Training
### Pre-training & Post-training

> [!QUESTION] How are LLM trained?

> [!HINT] It all starts with Transformers
> 

<p><a href="https://commons.wikimedia.org/wiki/File:Transformer,_full_architecture.png#/media/File:Transformer,_full_architecture.png"><img src="https://upload.wikimedia.org/wikipedia/commons/3/34/Transformer%2C_full_architecture.png" alt="Transformer, full architecture.png" height="720" width="684"></a><br>By dvgodoy - <a rel="nofollow" class="external free" href="https://github.com/dvgodoy/dl-visuals/?tab=readme-ov-file">https://github.com/dvgodoy/dl-visuals/?tab=readme-ov-file</a>, <a href="https://creativecommons.org/licenses/by/4.0" title="Creative Commons Attribution 4.0">CC BY 4.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=151216016">Link</a></p>

> [!INFO] 1) Pre-training
>**Phase**
> - Base model
> - *Variant*: Completions
> 
> **Dataset**
> - Standard data (Common Crawl, GitHub, Wikipedia, Books, ArXiv, Code Exchange, etc.)
> 
> **Purpose & Task**
> - Next-token prediction 
> - Gain language understanding
> - Gain background knowledge
>   
> **Resources**
> -  [Llama paper](https://arxiv.org/pdf/2302.13971) > Table 1: Pre-training data
> - [common crawl sample](https://huggingface.co/datasets/agentlans/common-crawl-sample) 


> [!INFO] 2.1) Post-Training
>**Phase**
> - Supervised Fine Tuning (SFT)
> - *Variants*: 1) Instruction, 2) Chat
>   
> **Dataset**
> - Structured data that demonstrates intended behaviour
>  
> **Purpose & Task**
> - Learn to follow instructions
> - Learn to answer questions about a domain
> - Learn to have conversations
> - Demonstrate intended behaviour
>   
> **Resources**
> -  [Llama 3 paper](https://arxiv.org/pdf/2407.21783) > Table 7: Statistics of SFT data
> - [alpaca dataset (instruction tuning)](https://huggingface.co/datasets/yahma/alpaca-cleaned)
> - [gaunaco (conversation tuning)](https://huggingface.co/datasets/philschmid/guanaco-sharegpt-style)
> - [paul graham dataset (conversation tuning)](https://huggingface.co/datasets/pookie3000/pg_chat)

> [!INFO] 2.2) Post-training
> **Phase**
> - Model Alignment (RL): DPO, PPO/RLHF, RLOO
>   
> **Dataset**
> - Dataset of rejected and preferred assistant responses
> 
> **Purpose & Task**
> - Make model better follow human preference
> - Make model safer
>   
> **Resources**
> - [descriptiveness-sentiment-trl instruction tuning](https://huggingface.co/datasets/trl-internal-testing/descriptiveness-sentiment-trl-style)
> - [llama3 paper](https://arxiv.org/pdf/2407.21783) > 4. Post-Training

> [!INFO] 2.3 Post-training
> **Phase**
> - Reasoning (RL): GRPO
> 
> **Dataset**
> - Dataset of prompts and expected answers
> 
> **Purpose & Tasks**
> - Create 'reasoning models' for inference time reasoning
> - For quantitative domains (science, math, coding, etc.)
>   
> **Resources**
> - [gsm8k (Grade school math)](https://huggingface.co/datasets/openai/gsm8k  )

---
### LoRA vs. QLoRA

> [!QUESTION] How do we actually train?

> [!TIP] Compute: Llama 3 405B is training on up to 16K H100 GPUs
> Each H100 GPU costs ~30K USD

> [!TIP] We can fine-tune LLMs efficiently using
> - LoRA
> - QLoRA

> [!INFO] **Low-rank Matrix Decomposition, LoRA & QLoRA**
> - Instead of finetuning the weights of the actual model, we fine-tune the low rank matrices (a.k.a. adapters which consists of low-rank matrices)
> 	- During the inference time, these adapters are put on top of the actual weights of the base model, and they are summed together. This way, we don't have to optimise the base model itself.
> - In the example below, we can see that instead of finetuning $5 \times 5$ matrix (25 weights), we just have to fine-tune $5 \times 1 + 1 \times 5$ matrices (10 weights
> 	![[low-rank-matrix-decomposition-example.png]]
> - QLoRA is where the base model is also quantised (e.g, weights reduced from 16-bit to 4-bit)
![[lora-vs-qlora-for-llm-fine-tuning.png]]
>   

For mode details, refer [QLORA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/pdf/2305.14314) paper.

### Which open-source models? Which variants?

> [!Question] Which models to fine-tune?
> - Google (Gemma)
> - Meta
> - Mistral AI
> - DeepSeel
> - Qwen
> - ...

> [!Question] How many parameter model?
> Depends on the RAM
> ![[llm-model-parameters-and-vram-needed-for-fine-tuning.png]]

> [!Question] Which model variants to choose?
> **Base model**
> - model after pretraining phase
> - so no instruction following, chat (supervised-finetuning)
> - requires finetuning for downstream usage
> 
> **instruct / chat variant**
> - supervised finetuning already done
> - capable of chat / instruction following
> 
> **multi-modal / vision variant**
>  - can take both image and text input
> 
> **gguf variant**
> -  for inference use only (not trainable)


> [!Question] When to use which variant?
> **base model:**
> - you don't need chat / instruction following capabilities (ex. ascii generation)
> - you have lots of data > 2000 samples 
> - you want to train with your own chat template
> 
> **instruct / chat variant:**
> - you want to leverage the supervised finetuning already done
> - you don't have a lot of data
> > [!WARNING] you need to format your training set according to the chat template that was used during original SFT
> 
> **multi-modal variant:**
> - 🤓
> 
> **gguf variant**
> - never when finetuning only when doing inference

### Model naming conventions explained

| Model Name                                                                                            | Parameters | Variant    | Modality                               |                                      |
| ----------------------------------------------------------------------------------------------------- | ---------- | ---------- | -------------------------------------- | ------------------------------------ |
| [google/gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it)                                   | 4b         | instruct   | multi-model <br>(support vision input) |                                      |
| [google/gemma-3-1b-pt](https://huggingface.co/google/gemma-3-1b-pt)                                   | 1b         | pretrained | text-only                              |                                      |
| [unsloth/gemma-3-12b-it-GGUF](https://huggingface.co/unsloth/gemma-3-12b-it-GGUF)                     | 12b        | instruct   | multi-model <br>(support vision input) | GGUF                                 |
| [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)         | 70b        | instruct   | text-only                              |                                      |
| [unsloth/Llama-3.1-8B-unsloth-bnb-4bit](https://huggingface.co/unsloth/Llama-3.1-8B-unsloth-bnb-4bit) | 8b         | pretrained | text only                              | 4 bit quantized using Bits and Bytes |

---
### Collecting and Structuring Data

> [!Question] How to collect and structure data?
> ==*Depends on the task*==
> 
> **Pre-training: Continued**
> - Collect some unstructured training data
> 	- e.g., [paul graham essays](https://huggingface.co/datasets/pookie3000/pg_essays_split_1000_t)
> 	- ![[paul-graham-essays-for-continued-pre-training-example.png]]
>   
> **Post-training: Chat / conversation models using SFT**
> - Curate conversational data in a pre-defined template (each conversation consists of 1 pair of `role` and `content`)
> 	- e.g., [dataset-preparation](https://github.com/vossenwout/llm-finetuning-resources/tree/main/dataset-preparation), [pg_chat](https://huggingface.co/datasets/pookie3000/pg_chat)
> 	  ![[pg-chat-for-conversation-data-for-fine-tuning-example.png]]
> - Apply chat template to the above formatted data with special tokens (e.g., `eot_id`)
> 	- e.g., llama 3.1, [How to format inputs to ChatGPT models](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models)
> 	  ![[special-tokens-during-finetuning-example.png]]
> - **Prompt Templates**: Models will have different chat templates which were used during SFT of the specific model
> 	- e.g., [Mistral (in GO templating language)](https://github.com/unslothai/unsloth/blob/main/unsloth/chat_templates.py#L165)
>  	  
> **Post-training: Model Alignment using DPO/ PPO/ RLHF**
> - Curate dataset that shows chosen and rejected answer for given prompt
> 	  - e.g., [trl-internal-testing/descriptiveness-sentiment-trl-style](v)
> 	    ![[model-alignment-example-llm-fine-tuning-example.png]]
> 
> **Post-training: Reasoning models using GRPO**
> - Curate datasets with question and answers
> 	- e.g., [Goastro/mlx-grpo-dataset](https://huggingface.co/datasets/Goastro/mlx-grpo-dataset)
> 	  ![[reasoning-model-llm-finetuning-example.png]]
 	    
---
> [!Question] How to fine-tune?
> - **Libraries**: unsloth and PEFT
> - **Compute**: 
> 	- Paid platforms: GCP, AWS, etc.
> 	- Free platforms: [Google Colab](https://colab.research.google.com/), [Modal](https://modal.com/), AWS SageMaker, etc.

### How to save model?
 - Using GGUF format, a most popular one that contains both the tokenizer as well as the model. In other words, it contains everything that our system needs to run the model.
 - Also, allows the model to run on CPU (e.g., Macbooks)
![[saving-fine-tuned-llm-mode-explained.png]]
- **Model merging or LoRA on top**: We have two options when we save our model in GGUF
	1. Convert base model and adapters to GGUF separately, and during inference, put them on top. ==This allows us to swap different adapters at inference time==.
	2. Merge the base model with adapters by adding the weights together, and turn the merged model into GGUF. ==Makes it easier to share our specific model with others==
- **Quantize GGUF such that it fits in our VRAM**
	- e.g., [tools/quantize/quantize.cpp](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/quantize.cpp#L22)
		- Recommended to use `{ "Q4_K_M",   LLAMA_FTYPE_MOSTLY_Q4_K_M,   " 4.58G, +0.1754 ppl @ Llama-3-8B",  },` where
			- Q4 implies 4-bit quantization
- **Quantization and turning into GGUF is done with**
	- [llama.cpp](https://github.com/ggml-org/llama.cpp)
		- Unsloth - Has compatibility for this 
		- [gguf-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) - Hugging face space to convert HF repo into GGUF 
- **Inference of GGUF**
	- [llama.cpp](https://github.com/ggml-org/llama.cpp) - Library where all other inference providers are built on
	- ollama - Much user friendly
	- [open-webui](https://github.com/open-webui/open-webui)
---
# Hands-on
## 1. Ascii Art -  Completion fine-tuning

The notebook ([GitHub](https://github.com/prasanth-ntu/pookie-llm-finetuning-resources/tree/main/finetuning/unsloth)) walks through the steps of using the Unsloth library for parameter-efficient finetuning (specifically using LoRA) of a large language model (LLM) on a custom dataset. The goal is to train the model to generate ASCII art.

> [!SUMMARY] Key contents of the notebook
> 1. **Installation of Libraries**
> 2. **Loading the Base Model**
> 	- `meta-llama/Llama-3.2-3B`
> 3. **Adding LoRA Adapter and Patching with Unsloth**
> 4. **Dataset Preparation & Visualization**
> 	- [`pookie3000/ascii-cats`](https://huggingface.co/datasets/pookie3000/ascii-cats)
> 5. **Training the Model**
>    > [!TIP] Interesting stats
>    > - `Num examples = 201 | Num Epochs = 5 | Total steps = 130`
>    >  - `Batch size per device = 2 | Gradient accumulation steps = 4`
>    >   - `Data Parallel GPUs = 1 | Total batch size (2 x 4 x 1) = 8`
>    > - `Trainable parameters = 24,313,856 of 3,237,063,680 (0.75% trained)`
> 6. **Inference**
> 7. **Saving the Model**
> 	1. **Converting base model in GGUF format**
> 		1. Using standalone python code locally and `modal` in cloud : [gguf-conversion/gguf_base_model.py](https://github.com/prasanth-ntu/pookie-llm-finetuning-resources/blob/main/gguf-conversion/gguf_base_model.py)
> 			- [prasanthntu/Llama-3.2-3B-guide-GGUF](https://huggingface.co/prasanthntu/Llama-3.2-3B-guide-GGUF)
> 	2. **Saving LoRA adapter (in PeFT LoRA & GGUF)**
> 		1. From google colab directly
> 			- [`prasanthntu/Llama-3.2-3B-ascii-cats-lora`](https://huggingface.co/prasanthntu/Llama-3.2-3B-ascii-cats-lora)
> 		2. Using HF Spaces GUI ([ggml-org/gguf-my-lora](https://huggingface.co/spaces/ggml-org/gguf-my-lora))
> 			- [`prasanthntu/Llama-3.2-3B-ascii-cats-lora-F32-GGUF`](https://huggingface.co/prasanthntu/Llama-3.2-3B-ascii-cats-lora-F32-GGUF)
> 				- Note: Use `F32` for *Quantization Method* during conversion as Precision of weights is normally stored in `F32`
> 	3. **Merge model with LoRA weights and save to GGUF**
> 		1.  From google colab directly
> 			- [`prasanthntu/Llama-3.2-3B-ascii-cats-lora-q4_k_m-GGUF`](https://huggingface.co/prasanthntu/Llama-3.2-3B-ascii-cats-lora-q4_k_m-GGUF)
> 8. **Loading Saved Model (for continued finetuning or inference)**
> 	1. From google colab directly
> 	2. Using jupyter notebook code locally
> 		- Clone GGUF variants of the [base model](https://huggingface.co/prasanthntu/Llama-3.2-3B-guide-GGUF) and [LoRA adapter]( https://huggingface.co/prasanthntu/Llma-3.2-3B-ascii-cats-lora-F32-GGUF) dynamically , and run it using [inference/llama_cpp_inference_completion_adapter.ipynb](https://github.com/prasanth-ntu/pookie-llm-finetuning-resources/blob/main/inference/llama_cpp_inference_completion_adapter.ipynb)

Sample output generated during inference: ![[peft-fine-tuning-using-unsloth-for-ascii-generation.png]]

---
## 2. Paul Graham - Conversation model fine-tuning

---
# Appendix
## Environment
Exporting the Google Colab Environment
```python
import subprocess

# Generate requirements.txt
try:
    with open('requirements.txt', 'w') as f:
        subprocess.run(['pip', 'freeze'], stdout=f, check=True)
    print("✅ requirements.txt generated successfully.")
except Exception as e:
    print(f"❌ Error generating requirements.txt: {e}")
```


---
# To clarify
- [ ] ...