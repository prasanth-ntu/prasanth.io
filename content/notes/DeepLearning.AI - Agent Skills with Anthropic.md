---
tags:
  - ai-agents
  - anthropic
  - course
  - data-science
  - deep-learning
  - machine-learning
  - software-engineering
draft: true
aliases:
  - Courses/DeepLearning.AI - Agent Skills with Anthropic
---
**Key resources**
- Course [link](https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/)
	- Forum
- My Github Repo [link](https://github.com/prasanth-ntu?tab=repositories)

Below sections contain the key take aways from each lesson.

---
# Why use Skills - Part 1


# Why use Skills - Part 2

![[agent-skill-1.png]]
![[agent-skills-2.png]]

![[why-agent-skills.png]]
![[why-agent-skills-2.png]]
![[why-agent-skills-3.png]]
![[agent-skills-are-portable.png]]
 ![[agent-skills-are-composable.png]]
![[how-skills-work.png]]

### Progressive Disclosure

> [!WARNING] Skills are *Progressive Disclosed*
> - Only load data necessary
> - Avoid polluting the context window with data we might not need
> 
> *Think of context window as public good ⇒ More tokens we consume, faster context window fills up, and the likelihood of context degradation or incorrect responses potentially increases*

![[skills-progressive-disclosure-1.png]]

# Skills vs. Tools, MCP and Subagents

![[general-agents.png]]
> [!SUMMARY]
> - Bring in **MCP servers** for the (external) context
> - Leverage **Subagents** for their own main thread & parallelization
> - Bring in **Skills** for repeatable workflows


![[skills-vs-mcp.png]]
> [!TIP] Skills vs MCP
> - Skills: Set of instructions to put those tools together to build particular workflows that are repeatable
> - MCP: Brings in all the underlying tooling we need


![[skills-vs-tools.png]]


![[skills-vs-subagents.png]]


![[customer-insight-analyser-agent.png]]


![[skills-vs-tools-mcp-subagents-summary.png]]

> [!TIP] Components in AI system
> - **Prompt**: Underlying most atomic units in the conversation. They don't scale very well across teams and companies
> - **Skills**: Can be leveraged to bundle prompts, conversations, code and assets
> - **Subagents**: Tasks can be delegated to subagents, and it can make use of skills and even consume tools from main agents via MCP
> - **Context Window**: Public good 
> 	- **Subagents**: Help us minimize what goes in main context window
> 	- **MCP**: Loads data necessary 
> 	- **Skills**: Load it progressively
> - Persistance: Longer-term memory
> 	- Subagents: Can persist across many different sessions from the subagent and parent agent
> 	- **Skills**: Can persist across conversation that we have with user and AI application


# Exploring Pre-Built Skills (L3)


# Creating Custom Skills (L4)


# Skills with Claude API


# Skills with Claude Code


# Skills with Claude Agent SDK


# Conclusion

---
# Official Documentation/ Resources
- https://claude.com/blog/skills-explained
	- https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction
	- https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills
- https://github.com/anthropics/skills
	- https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md
- https://agentskills.io/home#adoption