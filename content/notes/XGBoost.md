---
tags:
  - data-science
  - machine-learning
aliases:
  - Knowledge/Tech-Science/XGBoost
---
# xgboost.XGBClassifier

**Use(ful) Parameters**
- `max_depth`
- `max_leaves`
- `n_estimaters`
- `eta`
- `scale_pos_weight`[^2]
	- Balances positive (minority) and negative (majority) classes in imbalanced datasets by weighting errors on the positive class, preventing the model from ignoring rare events, with a typical value of `count(negative_samples) / count(positive_samples)`. This parameter is crucial for improving recall and AUC in binary classification by telling the model to penalize misclassifications of the positive class more heavily, helping it learn from the minority class more effectively.
	- How it works?
		- **Default value:** `1` (no weighting).
		- **Recommended setting:** Set it to the ratio of negative to positive instances: `count(negative_instances) / count(positive_instances)`. For extreme imbalance, `sqrt(count(negative_instances) / count(positive_instances))` is sometimes suggested.
		- **Effect:** It helps the model converge faster and improves metrics like recall, precision, and AUC for the minority class, reducing the need for complex sampling techniques like over/undersampling.


For more details, refer
- Official API doc [^1]
- 

# Footnote
[^1]: https://xgboost.readthedocs.io/en/latest/python/python_api.html#xgboost.XGBClassifier
[^2]: https://xgboost.readthedocs.io/en/stable/parameter.html
