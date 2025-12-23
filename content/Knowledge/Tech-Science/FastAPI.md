---
tags:
  - softwareengineering
  - Coding
  - Programming
draft: true
---

FastAPI is a modern Python web framework designed for building APIs quickly and efficiently.

## Core FastAPI Structure
- `FastAPI()` creates the main application instance
- `APIRouter()` groups related endpoints
	- @router.post("/endpoint")` decorates handler functions
- `app.include_router(router)` registers the router with the app
	- Takes all the endpoints defined in that router and registers that with the main FastAPI app, this making it accessible via HTTT (POST in this example) requests.
	-  If the router had multiple endpoints, it would register all of them. The router is just a way to group related endpoints together before adding them to the main app.

  **Key Features**
1. **Async Support**: FastAPI is built for async operations, which is critical concurrent API calls to external services (e..g, databases).
  2. **Automatic Validation**: Pydantic models (like `RequestModel` and `ResponseModel`)  provide automatic request/response validation and serialization.
  3. **Dependency Injection**: FastAPI can automatically parse headers, query parameters, and request bodies using type hints.
  4. **Application Lifecycle**: The `asynccontextmanager` pattern manages startup/shutdown for expensive resources like database connections and agent initialization.

## Handler function
A handler function is the Python function that processes incoming HTTP requests to a specific endpoint.

  In this example:
```python
@router.post("/endpoint")
  async def handler(request: RequestModel) -> ResponseModel:
      return ResponseModel(data="response")
```
  
> [!TIP] "handler function" = the function that handles requests to that specific route/endpoint.

## Dependency injection
Dependency Injection means FastAPI automatically provides (injects) values into your handler function parameters based on the HTTP request.

**Example: Without dependency injection**, you'd manually do:
```python
async def chat(raw_request):
      # Manual parsing from request body
      request_data = json.loads(raw_request.body)
      request = ChatRequest(**request_data)

      # Manual header extraction
      headers = ChatHeader(
          user_agent=raw_request.headers.get("user-agent"),
          x_session_id=raw_request.headers.get("x-session-id")
      )
```
 
 With dependency injection, FastAPI does this automatically based on type hints. You just declare what you need as parameters, and FastAPI figures out how to get it from the HTTP request.
 
**Example: With dependency injection**
```python
```python
from fastapi import Depends, Header
from typing import Annotated

@router.post("/chat")
async def chat(
    request: ChatRequest,  # Auto-parsed from request body
    headers: Annotated[ChatHeader, Header()]  # Auto-parsed from HTTP headers
) -> ChatResponse:
    pass
```

 The headers: `Annotated[ChatHeader, Header()]` syntax tells FastAPI:

  1. `headers` - parameter name
  2. `ChatHeader` - the Pydantic model to create
  3. `Header()` - tells FastAPI "get this data from HTTP headers"
  4. `Annotated[...]` - Python typing syntax that combines type + metadata

  ### **How it works?**
  When an HTTP request comes in with headers like:
```
User-Agent: Mozilla/5.0
Accept-Language: en-US
X-Session-Id: abc123

```
  
  FastAPI automatically:
  1. Extracts these header values
  2. Creates a `ChatHeader` object using them:
```
  headers = ChatHeader(
      user_agent="Mozilla/5.0",
      accept_language="en-US",
      x_session_id="abc123"
  )
```
  3. Passes it to your handler function

  The `ChatHeader` model probably looks like:
```
  class ChatHeader(BaseModel):
      user_agent: str
      accept_language: str
      x_session_id: str
```

  Compare to request body:
  - `request: ChatRequest` - data from JSON body
  - `headers: Annotated[ChatHeader, Header()]` - data from HTTP headers

  Both are dependency injection, just from different parts of the HTTP request.
      
  Other common dependencies:
  - `Query()` - from URL query parameters
  - `Path()` - from URL path parameters
  - `Depends()` - custom dependency functions

  > [!TIP] It's called dependency "injection" because the framework injects these values into your function.

### `Annotated` explained
Annotated is Python's way to attach extra information (metadata) to a type hint.

  **Basic syntax**: `Annotated[Type, metadata]`

  In our example:
