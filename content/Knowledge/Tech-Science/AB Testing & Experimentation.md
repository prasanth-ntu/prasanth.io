---
tags:
  - Math
  - Statistics
  - datascience
  - DataAnalytics
---
In A/B testing and statistical analysis, the**Minimum Detectable Effect (MDE)** and the **p-value** are ==distinct but related concepts used to determine if a change is meaningful and statistically significant==. 

**Key Differences and Relationships** 
- **Definition of MDE:** The smallest change in a metric (e.g., conversion rate) that you want your test to reliably detect. It acts as a "sensitivity dial" for your experiment, set before the test runs.
- **Definition of P-Value:** The probability of observing a difference as large as (or larger than) what you saw, assuming there is no actual difference (null hypothesis).
- **The Goal:** You want to run a test where the **p-value is below your significance threshold** (usually 0.05) and the **observed effect is at least as large as your MDE**. 

**Core Concepts Explained** 
1. **MDE Determines Sample Size:** A lower MDE (e.g., wanting to detect a 1% lift) requires a much larger sample size to be statistically powered compared to a higher MDE (e.g., wanting to detect a 10% lift).
2. **MDE is a Target, Not a Result:** The MDE is defined _before_ the test. If you observe an effect smaller than your MDE, it may still be statistically significant (low p-value), but the test was not specifically designed to reliably detect such a small change.
3. **P-Value Measures Significance:** If the p-value is low ($p<0.05$), the result is deemed statistically significant, meaning the observed difference is unlikely to be due to chance. 

**Common Pitfalls** 
- **"Peeking" at Results:** A common, invalid practice is to stop a test the moment the p-value falls below 0.05, regardless of whether the target MDE has been reached. This drastically increases the risk of false positives.
- **Setting MDE Too Low:** Setting an extremely low MDE requires a massive sample size, leading to "zombie experiments" that run for too long. 

**Summary Table** 

| Concept          | What it is                         | When it's decided |
| ---------------- | ---------------------------------- | ----------------- |
| **MDE**          | Minimum desired, meaningful uplift | Before the test   |
| **P-Value**      | Probability of result being noise  | After the test    |
| **Significance** | $𝑝<0.05$ (standard)               | After the test    |