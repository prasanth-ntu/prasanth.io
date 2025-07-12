---
tags:
  - DataScience
---
Pre-training Text [[Encoder Models|Encoders]] as Discriminators Rather Than Generators.

ELECTRA is a new pretraining approach which **trains two [[Transformer Model|transformer models]]**: the **generator** and the **discriminator**. The **generator**’s role is to *replace tokens in a sequence*, and is therefore trained as a [[MLM|masked language model]]. The **discriminator**, which is the model we’re interested in, tries t*o identify which tokens were replaced by the generator* in the sequence.

In other words, we train the model to detect whether words in a sentence are real or replaced, adding robustness to the model’s understanding of language.

For more details, refer 
- https://huggingface.co/docs/transformers/en/model_doc/electra