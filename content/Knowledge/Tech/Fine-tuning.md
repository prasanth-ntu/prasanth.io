---
tags:
  - DataScience
---
<span style="color:green"><i>Fine-tuning</i>, on the other hand, is the training done <b>after</b> a model has been pretrained. To perform fine-tuning, you first acquire a pretrained language model, then perform additional training with a dataset specific to your task</span>. 

![Fine-tuning from pre-training](https://huggingface.co/datasets/huggingface-course/documentation-images/resolve/main/en/chapter1/finetuning.svg)

**Wait — why not simply train directly for the final task? There are a couple of reasons:**

1. **Take advantage of knowledge gained from source task**: The pretrained model was already trained on a dataset that has some similarities with the fine-tuning dataset. The **fine-tuning process is thus able to take advantage of knowledge acquired by the initial model during pretraining** (for instance, with NLP problems, the pretrained model will have some kind of statistical understanding of the language you are using for your task).
2. **Less data**: Since the pretrained model was already trained on lots of data, the **fine-tuning requires way less data** to get decent results.
3. **Time and Resources**: For the same reason**, the amount of time and resources needed to get good results are much lower**.

For example, one could leverage a pretrained model trained on the English language and then fine-tune it on an arXiv corpus, resulting in a science/research-based model. The fine-tuning will only require a limited amount of data: the knowledge the pretrained model has acquired is “transferred,” hence the term _[[Transfer learning|transfer learning]]_.

Fine-tuning a model therefore has ***lower time, data, financial, and environmental costs***. It is also quicker and easier to iterate over different fine-tuning schemes, as the training is less constraining than a full pretraining.

This process will also achieve better results than training from scratch (unless you have lots of data), which is why you should **always try to leverage a pretrained model — one as close as possible to the task you have at hand — and fine-tune it.**