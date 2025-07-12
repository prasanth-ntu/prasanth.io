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

> [!TIP] Multi-Agent Collab can be Sequential, Parallel, Hierarchical, and even Asynchronous.

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
# Create agents to research and write an article

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
For more details, refer this GitHub code #TBA

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
# Multi agent customer support automation

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
For more details, refer this GitHub code #TBA 

---
# Mental framework for agent creation

Think as a ***Manager***, as they are conditioned to think
- What is the Goal
- What is the Process

> [!TIP] What kind of people would I need to hire to get this job done? What should be their roles, goals, backstories?
> Those are the agents we want to build

**Example: Use case related HR**

| Okay Agent        | Better Agent           |
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

---
# Tools for a customer outreach campaign


---
# To do or clarify
- [ ] Multi agent customer support automation 
	- [ ] When we set `Crew(..., memory=True)`, does it enable short-term memory or long-term memory? How about entity memory?
	- [ ] Citation is not provided in the demo output. Is it a glitch or something else?
	- [ ] What's considered as guardrail in this project?
		- [ ] Is it the `expected_output` defined in the `Task` or `backstory` provided in the `Agent` or something else? 
- [ ]  