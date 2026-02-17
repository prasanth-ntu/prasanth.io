---
tags:
  - aws
  - certification
  - cloud
  - career-development
  - devops
aliases:
  - Knowledge/Tech-Science/AWS Certification Plan
draft: true
---

# AWS Certification Plan

## Goal

Build formal AWS credentials that compound on existing production ML and infrastructure experience. The certification path is designed to:

1. **Validate core identity** as an ML Engineer (Cert 1)
2. **Broaden architectural depth** for senior/staff-level roles (Cert 2)
3. **Specialize further** based on career direction (Cert 3)

The "ML + Architecture" combination is rare and highly valuable — most people have one or the other.

## Certification Sequence

### 1. AWS Certified Machine Learning Engineer - Associate (MLA-C01)

| Detail | Value |
|--------|-------|
| Cost | $150 USD |
| Duration | 130 min, 65 questions |
| Target | Exam by mid-March 2026 |
| Prep needed | 2-3 weeks |

**Why first:** Directly maps to existing skillset — production ML, SageMaker, MLOps, model deployment. This is the *new* cert replacing the retiring ML Specialty (last exam March 31, 2026). Early holders get differentiation value. Study material doubles as interview prep for ML system design questions.

**Key domains:**
- Data preparation for ML (SageMaker Data Wrangler, Feature Store)
- ML model development (SageMaker training, hyperparameter tuning)
- ML model deployment and orchestration (SageMaker Pipelines, endpoints)
- ML solution monitoring and maintenance (Model Monitor, drift detection)

