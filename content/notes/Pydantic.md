---
tags:
  - data-science
  - python
  - software-engineering
  - tool
  - ai-agents
aliases:
  - Knowledge/Tech-Science/Pydantic
---
> [!TIP] **Mental model:** Declare what your data should look like with Python type hints, and Pydantic enforces it at runtime — parsing, coercing, and raising clear errors automatically.

## Why [Pydantic](https://docs.pydantic.dev/latest/)

- **Validation with zero boilerplate** — Define a model and Pydantic handles validation, type coercion (e.g., `"42"` → `42`), and error messages
- **Serialization / deserialization** — `.model_dump()`, `.model_dump_json()`, and `.model_validate()` give clean dict/JSON round-tripping
- **Self-documenting data contracts** — Models serve as living documentation for API payloads, config files, DB rows, etc.
- **Custom validators** — `@field_validator` and `@model_validator` let you add business logic that runs automatically on construction
- **Performance** — Pydantic v2 rewrote the core in Rust (`pydantic-core`), making validation 5–50x faster than v1
- **Settings management** — `pydantic-settings` loads config from env vars, `.env` files, or secrets directories with the same validation guarantees

## BaseModel

`BaseModel` is the core class all Pydantic models inherit from. It turns a plain Python class into a validated, serializable data structure — no `__init__` needed.

A "model" is simply a class that inherits from `BaseModel` — it defines the blueprint of your data (what fields exist, their types, and any constraints). Same concept as a schema in JSON Schema, a model in Django ORM, or a struct in Go/Rust. The `model_` prefix on methods (`.model_dump()`, `.model_validate()`) was added in v2 to avoid collisions with user-defined field names — v1 used `.dict()` and `.json()`, which broke if you had a field called `dict` or `json`. The `model_` prefix makes collisions far less likely, though you should still avoid naming fields `model_dump`, `model_validate`, etc. as they would shadow the built-in methods.

What inheriting from `BaseModel` gives you:

| Feature | What it does | Example |
|---|---|---|
| **Automatic `__init__`** | Accepts fields as keyword arguments | `User(name="Alice", age=25)` — no `def __init__` needed |
| **Validation on construction** | Fields are validated and coerced to their declared types | `User(age="25")` → age becomes `25` (int) |
| **`.model_dump()`** | Convert model to dict | `user.model_dump()` → `{"name": "Alice", "age": 25}` |
| **`.model_dump_json()`** | Convert model to JSON string | `user.model_dump_json()` → `'{"name":"Alice","age":25}'` |
| **`.model_validate()`** | Create model from dict | `User.model_validate({"name": "Alice", "age": 25})` |
| **`.model_json_schema()`** | Generate JSON Schema from model | `User.model_json_schema()` → `{"properties": {"name": ...}}` |

### Without vs With Pydantic

**Without** — manual validation is verbose and easy to forget:

```python
class User:
    def __init__(self, name, age, email=None):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(age, int):
            # Won't coerce "25" → 25, just rejects it
            raise TypeError("age must be an integer")
        if email is not None and not isinstance(email, str):
            raise TypeError("email must be a string")
        self.name = name
        self.age = age
        self.email = email
```

**With Pydantic** — same guarantees in 4 lines:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str | None = None

user = User(name="Alice", age="25")
print(user.age)        # 25 (int, not str)
print(user.model_dump())
# {'name': 'Alice', 'age': 25, 'email': None}

User(name="Alice", age="not a number")
# ValidationError: 1 validation error for User
# age - Input should be a valid integer
```

> [!INFO] **BaseModel vs dataclass** — Python's `@dataclass` also generates `__init__` from type hints, but stores whatever you pass with no validation. `BaseModel` validates and coerces on construction.

## Examples

### Nested Models

Pydantic automatically validates nested dicts into their corresponding model types:

```python
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    country: str = "Singapore"

class Employee(BaseModel):
    name: str
    address: Address

emp = Employee(
    name="Bob",
    address={"street": "123 Orchard Rd", "city": "Singapore"}
)
print(emp.address.country)  # "Singapore"
```

### Custom Validators

Two types of validators:

- **`@field_validator`** — a `@classmethod` that runs on a **single field** in isolation. Uses `cls` (the class itself, not an instance) because the instance hasn't been fully constructed yet. It's for checks like "name must not be empty."
- **`@model_validator`** — runs **after all fields** are set, so it uses `self` (the fully constructed instance) and can access the entire model. Use this when validation depends on multiple fields, like "end_date must be after start_date" (you need both values to check this).

```python
from pydantic import BaseModel, field_validator, model_validator
from datetime import date

class Event(BaseModel):
    name: str
    start_date: date
    end_date: date

    @field_validator("name")          # only receives the name value
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Event name cannot be empty")
        return v.strip()

    @model_validator(mode="after")    # receives self — can access all fields
    def end_after_start(self) -> "Event":
        if self.end_date < self.start_date:
            raise ValueError("end_date must be after start_date")
        return self
```

### Serialization Round-Trip

"Round-trip" means converting a model to JSON and back without losing data. This is useful when you need to store models in a database, send them over an API, or cache them to disk — you can always reconstruct the exact same model from the serialized output.

```python
from pydantic import BaseModel

class Config(BaseModel):
    host: str
    port: int
    debug: bool = False

# Dict → Model → JSON → Model
config = Config(host="localhost", port=8080)
json_str = config.model_dump_json()
# '{"host":"localhost","port":8080,"debug":false}'

config2 = Config.model_validate_json(json_str)
assert config == config2
```

### Settings from Environment Variables

Apps typically store config (database URLs, API keys, feature flags) in environment variables rather than hardcoding them. `pydantic-settings` lets you define a model for your config, and it automatically reads and validates values from env vars or `.env` files — so you get the same type safety for config as you do for data.

```python
# pip install pydantic-settings
from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    database_url: str
    api_key: str
    debug: bool = False

    model_config = {"env_prefix": "MY_APP_"}

# Reads MY_APP_DATABASE_URL, MY_APP_API_KEY, MY_APP_DEBUG
# from environment variables or .env file
settings = AppSettings()
```

## Ecosystem and Use Cases

- [[FastAPI]] uses Pydantic models as its core request/response layer
- LangChain, Instructor, and OpenAI's SDK use it for structured outputs (see [[Function Calling]])
- Best applied at boundaries where untrusted or semi-structured data enters your code — API endpoints, file parsing, LLM outputs, config loading

### JSON Schema for Function Calling

![[Pydantic-Introduction.png|534]]
![[Pydantic-Example.png|534]]

We create a Pydantic model that gets cast as a JSON schema, used for function calling in OpenAI.

> [!Note] The Pydantic model itself doesn't do anything — we just use it to generate the JSON schema.

For more details, refer [[Function Calling]] > ***OpenAISchema Powered by Pydantic*** section
