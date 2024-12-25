---
tags:
  - DataScience
  - SoftwareEngineering
  - DeepLearningAI
  - Course
---

**Key resources**
- Course [link](https://learn.deeplearning.ai/courses/functions-tools-agents-langchain/lesson/1/introduction)
- My Github repo [link](https://github.com/prasanth-ntu/DeepLearningAI-Functions-Tools-and-Agents-with-LangChain)

# Take aways from each lesson

| **Lesson & Notebook**                                                                                                                                                    | **Summary of key points & Callouts**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [L1-openai-functions.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Functions-Tools-and-Agents-with-LangChain/tree/main/L1)                                       | - How to define tools/functions for [[OpenAI]] `ChatCompletion` and pass it, and eventually, execute it.<br>- Different variants of [[Function Calling]].<br>   - `function_call="auto"` ⇒ [[LLM]] will decide when to call the function.<br>   - `function_call="none"`⇒ [[LLM]] will not call the function. <br>   - `function_call={"name": "<function_name>"}`⇒ [[LLM]] will call this function forcefully.<br>- Different roles in `ChatCompletion`<br>   - `user`<br>   - `assistant`<br>   - `function`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [L2-lcel.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Functions-Tools-and-Agents-with-LangChain/blob/main/L2/L2-lcel.ipynb)                                     | [[LCEL]] intro<br>- **Simple chain** (`chain = prompt \| model \| output_parser`) which is `invoke`d using <br>   - prompt (`ChatPromptTemplate`)<br>   - model (`ChatOpenAI`)<br>   - output_parser (`StrOutputParser`)<br>- **More complex chain** that uses `chain = RunnableMap(...) \| prompt \| model \| output_parser`, where we are also introduced to `vectorstores` retriever<br>- **Leverage binding** to create reusable components, such as creating a model with `functions` binded to it.<br>   - e.g., `model = ChatOpenAI(temperature=0).bind(functions=functions)`<br>   - Also, used `ChatPromptMessage` (for multi-turn, role-based prompts), which is different from `ChatPromptTemplate` (simple, single human message prompts)<br>- **Using Fallbacks** to handle failure scenarios<br>   - e.g., `final_chain = simple_chain.with_fallback([complex_chain])`<br>- **Leverage Interface components**<br>   - `invoke [ainvoke]`<br>   - `batch [abatch]`<br>   - `stream [astream]` |
| [L3-function-calling.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Functions-Tools-and-Agents-with-LangChain/blob/main/L3/L3-function-calling.ipynb)             | - Intro to [[Pydantic]], and few examples to create data structures<br>   - Nesting data structures with [[Pydantic]]<br>- [[Pydantic]] to OpenAI function definition (json schema)<br>   - `convert_pydantic_to_openai_function`<br>   - Nested data structures<br>       - e.g.,`class User(BaseModel)` <br>       - e.g., `class Class(BaseModel): Users: List[User]<br> students: List[User]`<br>- Few other scenarios/examples covering previously discussed techniques like<br>   - Forcing to use a function<br>   - Using in a chain<br>   - Using multiple functions                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [L4-tagging-and-extraction.ipynb](https://github.com/prasanth-ntu/DeepLearningAI-Functions-Tools-and-Agents-with-LangChain/blob/main/L4/L4-tagging-and-extraction.ipynb) | - LLM *evaluate* the input text, and generate structured output<br>- Tagging intro<br>   - Assigns descriptive categories or labels<br>   - e.g., `{sentiment: positive, language: spanish}`<br>- Extraction intro<br>   - Retrieves specific information or entities<br>   - e.g., `{first name: Lang, last name: Chain, title: Mr}`<br>- Using `text_splitter` along with `RunnableLambda` to handle really long articles/content<br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |