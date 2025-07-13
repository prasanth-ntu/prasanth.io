---
tags:
  - DataScience
  - SoftwareEngineering
  - DeepLearningAI
  - Course
  - AIAgent
  - CrewAI
---
**Key resources**
- Course [link](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/)
	- Forum [link](https://community.deeplearning.ai/c/short-course-q-a/multi-ai-agent-systems-with-crewai/449)
- My Github Repo [link]()

Below sections contain the key take aways from each lesson.

---
# Overview

> [!INFO] 6 key components of multi-agent systems
> 1. Role playing
> 2. Focus
> 3. Tools
> 4. Cooperation
> 5. Guardrails
> 6. Memory
>    
>    *Interestingly, these components indeed makes for a great employee.*

> [!TIP] Multi-Agent Collab can be 
> - Sequential
>  - Parallel 
>  - Hierarchical
>  - Asynchronous

> [!WARNING] Traditional Software Development vs. AI Software Development
Unlike traditional approach, AI Software Development has
> - Fuzzy inputs
> - Fuzzy transformations
> - Fuzzy outputs
> - Probabilistic nature  

 **Lead Generation: Data Collection & Analysis Example**
 - Traditional Automation
	 - Website Visitor (e.g., Form) → Lead (e.g., >10 employees) → Sales (Low/Med/High Priority)
 - Agentic Automation
	 - Website Visitor → Lead → Crew of AI Agents → Sales, where the 
	 - **Crew of AI Agents** could do
		 - Research (data collection)
		 - Comparison
		 - Scoring
		 - Talking points
---		 
# AI Agents
**Initial Building Blocks**
- Agents
- Tasks
- Crews

---
# Create agents to research and write an article (L2)

> [!SUMMARY] This lesson introduces us to the fundamental concepts of multi-agent systems, and get an overview of crewAI framework.

> [!TIP] It's been seen that LLMs perform better when they are role playing.

Steps involved in creating a Multi AI Agent
1. **Create `Agents` by providing them `role`, `goal`, `backstory`
2. **Create `Tasks`** by providing them `description`, `expected_output`, and `agent`
3. **Create `Crew`**, a top-level organization that oversees the agents and tasks

The Agentic `Crew` to research and write any article was assembled using 3 `Agents` and 3 `Tasks`, which are
- Content Planner
- Content Writer
- Editor
For more details, refer this [GitHub code](https://github.com/prasanth-ntu/DeepLearningAI-Multi-AI-Agent-Systems-with-CrewAI/tree/main/L2)

---
# Key elements of AI agents 

> [!TIP] Agents work better when they are role playing, focused, have appropriate tools, allowed to cooperate, leveraging memory, and having some guardrails.

1. Role Playing
	- e.g., "Give me an analysis on tesla stock" vs. "you are a FINRA approved financial analyst. give me an analysis on tesla stock". 
		- The later is more effective.
	
2. Focus
> [!WARNING] If we mix things too much (e.g., too many tools, information, context, etc.), our models can loose important information, and hallucinate more.

> [!FAILURe] Do not use one single agent to achieve everything.

3. Tools

> [!INFO] Two different ways to give Agents Tools
> 1. Agent Level
> 2. Task Level

4. Cooperation
> [!TIP]  Ability to cooperate (take feedbacks, delegate tasks) and to bounce ideas of each other produces much better outcome.

5. Guardrails
> [!SUCCESS] Prevent Agent from derailing and budge them to stay on track, thereby making sure to prevent hallucinations and we get reliable and consistent results.

6. Memory
> [!TIP] Memory makes huge, immense difference on our Agent.

> [!INFO] 3 types of memory offered by CrewAI out of the box:
> 3. Short term memory
> 4. Long term memory
> 5. Entity memory

---
# Multi agent customer support automation (L3)

> [!SUMMARY] This lesson covers the six key elements that help make AI Agents perform better.

The Agentic `Crew` to provide customer support was assembled using 2 `Agents` and 2 `Tasks`
- `Agents`
	- `support_agent` with `role="Senior Support Representative"`
	- `support_quality_assurance_agent` with `role="Support Quality Assurance Specialist"` and `allow_delegation=True`, so that agent can delegate its work to another agent which is better suited to do a particular task.
- `Tool`
	- `docs_scrape_tool` that scrapes a 1 page (URL) of CrewAI documentation.
- `Tasks`
	- `inquiry_resolution` with `tools=[docs_scrape_tool]` so that the `Agent` can access this `tool` on this specific-task. 
	- `quality_assurance_review`
- `Crew`
	- `crew` with `memory=True` to enable the Memory

> [!INFO] Interestingly, the overall token cost of `gpt-4o-mini` is expensive than `gpt-4o`, and it even made too many attempts which shows it's limitations. 

For more details, refer this [GitHub code](https://github.com/prasanth-ntu/DeepLearningAI-Multi-AI-Agent-Systems-with-CrewAI/tree/main/L3)

---
# Mental framework for agent creation

Think as a ***Manager***, as they are conditioned to think
- What is the Goal?
- What is the Process?

> [!TIP] What kind of people would I need to hire to get this job done? What should be their roles, goals, backstories? 
> Those are the agents we want to build.

**Example: Use case related to HR**

| Okay Agent 👎     | Better Agent 👍        |
| ----------------- | ---------------------- |
| Researcher        | HR Research Specialist |
| Writer            | Senior Copywriter      |
| Financial Analyst | FINRA Approved Analyst |

---
# Key elements of agent tools

> [!TIP] What makes a great Tool?
> 1. Verstaile
> 2. Fault-tolerant
> 3. Cache

> [!INFO] Tools is the connection between AI apps (that have fuzzy inputs) and the external world (that have strongly typed inputs).

> [!INFO] CrewAI support Cross-agent caching

For more details, refer [Available CrewAI Tools] (https://docs.crewai.com/en/concepts/tools#available-crewai-tools).

> [!TIP] We can also use all the tools that LangChain offers. 

---
# Tools for a customer outreach campaign (L4)

> [!SUMMARY] This lesson covers more about tools, including custom ones

The Agentic `Crew` to perform customer outreach campaign (drafting different emails for different target audience) was assembled using 2 `Agents`, 4 `Tools`, and 2 `Tasks`
- `Agents`
	- `sales_rep_agent` with `role=Sales Representative`
	- `lead_sales_rep_agent` with `role=Lead Sales Representative`
- `Tool`
	- `directory_read_tool` that list files in directory
	- `file_read_tool` that reads file contents
	- `search_tool` (from `SerperDevTool`) to search the internet with Serper
	- `sentiment_analysis_tool` (custom tool) that's hardcoded output
- `Tasks`
	- `lead_profiling_task` with `tools=[directory_read_tool, file_read_tool, search_tool]`
	- `personalized_outreach_task` with `tools=[sentiment_analysis_tool, search_tool]`
- `Crew`
	- `crew` with `memory=True` to enable the Memory

For more details, refer this [GitHub code](https://github.com/prasanth-ntu/DeepLearningAI-Multi-AI-Agent-Systems-with-CrewAI/tree/main/L4)

---
# Key elements of well defined tasks

> [!TIP] What tasks and processes do I expect the individuals on my team to do?
> Those are the tasks we want to create.

> [!TIP] Two key elements of well defined tasks
> 1. Clear description of the tasks
> 2. Set a clear and concise expectation

**Other (hyper)parameters or task attributes**
- Set context
	- By using `context`, we can specify other tasks whose outputs will be used as context for this task.
- Set a callback
	- By using `callback`, we can specify the Function/object to be executed after task completion.
- Override Agent tools with specific task tools
	- By using `tools`, we can specify the tools/resources the agent is limited to use for this task.
- Force human input before end of task
	- By setting `human_input=True`, the task will ask for human feedback (whether you like the results or not) before finalising it.
- Execute asynchronously
- Output as Pydantic
	- By using `output_pydantic`
- Output as JSON
	- By using `output_json`, you can specify the structure of the output you want.
- Output as file
	- By using `output_file`, you can get your output in a file.
- Run in parallel
	- By using `async_execution=True`, we can specify the task should be executed asynchronously. Defaults to `False`.

For more details, refer crew ai documentation > [tasks](https://docs.crewai.com/en/concepts/tasks)

---
# Automate Event Planning (L5)

> [!SUMMARY] This lesson covers about tasks, and different parameters for it.

The Agentic `Crew` to perform automated event planning was assembled using 3 `Agents`, 2 `Tools`, 3 `Tasks`
- `Agents`
	- `venue_coordinator` with `tools=[search_tool, scrape_tool]`
	- `logistics_manager` with `tools=[search_tool, scrape_tool]`
	- `marketing_communications_agent`with `tools=[search_tool, scrape_tool]`
> [!NOTE] Interestingly, `tools` are passed directly into `Agents` unlike previous examples, where they are passed only to the `tools`
- Class `VenueDetails` using `Pydantic BaseModel`
- `Tasks`
	- `venue_task` with `human_input=True`, `output_json=VenueDetails`, and `output_file="venue_details.json"`
	- `logistics_task` with `human_input=True`
	- `marketing_task` with `async_execution=True` and `output_file="marketing_report.md"`
- `Crew`

> [!NOTE] The `human_input=True` turned out to be useful for providing feedback on the Final Result and Agent's actions.

For more details, refer this [GitHub code](https://github.com/prasanth-ntu/DeepLearningAI-Multi-AI-Agent-Systems-with-CrewAI/tree/main/L5)

---
# Multi agent collaboration for financial analysis (L6)

> [!SUMMARY] This lesson covers on ways to make agents collaborate with each other.

The multi Agentic `Crew` to perform financial analsyis was assembled using `4` Agents, 2 `Tools`, and `3 Tasks`
- `Agents`
	- `data_analyst_agent`
	- `trading_strategy_agent`
	- `execution_agent`
	- `risk_management_agent`
	*Note*: All the `Agents` were given `allow_delegation=True`, and `tools=[scrape_tool, search_tool]`
- `Tasks`
	- `data_analysis_task`
	- `strategy_development_task`
	- `execution_planning_task`
	- `risk_assessment_task`
	*Note*: All the `Tasks` were configured with `output_file` to output a markdown file.
- `Crew`
	- `crew` with `process=Process.hierarchical`
	
> [!TIP] Why hierarchical process instead of sequential process?
> For a financial trading crew with multiple specialized agents, the hierarchical process is likely more appropriate as it allows for better coordination between the data analyst, strategy developer, execution agent, and risk manager, rather than forcing them to work in strict sequence.

For more details, refer this [GitHub code](https://github.com/prasanth-ntu/DeepLearningAI-Multi-AI-Agent-Systems-with-CrewAI/tree/main/L6)

---
# Build a crew to tailor job applications (L7)

> [!SUMMARY] This lesson covers building our first multi-agent system

The multi Agentic `Crew` to perform tailored job applications using 4 `Agents`, 3
- `Agents`
	- `researcher` with `role="Tech Job Researcher"` 
	- `profiler` with `role="Personal Profiler for Engineers"`
	- `resume_strategist` with `role="Resume Strategist for Engineers"`
	- `interview_preparer` with `role="Engineering Interview Preparer"`
  *Note:* All the `Agents` were given `tools=[scrape_tool, search_tool, read_resume, semantic_search_resume]`, except `researcher` which was only given `tools=[scrape_tool, search_tool]`
- `Tasks`
	- `research_task` with `output_file` as markdown and `async_execution=True` to extract job requirements
	- `profile_task` with `output_file`  as markdown and `async_execution=True` to compile comprehensive profile
	- `resume_strategy_task` with `output_file` as markdown and `context=[research_task, profile_task]` to align resume with job requirements	
	- `interview_preparation_task` with `output_file` as markdown and `context=[research_task, profile_task, resume_strategy_task]` to develop interview materials 
	
> [!NOTE] How does `context` work in `Tasks`?
> - You can pass a list of tasks as `context` to a task.
> - The task then takes into account the output of those tasks in its execution.
> - The task will not run until it has the output(s) from those tasks.

---
# Next steps with AI Agent Systems

Check out these resources
- Crew AI related
	- [Crew AI Examples[(https://docs.crewai.com/en/examples/example)
		- [AI Crew for Matching CVs to Job Proposals](https://github.com/crewAIInc/crewAI-examples/tree/main/match_profile_to_positions)
	- [Crew GPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)
	- [CrewAI Plus](https://app.crewai.com/crewai_plus/dashboard)
- Others
	- [ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924)

---
# To do or clarify
- [ ] Multi agent customer support automation (L3)
	- [ ] When we set `Crew(..., memory=True)`, does it enable short-term memory or long-term memory? How about entity memory?
	- [x] Citation is not provided in the demo output. Is it a glitch or something else?
		- Seems this is resolved once migrated to latest GPT 4 variant models
	- [ ] What's considered as guardrail in this project?
		- [ ] Is it the `expected_output` defined in the `Task` or `backstory` provided in the `Agent` or something else? 
- [ ]  Tools for a customer outreach campgain (L4)
	- [ ] Does this tool has caching with a timeout so that we don't have to pay again for the same call for same query in a short span? 
		- [Perplexity link](https://www.perplexity.ai/search/from-crewai-tools-import-serpe-5hIYzVEXSIiOjaLHetM43Q)
	- [ ] What's `cached_promot_tokens` in `result.token-usage`
		- For e.g., Token Usage: total_tokens=67180 prompt_tokens=65040 cached_prompt_tokens=51200 completion_tokens=2140 successful_requests=15 for gpt-4o
- Automate Event Planning (L5)
	- [ ]  When `async_execution=True` was enabled for two tasks, it's throwing an error. How to fix it?