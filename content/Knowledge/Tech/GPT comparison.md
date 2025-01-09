---
tags:
  - DataScience
  - ArtificialIntelligence
  - DeepLearningAI
  - LLM
  - GPU
---
# Estimating compute time naively

Given, NVIDIA A100 has a throughput of $312 \text{ TFLOPs}$ for FP16 precision,

| Year |   Model   |             Est. Compute†<br>(in [[FLOPS\|FLOP]]s & TFLOPs)             |                  Est. Compute Growth                  |                                                  Est. training duration with  $10000\times \text{ A100}$ GPUs                                                  | Est. Parameter Count | Est transformer layers |               Est. Parameter Growth               |
| :--: | :-------: | :---------------------------------------------------------------------: | :---------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------: | :--------------------: | :-----------------------------------------------: |
| 2018 | [[GPT-1]] |                                                                         |                                                       |                                                                                                                                                                |                      |                        |                                                   |
| 2019 | [[GPT-2]] |       $4e21 \text{ FLOP}\rightarrow 4 \times 10^9 \text{ TFLOPs}$       |                                                       |           $\large \frac{4 \times 10^9 \text{ TFLOP}}{10000 \times 312 \text{ TFLOPS}}$ <br>$= 12.8 \times 10^2 \text{ secs}$ $= 0.0147 \text{ days}$           |         1.5B         |                        |                                                   |
| 2020 | [[GPT-3]] |     $3e23 \text{ FLOP} \rightarrow 3 \times 10^{11} \text{ TFLOPs}$     |   <span style="color:green"><b>+ ~2 OOMs</b></span>   |          $\large \frac{3 \times 10^{11} \text{ TFLOP}}{10000 \times 312 \text{ TFLOPS}}$ <br>$= 9.61 \times 10^4 \text{ secs}$ $= 1.11 \text{ days}$           |         175B         |           96           | <span style="color:green"><b>+ ~2 OOMs</b></span> |
| 2023 | [[GPT-4]] | $\text{~}4e25 \text{ FLOP} \rightarrow 4 \times 10^{13} \text{ TFLOPs}$ | <span style="color:green"><b>+ ~1.5-2 OOMs</b></span> | $\large \frac{4 \times 10^{13} \text{ TFLOP}}{10000 \times 312 \text{ TFLOPS}}$ <br>$= 12.8 \times 10^6 \text{ secs}$ $= 148 \text{ days}$ $(\text{5 months})$ | ~1-2 trillion params |                        | <span style="color:green"><b>+ ~1 OOM</b></span>  |
- \*without factoring in memory bandwidth, latency, power efficiency, etc.
- †Sources: 
	- [Epoch AI](https://epochai.org/data/epochdb/table)

# Pre-training dataset and cost
| Year | Model     | Dataset (size)                                                      | Cost (in terms of cloud compute) |
| ---- | --------- | ------------------------------------------------------------------- | -------------------------------- |
| 2018 | [[GPT-1]] |                                                                     |                                  |
| 2019 | [[GPT-2]] |                                                                     |                                  |
| 2020 | [[GPT-3]] | 300 billion tokens†<br>(60% of original data of 499 billion tokens) | ~$4.6 million†                   |
| 2023 | [[GPT-4]] |                                                                     |                                  |
*Sources: 
- †[Build a Large Language Model from Scratch](https://www.amazon.sg/dp/1633437167?ref_=mr_direct_us_sg_sg&showmri)*