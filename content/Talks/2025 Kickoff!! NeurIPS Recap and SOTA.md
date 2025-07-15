---
tags:
  - DataScience
  - MachineLearning
  - ArtificialIntelligence
  - Talks
  - MachineLearningSingapore
  - GoogleDevelopersSpace
  - Meetup
title: 2025 Kickoff!! NeurIPS Recap and SOTA
---
# Meet up event details
[Meetup link](https://www.meetup.com/machine-learning-singapore/events/305605893/?eventOrigin=home_page_upcoming_events$all)

For our annual NeurIPS event, we're once again bringing back our thoughts/impressions/knee-jerk reactions from the December NeurIPS conference.

Talks:

**"The State of LLM Patterns & Agents" - Sam Witteveen**

In this talk, Sam will look at both recent academic and industrial advancements of how people are using LLMs/VLMs. He will cover what patterns and paradigm have survived over the past 18 months and also look at the state of new techniques and frameworks for building LLM apps and agents. If 2025 is the year of AI agents what exactly is new?

**"The End of Pretraining" - Martin Andrews**

Now that 'reasoning models' have started to appear from the big labs, NeurIPS clearly separated into the main conference (with papers from the 'before times') and the workshops... There was no clearer watershed moment that Ilya Sutskever's talk in which he likened text tokens to the limited supply of fossil fuels. Martin will reflect on this, and how 'reasoning' will enable AI to continue to flourish - and talk about Deepseek's R1 model release.

# "The State of LLM Patterns & Agents" - Sam Witteveen

## State of Agents 2025
### Most Agents aren't needed
- Most problems are well crafted to LLM chains than Agents
### LLM Apps
- Agents are just a subclass of LLM Apps
### Chains vs. Agents
- [ ] Attach the screenshot titled ...
### What are agents?
- [ ] Attach the screenshot titled ...
### The Agents Equation
- [ ] Attach the screenshot titled ...
### Agents - At a low level
> *Agents really are all about loops*
- [ ] Attach the screenshot titled ...
### Flows vs. Agency
- [ ] Attach the screenshot titled ...
### Flows
> *What we need now a days really is Flows*
- [ ] Attach the screenshot titled ...
- [ ] Attach the paper (Code Generation with AlphaCodium: PromptEngineering to FlowEngineering)

### Anthropic - Building Effective agents
> Don't use /buildagent until you really need one
- [ ] Attach the Anthroipc blogpost ...
#### Prompt Chaining Workflow
- [ ] Attach the screenshot titled ...
#### Parallelization Workflow
> Suited with Superfast, super cheap models
- [ ] Attach the screenshot titled ...
#### Routing Workflow
> If see from traditional ML perspective, it just does ML classification
> Good for more ambiguos things
- [ ] Attach the screenshot titled ...
#### Reflection 
> Same LLM can say it's output sucks, and improvise the output during reflection
- [ ] Attach the screenshot titled ...
#### Augmented LLM
> Can be retrieval, RAG, memory, getting something and bringing it back
- [ ] Attach the screenshot titled ...
#### Evaluator Optimizer Workflow
- [ ] Attach the screenshot titled ...

#### Planning pattern
- [ ] Attach the screenshot titled ...
#### Autonomous  Agent
- [ ] Attach the screenshot titled ...
#### ReAct Pattern
> Precursor to function calling
- [ ] Attach the screenshot titled ...
#### Multi Agent
- [ ] Attach the screenshot titled ...
#### Hierarchical - Multi Agent
> Quite dangerous
- [ ] Attach the screenshot titled ...
#### Magentic - One
> Uses a ledger (interesting approach)
> Quite effective (double-checking kind of system)
- [ ] Attach the screenshots titled ...

> TL;DR Patterns haven't fundamentally changed that much. Lot of people have optimized it, and that's where it leads to **Frameworks**.
## Frameworks
#### Agent Frameworks
- [ ] Attach the screenshot titled ...
#### Current Popular Frameworks
- [ ] Attach the screenshot titled ...
- LangChain
	- Has lot of technical debt as they literally launched 1 week after some GPT/OpenAi variant.
	- Literally adopted every patterns, and hence lot of tech debt
- LangGraph
	- Big fan of flow engineering idea
- LlamaIndex
	- Similar to LangChain
- Phidata
	- Kind of new
- Smolagents
	- They tend to subscribe to the idea of everything to code
	- Paper: Executable Code Actions Elicit Better LLM Agents
		- Idea is great, but doesn't work that well with any of the small models
		- Even if does work, we end up burning lots of tokens
- Pydantic AI
	- Sam likes this the most
	- Created by the team in [[Pydantic]]
#### Complexity vs. Control
> Decide ourselves are we going to have state machine?
> Do we want various nodes? Do we want auto parser?
> Those things made sense where LLMs in the past where string in string out, but the SOTA LLMs are much more sophisticated
- [ ] Attach the screenshot titled ...
#### Frameworks
> Swarm - We can learn it 20mins, whereas LangChain would take time to learn
> To understand what's going on with Agents
- [ ] Attach the screenshot titled ...
#### Tools
- [ ] Attach the screenshot titled ...
#### Common Tools
- [ ] Attach the screenshot titled ...
#### Composio

> So, that gave us basic of patterns, agents and tools
#### Code Agents
> Where the money is
- **Github Copilot Workspace**
- **Devin**
	- - [ ] Attach the screenshot titled ...
	- Devin Sucks - In other words,
- **OpenHands**
	- Awesome course on Youtube
	- Totally OpenSource
	- MIT License
	- - [ ] Attach the screenshot titled ...
	- OpenHands: Use Cases
- - [ ] Attach the survey paper titled "LLM: ..."
#### Browser Agents
> Next ones becoming popular
- Claude Computer Use
	- Don't run this on your computer 😂
	- Better run it in Docker Instance
- Agent-S
	- 	- - [ ] Attach the screenshot titled ...
- OmniParser
	- Didn't get a lot of love, but really should
	- Allows models to detect what's in the screen
- Project Mariner
	- From Google: Chrome extension that can run in chrome which we can ask to do variety of stuff
-  Anthropic Virtual Collaborator
> These things are going to wipe out RPA (things like UI Path).
- [ ] Attach the screenshot titled ...

#### Enterprise vs. Consumer
> Most agents are mostly focused on Enterprise
- [ ] Attach the screenshot titled ...

#### Microsoft Copilot Studio
> Successful product 
> They can learn from the type of agents are trying to build, and roll out the popular ones

#### Google - Agent Space
> ...

#### Deep Research - Google
> Gemini Consumer App: Give it a task, and go off and research for us
> Definitely the kind of agent we can expect in coming months
- [ ] Try it out on my own

#### Notebook LLMS is something similar

### Evaluations
> Models change, so, ensure, we have proper tools (including tool evals)
- [ ] Attach the screenshot titled ...

#### LLM as a Judge
> Sam is very bullish on this
> If we put the outputs back in, we can do in-context learning, can be cached, judge whole bunch of response
- [ ] Attach the screenshot titled ...
- [ ] Attach the paper titled (Agent-as-a-Judge from Meta) ...

#### Be Careful of 3rd party tracing solutions
> Be very careful on where we are saving the prompts, responses, data, agents, etc.
- [ ] Attach the screenshot titled ...
- Phoenix
	- Fully self-hosted: Your data is your data
### Production
> Best agent framework for Production is Python
#### Why Python?
- Lot of LLM SDKs
- Lots of Tools
- Not tied down to one way of doing things
#### So, what do you do?
> Embrace and be ready to switch to new/better/cost-effective models
> VERY IMPORTANT
- [ ] Attach the screenshot titled ...

#### Pydantic AI
> Go with this as much as possible
- [ ] Attach the screenshot titled ...

### Conclusion
- Don't build Agents, build LLM apps
	- Learn during POC and prototyping, but bare-bone it when going to prd
- Don't buy into the hype
- [ ] Attach the screenshot titled ...

### Future
- [ ] Attach the Paper titled "Behavioral Cloning for Agents"
- [ ] Agent Marketplaces are coming (e.g., Stripe/crypto is working where one agent makes payment to another agent)
- [ ]  Gemini 2.0 Flash Thinking 21-Jan-2025 (It's free for few 100 calls a day, so try it)
	- [ ] [TODO] Visit Google AI Studio, and try it

---
# "The End of Pretraining" - Martin Andrews
## Outline
- NeurIPS
	- Old News
	- New News
- Newer News + Newest News
- Wrap-up & QR code

## Backdrop: o1 Release
- [ ] Attach the screenshot titled ...
## NeurIPS
#### Paper Timeline
- [ ] Attach the screenshot titled ...
#### Choosing Papers
- [ ] Attach the screenshot titled ...

#### Paper 'Shoutouts'
##### Faces and Training
- [ ] - [ ] Attach the screenshot titled ...
##### Reasoning
- [ ] - [ ] Attach the screenshot titled ...
## Ilya
#### Test of time award speech
- Sequence to Sequence Learning with NNs
	- Translational task
	- LSTM with 4 layers

## Topic 3