```
 headers: Annotated[ChatHeader, Header()]
  #       ^^^^^^^^^ ^^^^^^^^^^  ^^^^^^^^
  #       Annotated  Type       Metadata
```
 
  **What this tells FastAPI**:
  - **Type**: "This parameter should be a `ChatHeader` object"
  - **Metadata**: "Get the data from HTTP headers using `Header()`"

  **Without `Annotated`, you'd write:**
  `headers: MobotHeader  # Just the type - FastAPI wouldn't know WHERE to get the data`

  FastAPI wouldn't know if `ChatHeader` should come from:
  - Request body?
  - URL parameters?
  - HTTP headers?
  - Query parameters?

  **With Annotated:**
  `headers: Annotated[MobotHeader, Header()]  # Type + instruction`

  Now FastAPI knows: "Create a `ChagHeader` object using data from HTTP headers"

  Other examples:
  - `user_id: Annotated[int, Path()]        # From URL path`
  - `page: Annotated[int, Query()]          # From query parameters  `
  - `db: Annotated[Database, Depends(get_db)]  # From custom dependency`

  > [!TIP] Think of Annotated as: "This is the type I want, and here's how to get it."

## Pydantic models for validation

> [!TIP] The separation allows you to have clean, Pythonic field names internally while seamlessly integrating with external systems that use different naming conventions.
> - `validation_alias`: Used when receiving data from external sources with specific field names
> 	- This controls what field names are accepted when validating/parsing input data.
> - `serialization_alias`: Used when sending data to external systems that expect specific field names
> 	  - This controls how field names appear when serializing data (converting to JSON/dict).

### **`validation_alias` - Receiving Data (INPUT)**
```python
# Request models - data coming FROM external sources
class ChatMessage(BaseModel):
    content: str = Field(validation_alias="content")

class Metadata(BaseModel):
    userr_id: int = Field(validation_alias="userID")
    current_location: Coordinates = Field(validation_alias="location")
    timezone: str = Field(validation_alias="timezone")

class MobotChatRequest(BaseModel):
    conversation: list[MobotChatMessage] = Field(validation_alias="conversation")
    metadata: Metadata = Field(validation_alias="metadata")
```

### **`serialization_alias` - Sending Data (OUTPUT)**
```python
# Response models - data going TO external sources
class Item(BaseModel):
    item_id: int = Field(serialization_alias="itemID")
    item_name: str = Field(serialization_alias="itemName")
    quote_signature: str = Field(serialization_alias="quoteSignature")

class ChatResponse(BaseModel):
    conversation: list[Conversation] = Field(serialization_alias="conversation")
```

#### **The Flow**

1. **External system → Your API** (Request): Uses `validation_alias`
   ```python
   # External system sends: {"userID": 123, "location": {...}}
   # Your model receives it as: user_id=123, current_location=Coordinates(...)
   ```

2. **Your API → External system** (Response): Uses `serialization_alias`
   ```python
   # Your model has: item_id=123, item_name="ItemXYZ"
   # External system receives: {"itemID": 123, "itemName": "ItemXYZ"}
   ```

This separation allows you to:
- **Keep clean, Pythonic field names** internally (snake_case)
- **Seamlessly integrate** with external systems that use different conventions (camelCase, etc.)
- **Maintain clear boundaries** between input and output data transformations

---
## Application Lifecycle

**Example:**
```python
@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    conn = aiosqlite.connect(":memory:")
    service_a = ServiceAClient()
    service_b = ServiceBClient()
    chat_agent = create_chat_agent(conn, service_a, service_b)

    app_state["chat_agent"] = chat_agent
    yield
    ...
    await conn.close()


router = APIRouter(lifespan=lifespan)

agent_output = await agent.ainvoke(
    {"message": "Order a coffee"},
    config={
        "thread_id": headers.x_session_id,    # 🔑 This is the KEY!
        "configurable": {
            "user_id": request.metadata.userr_id,
            "latitude": request.metadata.current_location.latitude,
            # ... other context
        },
    },
)
```

 **What happens:**
  1. Startup (before yield):
    - Create database connection
    - Initialize the Chat agent
    - Store it in global state
    - Set up any other expensive resources
  2. Runtime (at yield):
    - Your API endpoints are now available
    - All requests can access the shared chat_agent
  3. Shutdown (after yield):
    - Close database connections
    - Clean up resources
    - Graceful shutdown

  **Why this matters:**
  - **Without lifecycle management**: You'd recreate the agent on every request (slow!)
  - **With lifecycle management**: Create once at startup, share across all requests (fast!)

  **Common lifecycle tasks:**
  - Database connections
  - ML model loading
  - External service clients
  - Cache initialization
  - Background tasks

