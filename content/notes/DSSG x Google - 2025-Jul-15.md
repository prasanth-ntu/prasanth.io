---
tags:
  - ai
  - data-science
  - google
  - machine-learning
  - talk
draft: true
aliases:
  - Talks/DSSG x Google - 2025-Jul-15
---
# Meetup event details
[Meetup link](https://www.meetup.com/datascience-sg-singapore/events/308852900/?_xtd=gqFyqTIzMTMyMjg3MKFwo2FwaQ%253D%253D&from=ref)

Discover how you can create agents faster with the Agent Development Kit (ADK), and learn from real-world experience transitioning from traditional machine learning to enterprise-level GenAI solutions.

**Agenda**

- **6:30 PM – 7:00 PM** Registration & Networking
- **7:00 PM – 7:30 PM** _Agent Development with ADK & Agent Engine_
- **7:30 PM – 8:00 PM** _How did I transfer from Training Xgboost Models to Building Production-Ready and Enterprise-Level GenAI Solutions_
- **8:00 PM – 8:30 PM** Q&A and Closing

**Synopsis**

- **Agent Development with ADK and Agent Engine** – _by Wei Yih_  
    In this session, you will learn about how Agent Development Kit (ADK) and Agent Engine features can streamline agent development, empowering you to build agents faster than ever.
- **How did I transfer from Training Xgboost Models to Building Production-Ready and Enterprise-Level GenAI Solutions** - _by Guan Wang_  
    Building GenAI solutions brings challenges to data scientists who are more used to building traditional ML models. In this talk we will discuss about the shift of experience for a data scientist working on GenAI, and what a full-stack developer is like - from gathering user stories, iterating with UI/UX, to chasing business to label data for proper accuracy evaluation of GenAI solutions, in addition to his/her influence on traditional IT tasks like infrastructure setting and architecture design, performance testing, logging/monitoring and more
---
# **How did I transfer from Training Xgboost Models to Building Production-Ready and Enterprise-Level GenAI Solutions** - _by Guan Wang_ 

**Evaluation Work form the Very Start - just link ML**
- GenAI Evaluation vs Traditional Machine Learning Evaluation
- "Training", "Testing"
- Synthetic Data Generation with Business Validation/Labelling
- Confusion Matrix/Accuracy/Precision/Recall/F1 score
- LLM as Judge

**Not a typical Data Scientist Job - Business Case**
- **Business Requirements & User Stories**
	- As a `<role>`
	- I want `<goal>`
	- so that `<benefit>`
	- Acceptance criteria: `xxx`
- **Cost Estimation (and tracking)**
	- API, infra
	- Dev efforts
	- Post Production Service
- **Benefit Estimation (and tracking)**
	- Sales Uplift
	- Average Handling Time
	- A/B Testing
- **Build a Project Squad**
	- Project Manager
	- SCRUM Master
	- Tech team
		- Business Analyst
		- UI/UX Designer
		- IT Frontend Developers
		- IT Backend Developers
		- QA Testers
		- AI Developers (sometimes, Data Scientists)
		- Data Scientists
		- ML Engineers
	- Non-tech (Domain experts) team
		- Domain Experts
		- Information Risk Team
		- Model Risk Team
		- Business Risk Team
		- AI Tool Trainers
		- Champion Users
- **Architecture and Solution design**
	- Python vs Java
	- Real-time vs. Near Real-time vs. Batch
	- Databricks vs. Azure Kubernetes Service vs. Azure Functions
	- Agentic vs. Workflow
	- Function calling vs. text2sql vs. MCP
- **Model Choices**
	- Model capabilities
	- Cost
	- Availability
- **DevOps - Proper Python Software Engineering**
	- JIRA
	- GitHub
	- CI/CD, unit testing, SIT/UAT
	- Logging and Monitoring
- **UI/UX Design - Iteration and Iteration**
	- LLM Behaviour
	- Manage user expectations
	- Gather user feedbacks
	- Risk disclaimer
- **Performance Testing**
	- Latency vs Throughput
	- ...
- **SIT & UAT**
- **Disaster recovery**
- GenAI Solution Monitoring and Ops
	- Performance tracking (e.g., response time, accuracy)
	- Cost tracking and optimization
	- KPI tracking
		- Lead KPIs (e.g., user adoption, log-in frequency, click rate)
		- Lag KPIs (e.g., sales uplift)