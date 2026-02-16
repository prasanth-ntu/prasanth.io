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
  - Courses/DeepLearning.AI - MCP - Build Rich-Context AI Apps with Anthropic
---
**Key resources**
- Course [link]([https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/))
	- [Forum](https://community.deeplearning.ai/c/short-course-q-a/mcp-build-rich-context-ai-apps-with-anthropic/525)
- My Github Repo [link](https://github.com/prasanth-ntu/DeepLearningAI-MCP-Build-Rich-Context-AI-Apps-with-Anthropic)

Below sections contain the key take aways from each lesson.

---
# Why MCP (L1)

> [!WARNING]  Models are only as good as the **context** given to them

> [!SUMMARY] What is the Model Context Protocol (MCP)?
> MCP is an open protocol that standardizes (and *not reinvent the wheel*) how our **LLM applications** connect to and work with our **tools & data sources**.


![[without-mcp.png]]![[with-mcp-example-1.png]]![[with-mcp-example-2.png]]


> [!TIP] MCP standardizes AI development for multiple users, including
> - AI application developers
> - Tool or API developers
> - AI Application users
> - Enterprises

# MCP Architecture (L2)

> [!TIP] MCP follows Client-Sever Architecture

![[mcp-client-server-architecture.png]]

![[how-mcp-works.png]]

## Defining a ...
### Tool

**Example**
```python
@mcp.tool
...
```

### Resources

**Example**: *Direct*
```python
@mcp.resource(
	"docs://documents",
	mime_type="application/json"	
)
...
```

**Example**: *Templated*
```python
@mcp.resource(
	"docs://documents/{doc_id}",
	mime_type="text/plain"	
)
...
```

### Prompt

**Example**
```python
@mcp.prompt(
	name="format",
	description="..."
)
...
```

## Communication Lifecycle

![[mcp-communication-lifecycle.png]]

## MCP Transports

> [!SUMMARY] A transport handles the underlying mechanism of how messages are sent and received between the client and server.
> 1. stdio
> 2. Streamable HTTP

For more details, refer [MCP Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports#multiple-connections)

![[mcp-transport-streamable-http.png]]

![[mcp-streamable-http-transport.png]]

# Chatbot Example (L3)


# Creating an MCP server (L4)

![[mcp-server-example-1.png]]
# Creating an MCP client (L5)


# Connecting the MCP Chatbot to Reference Servers (L6)


# Adding Prompt and Resource Features (L7)



# Configuring Servers for Claude Desktop (L8)
- https://modelcontextprotocol.info/docs/clients/
- https://modelcontextprotocol.io/clients

# Creating and Deploying Remote Servers (L9)


# Conclusion
![[mcp-client-server-auth.png]]

![[mcp-client-primitives.png]]


### Building Effective Agents with MCP

![[mcp-composability.png]]

![[mcp-sampling-composability.png]]

![[mcp-registry.png]]

![[mcp-registry-2.png]]

![[mcp-server-discovery.png]]

---
# Appendix
##  The three MCP primitives:

**Analogy between MCP resources/tools/prompts and RESTful API methods:**

|MCP Primitive|REST Analogy|Purpose|
|---|---|---|
|**Resources**|`GET` endpoints|Read data|
|**Tools**|`POST/PUT/DELETE` endpoints|Execute actions|
|**Prompts**|**Postman collections / OpenAPI examples**|Pre-built request templates|
And just like in REST:

- `GET` should be **idempotent** and **safe** (no side effects) → Resources are read-only
- `POST/PUT/DELETE` **change state** → Tools can execute action

**Prompts** are server-provided templates that say: _"Here's the optimal way to ask me to do X."_
```
Example prompt from a "code-review" MCP server:

{
  name: "review-pr",
  description: "Review a pull request for issues",
  arguments: [
    { name: "diff", description: "The PR diff content", required: true },
    { name: "focus", description: "What to focus on: security|performance|style", required: false }
  ]
}
```

The **client** then:
1. Discovers available prompts from the server
2. Presents them to the user (maybe as slash commands or buttons)
3. Collects the argument values
4. Expands the template and sends the complete prompt to the LLM

**Why this matters:**
Instead of users writing:

> _"Can you review this code and look for bugs maybe? Here's the diff..."_ (suboptimal)

The server provides a battle-tested prompt structure that reliably produces good results.

So to complete the picture — who provides what:

|Component|Provided by|
|---|---|
|Resources|Server|
|Tools|Server|
|Prompts|Server|
|Loading strategy for resources|Client|
|Tool invocation decisions|Model|
|Prompt selection & argument filling|Client + User|
## Official Documentation/ Resources
- https://www.anthropic.com/news/model-context-protocol
- https://github.com/modelcontextprotocol/servers
- https://github.com/modelcontextprotocol/python-sdk
- https://modelcontextprotocol.io/docs/getting-started/intro
- https://modelcontextprotocol.io/docs/develop/build-server