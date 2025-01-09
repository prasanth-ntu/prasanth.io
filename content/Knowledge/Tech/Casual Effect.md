---
tags:
  - MachineLearning
  - DataScience
  - Statistics
---
> [!TIP] Casual effect refers to the direct impact that one variable (e.g., surge pricing) has on another variable (e.g., Book Through Rate), isolating this relationship from other influencing factors (e.g., day of time, weather, seasonal trends, etc.).

A model is **causally correct** if it accurately captures and reflects the true cause-and-effect relationship between variables, ensuring that the observed effects are genuinely due to the changes in the variable of interest and not confounded by other factors.
# Example: Causally Correct Model for Ad Campaign Effectiveness

## Use Case
A company wants to optimize its online advertising campaigns to maximize conversions (e.g., purchases, sign-ups) while minimizing costs. The goal is to build a model that accurately predicts the effectiveness of different ad campaigns, taking into account the causal effect of various factors such as ad spend, ad placement, and targeting criteria.

## Key Points of Causal Effect or Causally Correct:

### 1. **True Cause-and-Effect Relationship**:
   - The model should accurately capture *how changes in ad spend*, placement, and targeting *directly influence conversion rates*. For example, increasing ad spend on a specific platform should show a measurable impact on conversions.
### 2. **Avoiding Spurious Correlations**:
   - The <span style="color:red">model should avoid mistaking correlations for causation</span>. For instance, if both ad spend and conversions are influenced by seasonal trends, the model should account for this and <span style="color:red">not attribute the entire effect on conversions to ad spend alone.</span>
### 3. **Controlling for Confounding Variables**:
   - The model should control for other variables that might affect conversions, such as time of day, day of the week, and competitor activities, ensuring that the observed effect is truly due to changes in ad campaign parameters.
### 4. **Predictive Accuracy and Causal Validity**:
   - While predictive accuracy is important, the model should also be causally valid. This means that it should provide reliable predictions based on the true causal relationships, which is crucial for making informed decisions in ad campaign optimization.

## Example Scenario:

### Scenario 1: Simple Regression Function
- **Objective**: Understand the direct impact of ad spend on conversion rates.
- **Model**: A linear regression model where the dependent variable is the conversion rate, and the independent variable is ad spend.
- **Outcome**: The model shows that for every $100 increase in ad spend, the conversion rate increases by 0.5%.

### Scenario 2: Two-Step Ad Campaign Model
- **Step 1: Baseline Conversion Prediction**
  - **Objective**: Predict the baseline conversion rate using a deep neural network.
  - **Features**: Historical conversion rates, ad spend, ad placement, targeting criteria, time of day, day of the week, competitor activities.
  - **Outcome**: The model predicts the baseline conversion rate with high accuracy.

- **Step 2: Delta Conversion Model**
  - **Objective**: Predict the change in conversion rate due to different levels of ad spend, placement, and targeting criteria.
  - **Features**: Changes in ad spend, placement, and targeting criteria.
  - **Outcome**: The model shows that increasing ad spend on Platform A by $100 increases the conversion rate by 0.3%, while increasing ad spend on Platform B by $100 increases the conversion rate by 0.7%.

## Conclusion
By ensuring the ad campaign effectiveness model is causally correct, the company can make more reliable and effective decisions, optimizing ad spend, placement, and targeting to achieve the desired objectives of maximizing conversions and minimizing costs. The use of a two-step model allows for both high predictive accuracy and causal validity, providing a robust framework for ad campaign optimization.