> [!TIP] The agent here is designed to be stateless at the instance level but stateful per session/user through the configuration parameters passed to `ainvoke()`.

**Why this design?**
1. **Performance**: No overhead of recreating expensive resources
2. **Scalability**: One set of resources serves thousands of users
3. State **Management**: The `chat_agent` internally manages different conversation threads using the `thread_id` and `user_id`

> [!NOTE] **"Stateless at the instance level"**
The `chat_agent` is a **workflow definition** (a `CompiledStateGraph`). Think of it like a **recipe** or **blueprint**:

```python
# This is like a recipe - it has NO ingredients in it
chat_agent = create_chat_agent(db_conn, ext_service_1, ext_service_2)
```

The agent instance itself doesn't store any:
- ❌ User conversations
- ❌ User preferences  
- ❌ Session data
- ❌ Previous requests

It's just the **logic/workflow** of how to process requests.

> [!NOTE] **"Stateful per session/user"**
The **state** is stored externally and retrieved using the parameters passed to `ainvoke()`.

**How It Works**
1. **Database Storage**: The agent uses `AsyncSqliteSaver(conn)` to store conversation history
2. **Thread Separation**: Each `thread_id` creates a separate conversation thread in the database
3. **Context Loading**: When `ainvoke()` is called, it:
   - Loads the conversation history for that specific `thread_id`
   - Applies the current `user_id`, `location`, etc. as context
   - Processes the new message
   - Saves the updated conversation back to the database

**Analogy**
Think of it like a **restaurant**:
- **The Chef** (`chat_agent`): One chef can cook for many customers, but doesn't remember what each customer ordered before
- **The Order System** (`database` + `thread_id`): Keeps track of each customer's order history
- **The Recipe** (`workflow`): Same cooking process for everyone
- **The Ingredients** (`user_id`, `location`, etc.): Different for each order

**Multiple Users Example**
```python
# User A, Session 1
await agent.ainvoke({"message": "order unicon and 2 candies"}, config={"thread_id": "user-a-session-1"})

# User B, Session 1  
await agent.ainvoke({"message": "order quest protein cookies"}, config={"thread_id": "user-b-session-1"})

# User A, Session 1 (continues previous conversation)
await agent.ainvoke({"message": "Cancel my order"}, config={"thread_id": "user-a-session-1"})
```

**Same agent instance**, but **separate conversation histories** stored in the database by `thread_id`.

## Context Manager explained
 
 **`@asynccontextmanager`**
This is a **decorator** from Python's `contextlib` that converts a generator function into an **asynchronous context manager**. 

**What's a Context Manager?**
A context manager implements the `with` statement pattern:
```python
# Synchronous context manager
with open("file.txt") as f:  # __enter__ called
    content = f.read()       # Use the resource
# __exit__ called automatically (file closed)
```

**Async Context Manager**
Similar, but for async operations:
```python
# Async context manager  
async with some_async_resource() as resource:  # __aenter__ called
    await resource.do_something()              # Use the resource
# __aexit__ called automatically (cleanup)
```

**How `@asynccontextmanager` Works**
Instead of implementing `__aenter__` and `__aexit__` methods manually, you can use `@asynccontextmanager`:
```python
@asynccontextmanager
async def my_async_context():
    # This is like __aenter__
    resource = await setup_resource()
    try:
        yield resource  # Provide the resource
    finally:
        # This is like __aexit__
        await cleanup_resource(resource)

# Usage:
async with my_async_context() as resource:
    await resource.do_work()
```

**`AsyncGenerator[None, None]`**
This is a **type annotation** that describes what the function returns.

**Breaking Down the Type**
```python
AsyncGenerator[YieldType, SendType]
```
- **`YieldType`**: What the generator yields (sends out)
- **`SendType`**: What can be sent back to the generator (rarely used)

**Example:**
```python
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    # Setup code
    yield  # Yields None (nothing)
    # Cleanup code
```
- **First `None`**: The `yield` statement yields `None` (no value)
- **Second `None`**: No values are sent back to the generator