**Study resources:**
- [ ] Stephane Maarek & Frank Kane — [ML Engineer Associate: Hands On!](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/) (Udemy, 23hrs) [^1]
- [ ] AWS Skill Builder — [Exam Prep Plan for MLA-C01](https://skillbuilder.aws/exam-prep/machine-learning-engineer-associate) (free) [^2]
- [ ] Tutorial Dojo — [MLA-C01 Practice Exams](https://portal.tutorialsdojo.com/product/aws-certified-machine-learning-engineer-associate-mla-c01-practice-exams/) (Jon Bonso) [^3]
- [ ] Tutorial Dojo — [Free MLA-C01 Practice Sampler](https://portal.tutorialsdojo.com/courses/free-aws-certified-machine-learning-engineer-associate-practice-exams-mla-c01-sampler/) (20 free questions) [^4]
- [ ] AWS Official — [MLA-C01 Exam Guide PDF](https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf) [^5]
- [ ] Hands-on: SageMaker Studio notebook exercises
- [ ] Review: [SageMaker Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html), [Pipelines](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html), [Deploy from Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-deploy.html) [^6]

### 2. AWS Certified Solutions Architect - Associate (SAA-C03)

| Detail | Value |
|--------|-------|
| Cost | $75 USD (50% discount from Cert 1) |
| Duration | 130 min, 65 questions |
| Target | April-May 2026 |
| Prep needed | 4-6 weeks |

**Why second:** Broadens from ML-specific to full architectural knowledge. VPC, IAM, networking, storage, compute, databases, serverless. The most universally respected AWS cert. Reddit consensus: always do SAA before attempting Professional.

**Key domains:**
- Design secure architectures (IAM, VPC, security groups, NACLs)
- Design resilient architectures (multi-AZ, auto-scaling, load balancing)
- Design high-performing architectures (caching, CDN, storage tiers)
- Design cost-optimized architectures (Reserved/Spot instances, S3 tiers)

**Study resources:**
- [ ] Stephane Maarek — [Ultimate AWS Certified Solutions Architect Associate 2026](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/) (Udemy, 4.7 stars, 1.2M+ students) [^7]
- [ ] Stephane Maarek — [SAA-C03 Practice Exams](https://www.udemy.com/course/practice-exams-aws-certified-solutions-architect-associate/) (Udemy) [^8]
- [ ] Tutorial Dojo — [SAA-C03 Practice Exams](https://portal.tutorialsdojo.com/product/aws-certified-solutions-architect-associate-practice-exams/) (Jon Bonso, 401 questions) [^9]
- [ ] Tutorial Dojo — [SAA-C03 Study Path & Cheat Sheets](https://tutorialsdojo.com/aws-certified-solutions-architect-associate-saa-c03/) (free) [^10]
- [ ] AWS Official — [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) ([PDF](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf)) [^11]
- [ ] Hands-on: Build a multi-tier VPC with public/private subnets

### 3. Choose one based on career direction

**Option A: Solutions Architect Professional (SAP-C02)** — for architecture/platform leadership

| Detail | Value |
|--------|-------|
| Cost | $150 USD (50% discount) |
| Prep needed | 2-3 months |
| Target | Q3-Q4 2026 |

Best if: Consulting path, or any role requiring deep multi-account, hybrid-cloud, migration architecture expertise. One of the hardest cloud certs — validates serious architectural depth.

**Option B: Data Engineer Associate (DEA-C01)** — for data/ML pipeline track

| Detail | Value |
|--------|-------|
| Cost | $75 USD (50% discount) |
| Prep needed | 3-4 weeks |
| Target | Q3-Q4 2026 |

Best if: Any role heavy on data pipelines (Glue, Kinesis, Redshift, Athena). Complements ML + Architecture with data engineering depth.

## Cost Breakdown (50% Discount Chain)

| Cert | List Price | Actual Cost | Savings |
|------|-----------|-------------|---------|
| ML Engineer Associate | $150 | $150 | — |
| SA Associate | $150 | $75 | $75 saved |
| Cert 3 (Professional or Data Eng) | $150-$300 | $75-$150 | $75-$150 saved |
| **Total (3 certs)** | **$450-$600** | **$300-$375** | **$150-$225 saved** |

Each passed exam gives a 50% discount voucher for the next exam.

## Why NOT the ML Specialty?

- Last exam date: March 31, 2026 — too tight with leave ending March 2 + new baby
- Costs $300 vs $150 for the ML Engineer Associate
- The new ML Engineer Associate is more production-focused (better aligned with actual work)
- ML Specialty won't be renewable after retirement

## Timeline

```mermaid
gantt
    title AWS Certification Timeline
    dateFormat YYYY-MM-DD
    section Phase 1
    ML Engineer Associate Study    :2026-02-17, 21d
    ML Engineer Associate Exam     :milestone, 2026-03-10, 0d
    section Phase 2
    SA Associate Study             :2026-04-01, 42d
    SA Associate Exam              :milestone, 2026-05-15, 0d
    section Phase 3
    Cert 3 Study                   :2026-08-01, 60d
    Cert 3 Exam                    :milestone, 2026-10-01, 0d
```

## Related Notes

- [[Docker]] — Container fundamentals, essential for ML deployment domains
- [[Kubernetes (K8s)]] — Orchestration knowledge, relevant to SageMaker and EKS
- [[Spark]] — Distributed data processing, relevant to Data Engineer cert path

## References

[^1]: Stephane Maarek & Frank Kane. "AWS Certified Machine Learning Engineer Associate: Hands On!" Udemy. https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/
[^2]: AWS Skill Builder. "Exam Prep Plan: AWS Certified Machine Learning Engineer – Associate (MLA-C01)." https://skillbuilder.aws/exam-prep/machine-learning-engineer-associate
[^3]: Jon Bonso. "AWS Certified Machine Learning Engineer Associate MLA-C01 Practice Exams." Tutorials Dojo. https://portal.tutorialsdojo.com/product/aws-certified-machine-learning-engineer-associate-mla-c01-practice-exams/
[^4]: Tutorials Dojo. "FREE AWS Certified Machine Learning Engineer Associate Practice Exams MLA-C01 - Sampler." https://portal.tutorialsdojo.com/courses/free-aws-certified-machine-learning-engineer-associate-practice-exams-mla-c01-sampler/
[^5]: AWS. "AWS Certified Machine Learning Engineer - Associate (MLA-C01) Exam Guide." https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf
[^6]: AWS Documentation. "SageMaker Model Registry", "SageMaker Pipelines", "Deploy a Model from the Registry." https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html
[^7]: Stephane Maarek. "Ultimate AWS Certified Solutions Architect Associate 2026 (SAA-C03)." Udemy. https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/
[^8]: Stephane Maarek. "Practice Exams | AWS Certified Solutions Architect Associate (SAA-C03)." Udemy. https://www.udemy.com/course/practice-exams-aws-certified-solutions-architect-associate/
[^9]: Jon Bonso. "AWS Certified Solutions Architect Associate SAA-C03 Practice Exams." Tutorials Dojo. https://portal.tutorialsdojo.com/product/aws-certified-solutions-architect-associate-practice-exams/
[^10]: Tutorials Dojo. "AWS Certified Solutions Architect Associate Exam - SAA-C03 Study Path." https://tutorialsdojo.com/aws-certified-solutions-architect-associate-saa-c03/
[^11]: AWS. "AWS Well-Architected Framework." https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
[^12]: AWS. "AWS Certified Machine Learning Engineer – Associate." Official certification page. https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/
[^13]: AWS. "AWS Certification - Validate AWS Cloud Skills." https://aws.amazon.com/certification/
[^14]: Reddit r/aws. "Is AWS Solution Architect - Associate a respected enough cert to begin with?" https://www.reddit.com/r/aws/comments/1g48zmv/is_aws_solution_architect_associate_a_respected/
