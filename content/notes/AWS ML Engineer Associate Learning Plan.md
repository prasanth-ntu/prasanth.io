---
tags:
  - aws
  - certification
  - course
  - data-science
  - sagemaker
aliases:
  - Courses/AWS ML Engineer Associate Study Notes
draft: true
---
**Key resources**
- [[AWS Certification Plan|AWS Certification Plan]] — overall cert strategy and timeline
- AWS Skill Builder — [ML Engineer Associate Learning Plan](https://skillbuilder.aws/learning-plan/AY5A6VN52B/aws-ml-engineer-associate-learning-plan-includes-labs/C21UPEK6R9) (26hrs, 20 modules)
- AWS Skill Builder — [Exam Prep Plan for MLA-C01](https://skillbuilder.aws/learning-plan/A2FGY8CH1P/exam-prep-plan-aws-certified-machine-learning-engineer--associate-mlac01--english/3YFU86SSKN) (16.5hrs, 17 modules)
- Stephane Maarek & Frank Kane — [ML Engineer Associate: Hands On!](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/) (Udemy)
- [MLA-C01 Exam Guide PDF](https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf)

---
# Curriculum Overview
> Module: AWS ML Engineer Associate Curriculum Overview (45m)

<!-- Key takeaways from the intro module go here -->

![[ml-cycle-example.png|977]]

---
# Domain 1: Data Preparation for ML (28% of exam)

## 1.1 Collect, Ingest, and Store Data
> Module: AWS ML Engineer Associate 1.1 (1h)

<!-- Key takeaways -->
**Types of Data**
- **Data collection**: Data lake vs. Data warehouse vs. Database
- **Data types**: Text, Tabular, Time series, Image
- **Data format:** Structured (e.g., Apache Parquet), Unstructured (e.g., Text, Audio, Video), Semi-structured (e.g., XML, JSON)
- **Data format file types**: Row-based (e.g., CSV, Apache Avro, RecordIO), Column-based (e.g., Apache Parquet, ORC), Object notation (e.g., JSON, JSONL)
- **Data ingestion:** Batch (e.g., Model training) vs. Streaming (e.g., Model inference and predictions) data

**Data Visualization & EDA** 
- **Data visualization methods**: Relationship analysis (e.g., correlation matrices, scatter plots, heat maps), Distribution analysis (e.g., box plot, histograms, KDE plots), Comparison (e.g., bar charts, box plots by group. line charts), Composition (e.g., pie chart)
- **Data visualization graphs based on data type**: Categorical data (e.g., gender, race) $\Rightarrow$ Qualitative (e.g., bar chart, pie chart, heat maps), Numerical data (e.g., age, income) $\Rightarrow$ Quantitative (e.g., scatter plots, histograms, box plots, kde/density plots)

> [!WARNING] Categorical (Nominal) vs. Ordinal
>  - Categorical (Nominal): No inherent order (e.g., Dog, Cat, Bord)
>  - Ordinal: Meaningful order or ranking (e.g., Low, Medium, High)

**AWS Storage Options**
- **Storage considerations**: Cost, Performance, Data Structure, and Access Pattern
- **Storage Services for ML tasks**: S3, EBS, EFS, FSx
- **Storage based on ML workload categories**: 
	- Training: EBS or EC2
	- Inference: EBS or EFS
	- Real-time & Streaming: EFS
	- Dataset Storage: S3
- **Storage based on Data access Pattern**:
	- Copy and load: S3 $\rightarrow$ EBS
	- Sequential Streaming: S3 $\rightarrow$ EBS
	- Randomised access: EFS and FSx

**Data Ingestion**
- **Data ingestion methods**: Batch vs. Real-time
- **AWS dedicated streaming services**: 
	- Amazon **Kinesis** Data Stream
	- Amazon Managed Streaming for Apache **Kafka** (MSK)
	- Amazon Managed Service for Apache **Flink** (MSF)

![[aws-kinesis-example.png|710]]

**Data Extraction**
- **Data transfer and extraction tools**: CLI, SDK, S3 Transfer Acceleration, DMS, Lambda, Glue, DataSync, Snowball

 ![[aws-data-transfer-and-extraction-tools.png|627]]

**Data Merging**
- **AWS services for data merging**: Glue, EMR, SageMaker Data Wrangler

 ![[aws-glue-flow-example.png|678]]
 ![[aws-emr-flow-example.png|680]]
 ![[aws-sagemaker-data-wrangler-flow-example.png|747]]

**Data Ingestion and Storage Troubleshooting**
- **Monitoring tools**: CloudWatch (Metrics, Logs and Dashboards)
- **AWS Storage service metrics**
	- EBS metrics: VolumeReadBytes, VolumeWriteBytes, VolumeReadOps, VolumeWriteOps, VolumeThroughputPercentage, VolumeQueueLength
	- S3 metrics: BucketSizeBytes, NumberOfObjects, AllRequests, GetRequests, PutRequests
	- EFS metrics: StorageBytes, PercentIOLimit, TotalIOBytes
	- FSx metrics: DataReadBytes, DataWriteBytes, ThroughputCapacity, PercentThroughputCapacityUtilized
- **Scalability issues**: 
	- Capacity issues with data destinations
	- Latency issues, IOPs, and data transfer times
	- Uneven distribution of data access
- **Ingestion modifications**
	- Batching
	- Compression
	- Partitioning

## 1.2 Transform Data
> Module: AWS ML Engineer Associate 1.2 (1h)

<!-- Key takeaways -->
**Techniques for data transformation**
- Data Cleaning
- Categorical encoding
- Feature engineering

**Data Cleaning Techniques**
- **Incorrect and Duplicated data**
> [!SUMMARY] The process of automating data duplication removal is called _deduplication_. Deduplication works by scanning datasets for duplicate information, retaining one copy of the information, and replacing the other instances with pointers that direct back to the stored copy. Deduplication can drastically increase storage capacity by keeping only unique information in your data repositories.
- **Outliers**
	- Central tendency + Symmetry vs. Asymmetry: Mean, Median, Standard Deviation
	- Natural outliers (e.g., extremely tall individual) vs. Artificial outliers (e.g., temperature captured from faulty thermometer)
- **Incomplete or Missing Data**
	1. Identify missing values
	2. Determine why values are missing 
		- Missing at Random (MAR)
		- Missing Completely at Random (MCAR)
		- Missing Not at Random (MNAR)
	3. Drop (or) Impute missing values 

**Categorical Encoding Techniques**
- **Types of categorical values**: Binary (e.g., someone attended an event?), Nominal or multi-categorical (e.g., zip-code), Ordinal (e.g., drink size at a coffee shop: S, M, L)
> [!TIP] Not all categorical variables need to be encoded. Depending on your use case, different ML algorithms (e.g., Random Forest) might not require you to encode your variables.

- **Encoding techniques**: Label vs. One-hot encoding. For more details, refer [[Encodings]]
> [!TIP] Label encoding provides a unique value for each combination without growing your dataset too large.

> [!WARNING] One-hot coding might not be the best technique if there are a lot of categories. 
> These additional columns might grow your dataset so much that it makes it difficult to analyze efficiently.

**Feature Engineering**
- **Numerical feature engineering**
	- **Binning** (e.g., quantile binning)
	- **Feature scaling**
		- [[Min-Max Normalization]]: $X_{normalized}=(X-X_{min})\div(X_{max}-X_{min})$
		- Standardization or Z-Score Scaking: $X_{standardized}=(X-X_{mean})\div(X_{std})$
	- **Log transformation** (e.g., ) the log of $10,000 would be around 4 and the log of $10,000,000 would be around 7. Using this method, the outliers are brought much closer to the normal values in the remainder of the dataset.

> [!TIP] Standardization is more robust to outliers than normalization.
> For more details, refer [[Feature Engineering#Standarization vs. Normalization]]

> [!TIP] To scale or not to scale
> A lot of ML algorithms are sensitive to wide ranges of data, so feature scaling is required for many ML models. However, some ML models like decision trees are not skewed by wide ranges of numeric data. Whether or not to scale your data will depend on the ML algorithm that you decide to use.

- **Text feature engineering**: 
	- **Bag of words**
	- **N-gram**
	- **TF-IDF**

- **Temporal feature engineering**
	- e.g., Extract day, month, and year from timestamp

- **Other techniques**
	- Feature selection
	- Feature splitting
	- Feature combining
	- Dimensionality reduction (using PCA)

**AWS Tools and Services for Data Transformation**
- **Data Labeling**
	- Mechanical Turk
	- SageMaker Ground Truth
- **Data Ingestion**
	- **SageMaker Data Wrangler**: Use cases include data cleaning, feature engineering, fixing formatting issues, reducing data size, and automating transformations
	- **SageMaker Feature Store**: Use cases include automated data processing, centralised feature repository, standardized features, management of feature pipelines, caching for performance
- **Data Transformation**
	- **Glue + Glue DataBrew**: Use cases include automated ETL pipelines, data integration and ingestion, data cleansing and standardization, feature engineering, final pretraining data preparation 
		![[aws-using-glue-for-data-transformation.png|696]]
	- **SageMaker Data Wrangler**: Use cases include data cleaning, feature engineering, fixing formatting issues, reducing data size, and automating transformations
		![[aws-using-sagemaker-data-wrangler-for-data-transformation.png]]
	- **Lambda**
	- **Spark on EMR**

- **Demo: Transforming data by using Glue**
	1. Use AWS Glue to crawl and catalog data
	2. Load datasets into AWS Glue DataBrew
	3. Create a profile job in AWS Glue DataBrew
	4. Create a sales profile job in AWS Glue DataBrew
	5. Create a project in AWS Glue DataBrew
	6. Build a recipe in AWS Glue DataBrew

## 1.3 Validate Data and Prepare for Modeling
> Module: AWS ML Engineer Associate 1.3 (45m)

<!-- Key takeaways -->
**Fundamentals of Data Validation**

> [!SUMMARY] Data integrity refers to the accuracy, completeness, reliability, consistency, and security of data

> [!DANGER] ML models trained on datasets that exhibit these biases could end up learning them and then reproduce or even exacerbate those biases in their predictions.

- **Pre-training Bias Metrics**
	- **Class imbalance** (CI)
	- **Label imbalance**, such as difference in proportion of labels (DPL)
	For more information about different types of pre-training bias metrics, visit [Pre-training Bias Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-measure-data-bias.html)
- **Addressing Class Imbalance**
	1. **Resampling**: Undersampling or Oversampling
	2. **Synthetic data generation**: e.g., SMOTE
	3. **Data augmentation**: e.g., rotating, scaling, cropping, flipping, or adding noise to a dataset or using GAN
- **AWS Tools and Services for Data Validation and Bias Mitigation**
	- **Glue Data Quality**: Data quality rules, Automated scheduling, Data quality dashboards
	- **Glue DataBrew**: Data profiling, Built in transformations, Custom transformations
	- **Comprehend**: Entity recognition, Topic Modelling, Language Detection
	- **SageMaker Clarify**: Analyzes data and models across the ML lifecycle - pre-training, post-training, and in production - using metrics to identify bias (e.g., CI, DPL, drift/divergence) and explain model predictions (e.g., SHAP)
- **Data Security and Compliance**
	- **AWS encryption services**
		- **KMS**: Customer managed keys, AWS managed keys
		- **EBS**
		- **S3**: S3 managed encryption keys (SSE-S3), KMS managed encryption keys (SSE-KMS), Customer-provided encryption keys (SSE-C)
		- **RDS**
		- **RedShift**
		- **ElasticCache**
		- **Lambda**
		- **SageMaker**
	- **Data compliance requirements**
		- PII (e.g., GDPR, PDPA, CCPA)
		- PHI (e.g., HIPAA)
		- Data residency (e.g., GDPR)
	- **AWS data validation services for security and compliance**: Glue & Comprehend

**Final steps of Data Preparation**
- **Dividing datasets to reduce bias**
	- **Train, test, validate: A tripartite approach**
	- **Data-splitting techniques**: Simple hold-out, Cross-validation
	- **Dataset shuffling techniques**: Random permutation, Epoch-based shuffling, Mini-batch shuffling
	- **Data augmentation**: Image-based, Text-based, Time series
- **Configure data for model training**
	- Python libraries for data formatting: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

## Lab: SageMaker Data Wrangler and Amazon EMR
> Lab: Analyze and Prepare Data with Amazon SageMaker Data Wrangler and Amazon EMR (1h)

<!-- Lab notes -->

`adult_data.csv`
- 14 **Features**
	- 6 **numeric**: fnlwgt, age, education_num, capital_gain, hours_per_week, capital_loss
	- 4 **categorical**: workclass, relationship, marital_status, race
	- 3 **text**: occupation, education, native_country
	- 1 **binary**: sex
- Target column: income
- Type: Classification

![[aws-data-wranger-data-flow-adult-csv-data-previeww.png|550]]

![[aws-data-wranger-data-flow-adult-csv-dataflow-1.png|550]]

![[aws-data-wranger-data-flow-adult-csv-dataflow-2.png|550]]

> [!info]- Data Wrangler Insights Report
> ![[aws-lab-data-wrangler-insights-report.png|400]]

For *Task 6: Explore and query data from the SparkMagic PySpark kernel*, refer [jupyter notebook](https://gist.github.com/prasanth-ntu/0f8b557e88ea7aa07ba150d7a9f43082)

---
# Domain 2: ML Model Development (26% of exam)

## 2.1 Choose a Modeling Approach
> Module: AWS ML Engineer Associate 2.1 (1h 30m)

<!-- Key takeaways -->

## 2.2 Train Models
> Module: AWS ML Engineer Associate 2.2 (1h 30m)

<!-- Key takeaways -->

## 2.3 Refine Models
> Module: AWS ML Engineer Associate 2.3 (2h)

<!-- Key takeaways -->

## 2.4 Analyze Model Performance
> Module: AWS ML Engineer Associate 2.4 (1h 30m)

<!-- Key takeaways -->

## Lab: Train a Model with Amazon SageMaker
> Lab: Train a model with Amazon SageMaker (1h)

<!-- Lab notes -->

---
# Domain 3: Deployment and Orchestration of ML Workflows (22% of exam)

## 3.1 Select a Deployment Infrastructure
> Module: AWS ML Engineer Associate 3.1 (1h)

<!-- Key takeaways -->

## 3.2 Create and Script Infrastructure
> Module: AWS ML Engineer Associate 3.2 (1h 30m)

<!-- Key takeaways -->

## 3.3 Automate Deployment
> Module: AWS ML Engineer Associate 3.3 (1h 15m)

<!-- Key takeaways -->

## Lab: SageMaker Pipelines and Model Registry
> Lab: Orchestrate a Machine Learning Workflow using Amazon SageMaker Pipelines and SageMaker Model Registry (1h)

<!-- Lab notes -->

---
# Domain 4: ML Solution Monitoring, Maintenance, and Security (24% of exam)

## 4.1 Monitor Model Performance and Data Quality
> Module: AWS ML Engineer Associate 4.1 (2h 30m)

<!-- Key takeaways -->

## 4.2 Monitor and Optimize Infrastructure and Costs
> Module: AWS ML Engineer Associate 4.2 (2h 30m)

<!-- Key takeaways -->

## 4.3 Secure AWS ML Resources
> Module: AWS ML Engineer Associate 4.3 (2h 15m)

<!-- Key takeaways -->

## Lab: Monitor a ML Model for Data Drift
> Lab: Monitor a ML Model for Data Drift with Amazon CloudWatch (1h)

<!-- Lab notes -->

---
# Curriculum Conclusion
> Module: AWS ML Engineer Associate Curriculum Conclusion (10m)

<!-- Final notes, next steps -->

---
# Exam Prep Notes

## Practice Question Insights
<!-- Track patterns, tricky topics, and recurring themes from practice exams -->

## Weak Areas to Review
<!-- Topics that need extra attention based on practice exam results -->