**Why This Pattern?**
> [!NOTE] **FastAPI Lifespan Integration**: FastAPI expects the lifespan function to be an async context manager
```python
# FastAPI internally does something like:
async with lifespan_function(app):
    # Run the web server
    # Handle all requests
    pass
# Cleanup happens here
```

**Visual Timeline**
```python
@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    print("1. Setting up resources...")    # __aenter__ phase
    conn = aiosqlite.connect(":memory:")
    
    yield  # "Here's control, FastAPI - run your server!"
    
    print("2. Cleaning up resources...")   # __aexit__ phase  
    await conn.close()

# FastAPI usage:
# 1. Setting up resources...
# [Server runs and handles requests...]  
# [Server shutdown signal received...]
# 2. Cleaning up resources...
```

**Alternative Without Decorator**
You could write this manually (but it's more verbose):
```python
class LifespanManager:
    async def __aenter__(self):
        self.conn = aiosqlite.connect(":memory:")
        # ... setup code
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()
        # ... cleanup code

# Usage would be the same:
# async with LifespanManager(): ...
```

## **Key Benefits**

1. **Guaranteed Cleanup**: Even if exceptions occur, cleanup code runs
2. **Readable**: Setup and cleanup code are in the same function
3. **FastAPI Integration**: Works seamlessly with FastAPI's lifecycle system
4. **Async Support**: Handles async operations properly

The `@asynccontextmanager` decorator essentially transforms your function into a proper async context manager that FastAPI can use to manage the router's lifecycle!

---
## Key Async Patterns in Chat Agent

#### **Async Functions Everywhere**
```python
# Handler level
@router.post("/chat")
async def chat(request: ChatRequest) -> ChatResponse:
    agent = app_state["chat_agent"]
    agent_output = await agent.ainvoke(...)  # Async agent execution
    return resp

# Tool level  
async def search_items(self, keyword: str) -> Command:
    resp = await self.search_items_client.search(...)  # Async API call
    return result

# Client level
async def search(self, request: SearchRequest) -> SearchResponse:
    resp = await self.__client.get(...)  # Async HTTP request
    return response
```

#### **Async Context Managers**
```python
@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    # Async initialization
    conn = aiosqlite.connect(":memory:")  # Async DB
    yield
    await conn.close()  # Async cleanup
```

#### **AsyncGenerator for Streaming**
```python
from collections.abc import AsyncGenerator

async def stream_response() -> AsyncGenerator[str, None]:
    for chunk in data:
        yield chunk
```

### Common Async Gotchas to Avoid

#### **❌ Mixing Sync/Async**
```python
# DON'T DO THIS
def sync_function():
    result = await async_function()  # Error!

# DO THIS  
async def async_function():
    result = await other_async_function()  # ✅
```

#### **❌ Forgetting await**
```python
# DON'T DO THIS
async def handler():
    result = async_client.search(...)  # Returns coroutine, not result!
    
# DO THIS
async def handler():
    result = await async_client.search(...)  # ✅ Gets actual result
```

#### **❌ Blocking the Event Loop**
```python
# DON'T DO THIS
async def handler():
    time.sleep(5)  # Blocks entire event loop!
    
# DO THIS
async def handler():
    await asyncio.sleep(5)  # ✅ Non-blocking
```

### Database Operations with aiosqlite

```python
import aiosqlite
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

# Connection setup
conn = aiosqlite.connect(":memory:")
memory = AsyncSqliteSaver(conn)

# Usage in LangGraph
workflow.compile(memory)  # Persistent conversation memory
```

## The Beautiful `async` Chain

> [!TIP] The Beautiful Chain:
`HTTP Request → FastAPI Handler → LangGraph Agent → Chat Tools → External APIs`
Each level is async, so while waiting for external APIs, the server can handle other requests!

### **1. HTTP Request → FastAPI Handler**

```python
# app/api/handlers/chat/chat.py
@router.post("/chat")
async def chat(                                    # 🔹 ASYNC function
    request: hatRequest, 
    headers: Annotated[ChatHeader, Header()]
) -> ChatResponse:
    logger.info(f"request: {request}")
    agent = app_state["chat_agent"]
    
    # ⬇️ CALLS NEXT STEP
```

### **2. FastAPI Handler → LangGraph Agent**

```python
# app/api/handlers/chat/chat.py (continued)
    agent_output = await agent.ainvoke(            # 🔹 AWAIT agent call
        {
            "message": request.conversation[-1].content,
        },
        config={
            "thread_id": headers.x_session_id,
            "configurable": {
                "user_id": request.metadata.user_id,
                ...
            },
        },
    )
    
    # ⬇️ CALLS NEXT STEP (internally by LangGraph)
```

### **3. LangGraph Chat → Chat Tools**

```python
# app/agents/friday_agent.py - Inside the agent workflow
def build_chatbot_node(tools: list[Callable]) -> StateNode[AgentState]:
    def chatbot_node(state: AgentState) -> AgentState:
        # LangGraph automatically calls tools when AI decides to use them
        # This happens internally - the tool calls are ASYNC
        
        # When AI returns tool calls, LangGraph routes to:
        # ⬇️ CALLS NEXT STEP
```

### **4. Chat Tools → External APIs**

```python
# app/tools/friday/tools.py
async def search_items(                              # 🔹 ASYNC tool function
    self,
    keyword: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
) -> Command:
    logger.info(f"search_item: {keyword}")
    
    try:
        resp = await self.search_item_client.search(     # 🔹 AWAIT external API
            request=gopoi_dto.SearchRequest(
                keyword=keyword,
		        user_uid=str(user_uid),
            )
        )
        # ⬇️ CALLS NEXT STEP
```

### **5. External APIs → HTTP Request**

```python
# app/external/search_item/client.py
async def search(                                  # 🔹 ASYNC client method
    self, request: dto.SearchRequest
) -> dto.SearchResponse:
    params = request.model_dump(by_alias=True)

    try:
        resp = await self.__client.get(            # 🔹 AWAIT HTTP request
            self.__search_path, 
            params=params
        )
        resp.raise_for_status()
        return dto.SearchResponse.model_validate_json(resp.content)
```

### **Complete Chain with Async/Await Highlighted**

```python
# 1. 🌐 HTTP Request comes in
@router.post("/chat")
async def chat(...) -> MobotChatResponse:          # async ←
    
    # 2. 🎯 Handler calls Agent  
    agent_output = await agent.ainvoke(...)        # await ←
    
    # 3. 🤖 Agent calls Tools (internal to LangGraph)
    # LangGraph automatically awaits tool calls
    
    # 4. 🔧 Tool calls External API
    async def search_items(...) -> Command:          # async ←
        resp = await self.search_items_client.search(...) # await ←
        
        # 5. 🌐 Client makes HTTP Request
        async def search(...) -> SearchResponse:   # async ←
            resp = await self.__client.get(...)    # await ← (HTTP call)
```

### **The Magic: Non-Blocking Flow**

While **one request** is waiting at any `await` point:
- **Other HTTP requests** can be processed
- **Other agent invocations** can run  
- **Other tool calls** can execute
- **Other API calls** can be made

This is why your server can handle thousands of concurrent requests efficiently! 🚀

**Each `await` is a "yield point"** where the event loop can switch to processing other requests instead of blocking and waiting.

---
# ### httpx for Async HTTP Calls

Example code: 
```python
import httpx
from fastapi import HTTPException

class ApiClient:
    def __init__(self):
        self.__client = httpx.AsyncClient(
            base_url="https://api.example.com",
            headers={"Content-Type": "application/json"}
        )
    
    async def make_request(self, data: dict) -> dict:
        try:
            resp = await self.__client.post("/endpoint", json=data)
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code, 
                detail=e.response.text
            ) from e
```

**Benefits of this code**
1. Reuse AsyncClient: Initialize once, use many times
2. Consistent error handling: Same pattern across all clients
3. Pydantic integration: Type-safe requests and responses
4. Configuration-driven: URLs and paths from config
5. Proper headers: Set common headers at client level

This pattern allows your  platform to handle hundreds of concurrent order requests efficiently while making calls to multiple external services (item search, etc.) without blocking! 🚀

---

> [!TIP] In fast API, the route order matters.

**Example**
```python
# ✅ CORRECT ORDER (specific → general)
@router.get("/travel/visa-info/db/all")                               # Most specific
@router.get("/travel/visa-info/db/destination/{destination_country}") # Specific  
@router.get("/travel/visa-info/db/origin/{origin_country}")           # Specific
@router.get("/travel/visa-info/db/{origin_country}/{destination_country}") # General (catch-all)
```