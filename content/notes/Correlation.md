---
tags:
  - data-science
  - statistics
aliases:
  - Knowledge/Tech-Science/Correlation
---
Interpreting **correlation** helps us understand the strength and direction of a relationship between two variables. 

---
### **📌** **What is Correlation?**

Correlation measures how two variables move in relation to each other. It’s usually quantified using **Pearson’s correlation coefficient (r)**, which ranges from **-1 to +1**.

---

### **🔢**  **Correlation Values and Their Meaning**

| **Correlation Coefficient (r)** | **Strength**          | **Direction** |
| ------------------------------- | --------------------- | ------------- |
| **+1.0**                        | Perfect correlation   | Positive      |
| **+0.90 to +0.99**              | Very strong           | Positive      |
| **+0.70 to +0.89**              | Strong                | Positive      |
| **+0.40 to +0.69**              | Moderate              | Positive      |
| **+0.10 to +0.39**              | Weak                  | Positive      |
| **0.00 to +0.09**               | Negligible            | Positive      |
| **0.00**                        | None (No correlation) | —             |
| **–0.01 to –0.09**              | Negligible            | Negative      |
| **–0.10 to –0.39**              | Weak                  | Negative      |
| **–0.40 to –0.69**              | Moderate              | Negative      |
| **–0.70 to –0.89**              | Strong                | Negative      |
| **-0.90 to -0.99**              | Very strong           | Negative      |
| **-1.0**                        | Perfect correlation   | Negative      |

### **📈**  **Types of Correlation**

- **Positive**: As one variable increases, so does the other.    
    _E.g., Hours studied and exam scores._
- **Negative**: As one variable increases, the other decreases.
    _E.g., Stress level and sleep quality._
- **Zero**: No linear relationship between variables.
    _E.g., Shoe size and IQ._
---
### **⚠️** **Important Caveats**

1. **Correlation ≠ Causation**: Just because two things move together doesn't mean one causes the other. This can happen for several reasons:
	- **[[Glossary#Confounding Variable|Confounding variable]]**: A hidden third factor drives both variables. E.g., ice cream sales and drowning deaths both rise in summer — not because ice cream causes drowning, but because *temperature* increases both.
	- **Reverse causation**: The causal direction is backwards from what you assumed. E.g., hospital patients who receive more treatment have worse outcomes — not because treatment causes harm, but because sicker patients receive more treatment.
	- **Spurious correlation**: Two variables trend together by pure coincidence. E.g., per-capita cheese consumption correlates with deaths by bedsheet tangling — there is no causal or confounding link, just noise in large datasets.
2. **Outliers** can distort correlation values.
3. **Non-linear relationships** won’t be captured well by Pearson’s r.
4. **Spearman’s rank correlation** is used for non-linear but monotonic relationships.
---

### **✅**  **How to Use It in Practice**

- Look at both the **correlation coefficient** and the **scatterplot**.
- Always think about **possible confounding factors**.
- Use **domain knowledge** to interpret whether a correlation is meaningful.

  

