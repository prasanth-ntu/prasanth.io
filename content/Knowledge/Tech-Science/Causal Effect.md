---
tags:
  - machinelearning
  - datascience
  - Statistics
  - Learning
---
> [!TIP] Casual effect refers to the direct impact that one variable (e.g., surge pricing) has on another variable (e.g., Book Through Rate), isolating this relationship from other influencing factors (e.g., day of time, weather, seasonal trends, etc.).

---
- **Definition**: A causal effect refers to the specific change in an outcome that can be attributed to a particular intervention, treatment, or action. It quantifies the impact of one variable on another, assuming a cause-and-effect relationship.
- **Example**: If taking a medication reduces blood pressure, the causal effect of the medication is the reduction in blood pressure caused by its use.
- **Focus**: It is often used in statistical and experimental contexts to measure the magnitude of the relationship between cause and effect.
---
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
  - **Outcome**: The model shows that increasing ad spend on Platform A by \$100 increases the conversion rate by 0.3%, while increasing ad spend on Platform B by \$100 increases the conversion rate by 0.7%.

## Conclusion
By ensuring the ad campaign effectiveness model is causally correct, the company can make more reliable and effective decisions, optimizing ad spend, placement, and targeting to achieve the desired objectives of maximizing conversions and minimizing costs. The use of a two-step model allows for both high predictive accuracy and causal validity, providing a robust framework for ad campaign optimization.

---
# What does "Causal Impact Analysis" mean?

In general terms, **Causal Impact Analysis** is a statistical method used to determine whether a specific action, event, or intervention had a significant effect on an outcome. It goes beyond simple correlation (observing that two things happened at the same time) and tries to establish a cause-and-effect relationship. It answers the question: "Did our action _cause_ this change, or would it have happened anyway?"

For example, the Causal Impact Analysis could becperformed to evaluate if the BTR (Book Through Rate) model could accurately predict how a change in the discount value _caused_ a change in the BTR.

---
# What does "Average Treatment Effect" mean?

Conceptually, the **Average Treatment Effect (ATE)** is a measure used within [[Causal Effect#What does "Causal Impact Analysis" mean?|causal analysis]] to quantify the impact of an intervention or "treatment." It calculates the average difference in outcomes between a group that received the treatment (the "treatment group") and a comparable group that did not (the "control group").

## Example:
- **Treatment:** The specific action being studied. Say, the "treatments" are the different discount values of $1.0, $1.5, and $2.0.
- **Effect:** The outcome you are measuring. Say, this was the BTR.
- **Average:** It represents the average impact across the entire group, not the effect on any single individual.

---
# Causal Impact Analysis vs. Average Treatment Effect

> [!TIP] **Causal Impact Analysis is the _process_ or _method_, and the Average Treatment Effect (ATE) is the _result_ or _measurement_ you get from that process.**

Think of it like a medical check-up:

- **Causal Impact Analysis** is the entire procedure of going to the doctor to find out if a new diet is working. This includes designing the test (e.g., tracking your weight for 30 days while on the diet), finding a valid comparison (e.g., your weight trend before the diet), and analyzing the data.
- **Average Treatment Effect (ATE)** is the specific number the scale shows you at the end: "-3 kg". It's the quantifiable outcome of the analysis.

---
## Example: Google Ads

An e-commerce company wants to know if using a new ad format, "Video Discovery Ads," is more effective at driving sales than their standard "Image Ads."

- **Business Question:** Does switching our ad budget from Image Ads to Video Discovery Ads _cause_ a higher return on investment?

#### Causal Impact Analysis

This is a classic use case for an A/B test, which is a straightforward way to conduct a causal analysis.

- **How it's done:** The company uses Google Ads' built-in "Campaign Experiments" feature.
    1. **Setup:** They create an experiment where their target audience is randomly split into two groups.
    2. **Control Group (Group A):** This 50% of the audience continues to see the standard **Image Ads**.
    3. **Treatment Group (Group B):** This 50% of the audience is shown the new **Video Discovery Ads**.
    4. **Analysis:** The experiment runs for a set period (e.g., 30 days). Because the audience was split randomly, any significant difference in performance between the two groups can be confidently attributed to the different ad formats.

#### Average Treatment Effect (ATE)

The ATE measures precisely how much better (or worse) the new ad format performed.

- **Treatment:** Being shown a Video Discovery Ad.    
- **Outcome Metric:** Conversion Rate (the percentage of people who click the ad and then make a purchase).
- **ATE Calculation:** After 30 days, the results are:
    - Control Group (Image Ads) Conversion Rate = 2.0%
    - Treatment Group (Video Ads) Conversion Rate = 2.5%
    The Average Treatment Effect is the difference: **+0.5 percentage points**.
- **Meaning:** The ATE shows that using Video Discovery Ads caused a 0.5 percentage point increase in the conversion rate. This tells the company that for every 1,000 people who click a video ad, they can expect 5 more sales than if those people had clicked an image ad. This provides a clear justification for shifting more budget to video.

## Detailed breakdown:

| **Aspect**                    | **Causal Impact Analysis**                                                                                                                      | **Average Treatment Effect (ATE)**                                                            |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Role**                      | The overall **framework, methodology, or experiment** designed to isolate a cause-and-effect relationship.                                      | The specific, **quantitative metric** that measures the outcome of the analysis.              |
| **Question it Answers**       | "**How** can we reliably determine if our action caused a change?"                                                                              | "**By how much** did our action change the outcome on average?"                               |
| **In the Google Ads Example** | The analysis was the A/B test itself—the splitting of the audience and running the two ad versions simultaneously.                              | The ATE was the result of that test: **a +0.5 percentage point increase** in conversion rate. |

> [!SUMMARY] In short, you perform a **Causal Impact Analysis** in order to calculate the **Average Treatment Effect**. The ATE is the main piece of evidence that the analysis provides to prove whether the intervention was successful and by how much.