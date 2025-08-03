---
tags:
  - datascience
  - softwareengineering
  - deeplearningai
  - Course
  - AIAgent
  - CrewAI
---
**Key resources**
- Course [link](https://www.deeplearning.ai/short-courses/practical-multi-ai-agents-and-advanced-use-cases-with-crewai/)
	- Forum [link](https://community.deeplearning.ai/c/short-course-q-a/practical-multi-ai-agents-and-advanced-use-cases-w/487)
- My Github Repo [link](https://github.com/prasanth-ntu/DeepLearningAI-Practical-Multi-AI-Agents-and-Advanced)

Below sections contain the key take aways from each lesson.

---
# Overview of Multi AI-Agent Systems
**Use cases to be explored in this course**
- Automated Project Planning
- Project Monitoring
- Lead Qualification and Scoring
- Analysis and Report on Support Data
- Custom Content Creation at Scale

> [!TIP] Most of the use cases usually fo ground some form of research and analysis, summarization and reporting
<style>
.centered-img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  max-width: 720px;
  height: auto;
}
</style>
<img 
  src="operational-automation-use-cases-flow.png" 
  alt="Operational Automation Use Cases Flow" 
  class="centered-img"
  style="max-width:480px"
/>

> [!INFO] Main building blocks for building multi AI-agent systems
> 

<img src="multi-ai-agentic-system-block-diagram.png" alt="Main building blocks for building multi AI-agent systems"  class="centered-img">

> [!TIP] We can orchestrate agents in different ways
> 

<img src="different-ways-to-orchestrate-agents.png" alt="Different ways to orchestrate agents"  class="centered-img">

> [!TIP] We can build Agents and Crews even with a YAML file
> 

<img src="building-ai-agents-with-yaml-file.png" alt="Building AI Agents with YAML file"  class="centered-img">

---
# Automated Project: Planning, Estimation and Allocation (L2)

Unlike the [[DeepLearning.AI - Multi AI Agent Systems with CrewAI|previous course]], in this course, the `Agent` (`backstory`, `role`, and `goal`) and `Task` (`description`, and `expected_output`) are provided as `.yaml` files.

The Agentic `Crew` to perform Project Planning, Estimation and Resource Allocation was assembled using 3 `Agents`, and 3 `Tasks`.
- `Agents`
	- `project_planning_agent` with role as `The Ultimate Project Planner`
	- `estimation_agent` with role as `Expert Estimation Analyst`
	- `resource_allocation_agent` with role as `Resource Allocation Strategist`
- Class `TaskEstimate`, `MileStone`, and `ProjectPlan` using `pydantic BaseModel`
- `Tasks`
	- `task_breakdown`
	- `time_resource_estimation`
	- `resource_allocation` with `output_pydantic=ProjectPlan`
- `Crew`
> [!TIP] Since the output of `resource_allocation` tasks is configured to be pydantic, it can easily be converted to `json` and as pandas `DataFrame` subsequently for downstream processing.

--- 
# Internal and External Agents
**Internal tools** could be
- RAG search
- SQL query
- Trigger side effect

**External tools could be**
- Search the internet
- Check calendar
- Reply Email

<img src="data-analysis-crew-example.png" alt="Data Analysis Crew Example"  class="centered-img">

---
# Building Project Progress Report (L4)

The Agentic `Crew` to create a project progress report was assembled using 2 `Agents`, and 3 `Tasks`, and 2 custom built `Tools`.
- `Tools`
	- `BoardDataFetcherTool` and `CardDataFetcherTool` using crewai `BaseTool`
- `Agents`
	- `data_collection_agent` with `tools=[BoardDataFetcherTool(), CardDataFetcherTool()]`
	- `analysis_agent`
- `Tasks`
	- `data_collection`
	- `data_analysis`
	- `report_generation`
- `Crew`

> [!NOTE] The `analysis_agent` used for two different tasks (`data_analysis`, `report_generation`) in this project

<img src="l4-project-progress-report-summary.png" alt="Project Progress Report Summary"  class="centered-img"  style="max-width: 500px">

---
# Complex crew Setups


---
# Agentic Sales Pipeline (L6)

<img src="sales-pipeline-flow-part1.png" alt="Sales Pipeline Flow - Part 1"  class="centered-img"  style="max-width: 500px">

<img src="sales-pipeline-flow-part2.png" alt="Sales Pipeline Flow - Part 2"  class="centered-img"  style="max-width: 500px">

The Agentic `Crew` to create a Sales Pipeline was assembled using 2 `Crews`

`Crew` 1: `lead_scoring_crew` with 3 `Agents`, and 3 `Tasks`, and 2 `Tools`.
- `Agents`
	- `lead_data_agent`
	- `cultural_fit_agent`
	- `scoring_validation_agent`
- `Tasks`
	- `lead_data_task`
	- `cultural_fit_task`
	- `scoring_validation_task` with `context=[lead_data_task, cultural_fit_task] and `output_pydantic=LeadScoringResult`

`Crew` 2: `email_writing_crew` with 2 `Agents`, and 2 `Tasks`
- `Agents`
	- `email_content_specialist`
	- `engagement_strategist`
- `Tasks`
	- `email_drafting`
	- `engagement_optimization`

`SalesPipeline` - Built using `crewai`'s `Flow` feature
- Research a potential lead
- Score them given the person and the company details
- If it's a qualified lead, then draft a proper initial email

> [!TIP] Using `crewai` `Flow`, we can create end-to-end pipelines by leveraging `Flow` features like `start`, `listen`, `and_`, `or_`, `router` as well as `state`.
> 
> CrewAI operates on a higher level of abstraction, centered around the concept of a "crew" of autonomous AI agents. The "flow" in CrewAI dictates the sequence in which these agents, each with a specific role, set of tools, and a defined task, are activated. Key aspects include
> - Role-based task delegation
> - Sequential and Hierarchical workflows
> - Implicit state management
>   
>  This approach simplifies the process of creating multi-agent systems by focusing on the "who" and "what" rather than the "how" of the workflow. It excels in scenarios where the division of labor is clear and the process can be broken down into a series of distinct, role-based steps.

<img src="crewai_flow-for-agentic-sales-pipeline.png" alt="Crew AI flow for agentic sales pipeline - Part 2"  class="centered-img"  style="max-width: 600px">
<img src="crewai_flow-complex-for-agentic-sales-pipeline.png" alt="Crew AI Complex flow for agentic sales pipeline - Part 2"  class="centered-img"  style="max-width: 600px">

---
# Performance Optimization

> [!IMPORTANT] Speed and Quality are two main variables. However, Consistency is paramount.
<img src="speed-quality-consistency.png" alt="Performance Optimization - Speed, Quality, and Consistency"  class="centered-img"  style="max-width: 600px">

> [!QUESTION] How can we test agents performance?
> By comparing the `Task` description with expected outcome using `crewai test`.
<img src="crewai-improvements-of-tasks.png" alt="Crew AI improvement of tasks"  class="centered-img"  style="max-width: 600px">
<img src="crewai-checking-consistency.png" alt="Crew AI checking for consistency and quantifying it"  class="centered-img"  style="max-width: 600px">

> [!Question] How can we improve the `Task`, `Agent` and the `Crew` without having to spend long time?
> Leverage `crewai train` feature.
<img src="crewai-with-feedbaclk-loop.png" alt="Crew AI with feedback loop"  class="centered-img"  style="max-width: 600px">