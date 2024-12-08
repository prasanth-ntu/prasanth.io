---
tags:
  - DataScience
  - GPU
---
```dataviewjs 
dv.view('toc')
```

> Note: FLOPs and FLOPS are different, though there are some overlaps

# FLOP vs. FLOPS
## FLOP (Floating Point Operation)
- Refers to **single operation** involving floating-point arithmetic.
	- These are calculations involving real numbers (decimals), which are more complex than integer operations.
	- Used in tasks like simulations, rendering, and machine learning, where precision is crucial.
- **Unit of Measurement**: FLOP is a count or measure of how many floating-point calculations are needed for a task or algorithm.
	- Example: A matrix multiplication of $1000 \times 1000$ matrices may require millions of FLOPs.
- Examples of floating-point operations include:
	- Addition: $1.23 + 4.56$
	- Multiplication: $2.34 \times 5.67$
	- Division: $8.90/3.45$
## FLOPS (Floating Point Operations Per Second)
- Refers to the **rate** at which the floating-point operations are performed, measuring computational performance
	- $\text{FLOPs} = \text{(Number of Cores)} \times \text{(Clock Speed)} \times \text{(Instructions per Cycle per Core)}$
- **Unit of Measurement**: FLOPS (or variations like GFLOPS, TFLOPS, PFLOPS) is used to indicate the speed or throughput of a processor.
	- $1 \text{ GigaFLOPS (GFLOPS)}$ = Billion ($10^9$) FLOPs per second.
	- $1 \text{ TeraFLOPS(TFLOPS)}$ = Trillion ($10^{12}$) FLOPs per second.
	- $1 \text{ PetaFLOPS(PFLOPS)}$ = Quadrillion ($10^{15}$) FLOPs per second.
- **Example usage**:
	- A GPU capable of 10 TFLOPS can perform $10\times10^{15}$ floating-point operations per second.
- **Importance in GPUs**:
	- GPUs are optimized for parallel processing, making them capable of achieving extremely high FLOPS compared to CPUs.
	- For instance, a modern GPU like NVIDIA’s A100 has FP32 performance around 19.5 TFLOPS, meaning it can perform ~19.5 trillion 32-bit floating-point calculations per second.
- **Practical Applications**:
- 
## FLOP vs. FLOPS: Key Difference:

| **Aspect**          | **FLOP**                                         | **FLOPS**                                       |
| ------------------- | ------------------------------------------------ | ----------------------------------------------- |
| **Meaning**         | A single floating-point operation.               | Floating-point operations completed per second. |
| **Purpose**         | Describes workload size or algorithm complexity. | Measures processing power or performance.       |
| **Example Context** | “This algorithm requires $10^6 \text{ FLOPs}$.”  | “This GPU delivers $5 \text{ TFLOPS}$.”         |
### Analogy:
==Think of **FLOP** as a single task (like hammering one nail) and **FLOPS** as the rate at which you can hammer nails per second. A project task may require many hammering actions (FLOPs), and the speed of completing the project task depends on how fast you can hammer (FLOPS).==

---
# FLOP in detail

**FLOP** stands for **Floating Point Operation**, which is a fundamental arithmetic operation involving floating-point numbers (e.g., addition, subtraction, multiplication, division). In the context of GPUs and other computing devices, **FLOPs** (plural) often refer to the number of such operations a system can perform per second and are used as a measure of computational performance.

## Key Points About FLOP in GPUs

1. **Floating-Point Precision:**
	- GPUs can perform operations at different precision levels, which affects their FLOP throughput:
		- **FP32 (Single Precision)**: Commonly used in many ML/DL tasks and general computing.
		- **FP64 (Double Precision)**: Required for high-precision scientific computations.
		- **FP16 (Half Precision)**: Used in ML/DL for faster computations with reduced precision.
		- **BF16/INT8**: Used for specific tasks like deep learning inference for further speedup.
2. **Measuring FLOP**:
	- **FLOPs (Floating Point Operations per Second)** measure the computational power of a GPU:
		- $\text{FLOPs} = \text{(Number of Cores)} \times \text{(Clock Speed)} \times \text{(Instructions per Cycle per Core)}$
	- For instance, a GPU rated at **5 TFLOPs** can perform 5 trillion floating-point operations per second.
3. **Relevance of FLOP in GPUs**:
	- GPUs are optimized for high FLOP throughput because many tasks in graphics rendering, machine learning, and scientific simulations require massive numbers of floating-point operations. 
	- In deep learning, FLOPs are a common benchmark for measuring the compute intensity of a model (e.g., number of FLOPs required to process one forward pass of a neural network).
4. **Theoretical vs. Practical FLOPs**:
	- **Theoretical Peak FLOPs**: Maximum achievable performance under ideal conditions.
	- **Practical FLOPs**: Actual performance achieved in real-world workloads, often lower due to inefficiencies like memory bottlenecks, control flow divergence, or under-utilised cores.
---
## Example of FLOP Throughput in GPUs
- **NVIDIA A100**:
	- FP64: 19.5 TFLOPs
	- FP32: 156 TFLOPs (Tensor Cores)
	- FP16: 312 TFLOPs (Tensor Cores)

This highlights how GPUs are optimized for specific workloads, with ML tasks benefiting from lower-precision formats like FP16 for higher throughput.

## Examples of FLOPS in Action
1. **1 FLOP**:
	- **2.1 + 3.2** → A single floating-point addition.
	- **4.5 × 6.7** → A single floating-point multiplication.
2.	**Multiple FLOPS**:
	- **(2.1 + 3.2) × 4.5** → Consists of two FLOPS:
	- **1 FLOP** for addition: 2.1 + 3.2.
	- **1 FLOP** for multiplication: Result × 4.5.
3. **Matrix Multiplication Example**:
	- Consider multiplying two matrices, $A$ and $B$ to get $C$
		- $A$: $n \times m$ matrix (say, $500 \times 1000$)
		- $B$: $m \times p$ matrix (say, $1000 \times 400$)
		- $C$ = $A \times B$, will be $n \times p$ matrix ($500 \times 400$)
	- Each element in $C$ is computed by performing a dot ($.$) product of a row from $A$ and column from $B$, and each of that dot product involves
		- $m$ ($1000$) multiplications (one for each element of the row and column)
		- $m-1$ additions to sum these products together
		- The above $m$ multiplications and $m-1$ additions  can be approximated as $2m$ ($2\times1000$) operations.
	- Since there are $n \times p$ elements in C, then, there will be a total of $2 \times m \times n \times p$ ($2 \times 1000 \times 500 \times 400$ = $400,000,000$ = $400\times10^6$) operations = 400 **million FLOPs**.
4.	**Complex Operations**:
	- Operations like matrix multiplications or solving differential equations can require millions or billions of FLOPS depending on their size and complexity.

In summary, every basic floating-point arithmetic operation constitutes one FLOP, making this a fundamental measure for evaluating computational workloads. 
## FLOP vs Other Metrics
While FLOPs provide a useful measure of raw computational power, they should be considered alongside:
	•	**Memory bandwidth** (important for data-intensive tasks).
	•	**Latency** (critical for real-time applications).
	•	**Power efficiency** (relevant for deployment and scaling).

For optimal performance, balance between FLOPs and these factors is key!