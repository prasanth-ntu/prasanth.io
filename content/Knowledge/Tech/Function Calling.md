---
tags:
  - DataScience
---
- [Sample code](#Sample%20code)
- [Example use cases](#Example%20use%20cases)
- [The lifecycle of a function call](#The%20lifecycle%20of%20a%20function%20call)
- [Function call mechanisms](#Function%20call%20mechanisms)
	- [Vanilla OpenAI Function Calls](#Vanilla%20OpenAI%20Function%20Calls)
		- [Key Features of Vanilla OpenAI Function Calls:](#Key%20Features%20of%20Vanilla%20OpenAI%20Function%20Calls:)
	- [Example](#Example)
	- [OpenAISchema Powered by Pydantic](#OpenAISchema%20Powered%20by%20Pydantic)
		- [Key Features:](#Key%20Features:)
	- [Example](#Example)
	- [Comparison](#Comparison)
	- [Why Use OpenAISchema with Pydantic?](#Why%20Use%20OpenAISchema%20with%20Pydantic?)
- [Lessons learnt/Challenges faced so far](#Lessons%20learnt/Challenges%20faced%20so%20far)

Function calling allows us to connect models like `gpt-4o` to external tools and systems. This is useful for many things such as empowering AI assistants with capabilities, or building deep integrations between your applications and the models.

# Sample code
Refer Github example(s) for more details:
- Course 1: ...
	- [2-Introduction-To-Function-Calling.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Function-calling-and-data-extraction-with-LLMs/blob/main/L2-Introduction-To-Function-Calling/2-Introduction-To-Function-Calling.ipynb) 
	- [3-Function-calling-variations.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Function-calling-and-data-extraction-with-LLMs/blob/main/L3-Function-calling-variations/3-Function-calling-variations.ipynb)
	- [5-Structured-Extraction.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Function-calling-and-data-extraction-with-LLMs/blob/main/L5-Structured-Extraction/5-Structured-Extraction.ipynb)
- Course 2: [[DeepLearning.AI - Functions, Tools and Agents with LangChain]]
	- [L1-openai-functions.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Functions-Tools-and-Agents-with-LangChain/tree/main/L1)
	- [L2-lcel.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Functions-Tools-and-Agents-with-LangChain/blob/main/L2/L2-lcel.ipynb)
	  [L3-function-calling.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Functions-Tools-and-Agents-with-LangChain/blob/main/L3/L3-function-calling.ipynb)
	  [L4-tagging-and-extraction.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Functions-Tools-and-Agents-with-LangChain/blob/main/L4/L4-tagging-and-extraction.ipynb)
	  
# Example use cases

Function calling is useful for a large number of use cases, such as:

1. **Enabling assistants to fetch data:** an AI assistant needs to fetch the latest customer data from an internal system when a user asks “what are my recent orders?” before it can generate the response to the user
2. **Enabling assistants to take actions:** an AI assistant needs to schedule meetings based on user preferences and calendar availability.
3. **Enabling assistants to perform computation:** a math tutor assistant needs to perform a math computation.
4. **Building rich workflows:** a data extraction pipeline that fetches raw text, then converts it to structured data and saves it in a database.
5. **Modifying your applications' UI:** you can use function calls that update the UI based on user input, for example, rendering a pin on a map.
# The lifecycle of a function call 
![Lifecycle of a function call](https://cdn.openai.com/API/docs/images/function-calling-diagram.png)

![[content/Knowledge/Tech/attachments/images/What-is-Function-Calling.png]]

# Function call mechanisms
## Vanilla OpenAI Function Calls

"Vanilla OpenAI Function Calls" refers to the basic or **default implementation of OpenAI's function-calling mechanism**, **without additional frameworks or libraries enhancing its capabilities**. It involves directly defining and managing function schemas and handling function outputs according to OpenAI's API documentation, typically using JSON-based schemas.

### Key Features of Vanilla OpenAI Function Calls:

1. **Basic Schema Definition**: You define the structure of the input and output using JSON Schema syntax manually.
2. **Error Handling**: Handling errors or validation issues must be coded explicitly.
3. **Parsing and Validation**: Parsing the outputs and ensuring they meet the required schema is typically done using custom or manual logic.
4. **Flexibility**: While flexible, it may require repetitive boilerplate code to manage schema definitions and validation logic.

## Example
```python
openai_function = {
    "type" : "function",
    "function": {
        "name" : "plot_some_points",
        "description" : "Plots some points using matplotlib!",
        "parameters" : {
            "type": "object",
            "properties": {
                "x" : {"type" : "array", "items": {"type": "number"}},
                "y" : {"type" : "array", "items": {"type": "number"}}
            },
            "required": ["x", "y"]
        },
        "type": "function"
    }
}
```

---
## OpenAISchema Powered by Pydantic

When [[Pydantic]] is introduced (via the `openai-schema` package), it builds on the Vanilla OpenAI Function Calls by leveraging Pydantic's robust data validation and management features. [Pydantic](https://docs.pydantic.dev/dev/) is a library that provides easy-to-use, declarative data models in Python. 

> To learn more about comparison between OpenAPI and OpenAISchema, refer *[[OpenAPI]] > Section: # OpenAPI Specification vs. OpenAISchema comparison*
### Key Features:

1. **Declarative Models**: Instead of manually crafting JSON Schemas, you define Python classes using [[Pydantic]], which automatically generates JSON Schemas.
    - Example:
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
```
2. **Automatic Validation**: Input and output validation are handled automatically, ensuring adherence to the schema without additional manual checks.
3. **Error Messaging**: Clear and structured error messages when validation fails.
4. **Serialization/Deserialization**: Pydantic easily converts between Python objects and JSON, simplifying the handling of API inputs and outputs.
5. **Integration with OpenAI Function Calls**: Pydantic-powered schemas can be seamlessly integrated into OpenAI's function calls for better maintainability and reduced boilerplate.

## Example
```python
class PlotStructure(BaseModel):
    x: List[float] = Field(description="X values")
    y: List[float] = Field(description="Y values")

    @field_validator('y')
    def validate_dimensions(cls, y, values):
        if 'x' in values.data and len(values.data['x']) != len(y):
            raise ValueError("x and y arrays must have same length")
        return y
        
    @classmethod
    def get_openai_schema(cls, debug=False) -> Dict[str, Any]:
        """Generate the OpenAI function schema from the Pydantic model"""
        schema = cls.model_json_schema()
        openai_schema = {
            "type" : "function",
            "function": {
                "name" : "plot_some_points",
                "description" : "Plots some points using matplotlib!",
                "parameters": schema
            }
        }
        if debug:
            print(json.dumps(openai_schema, indent=2))
        return openai_schema
    
def plot_some_points(config: PlotStructure) -> None:
    """Create a plot with the given configuration"""
    try:
        plt.figure(figsize=(8, 6))
        plt.plot(config.x, config.y)
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error plotting: {str(e)}")

# Usage
plot_some_points(PlotStructure(x=[1, 2, 3], y=[10, 20, 30]))
```
---
## Comparison 

| **Feature**                        | **Vanilla OpenAI Function Calls** | **OpenAISchema (Pydantic)**                            |
| ---------------------------------- | --------------------------------- | ------------------------------------------------------ |
| Schema Definition                  | Manual JSON Schema                | Declarative Python classes using Pydantic              |
| Validation                         | Manual, error-prone               | Automatic and robust                                   |
| Error Handling                     | Requires custom logic             | Built-in with clear error messages                     |
| Ease of Use                        | More boilerplate                  | Simplifies schema management and reduces code overhead |
| Flexibility                        | Fully customizable                | Highly customizable but constrained by Pydantic        |
| JSON Serialization/Deserialization | Requires manual implementation    | Automatic                                              |

---
## Why Use OpenAISchema with Pydantic?

The combination of OpenAI Function Calls and Pydantic enables developers to focus on defining clean and reusable schemas while letting Pydantic handle the heavy lifting of validation and parsing. It’s particularly useful in production systems where data quality and schema adherence are critical.

# Lessons learnt/Challenges faced so far
1. Docstring matters (Refer [3-Function-calling-variations.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Function-calling-and-data-extraction-with-LLMs/blob/main/L3-Function-calling-variations/3-Function-calling-variations.ipynb))
2. Struggles with Nested APIs or Function Calls (Refer [3-Function-calling-variations.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Function-calling-and-data-extraction-with-LLMs/blob/main/L3-Function-calling-variations/3-Function-calling-variations.ipynb))
3. Similar observation when it needs to make Nested Function calls by handling json values (Refer [5-Structured-Extraction.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Function-calling-and-data-extraction-with-LLMs/blob/main/L5-Structured-Extraction/5-Structured-Extraction.ipynb))
[L4-tagging-and-extraction.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Functions-Tools-and-Agents-with-LangChain/blob/main/L4/L4-tagging-and-extraction.ipynb)
4. We can automate this using `convert_pydantic_to_openai_function` (Refer [L3-function-calling.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Functions-Tools-and-Agents-with-LangChain/blob/main/L3/L3-function-calling.ipynb), and more) in [[DeepLearning.AI - Functions, Tools and Agents with LangChain]]