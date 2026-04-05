---
tags:
  - data-science
  - python
  - software-engineering
aliases:
  - Knowledge/Tech-Science/Decorators
---
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
## Example 1: Basic decorator
```python
from typing import Callable

def my_decorator(func: Callable) -> Callable:
    def wrapper() -> None:
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello() -> None:
    print("Hello!")

say_hello()
```

Output
```
Before function call
Hello!
After function call
```

**The decorator function itself:**

1. `def decorate_hello(func):` - Defines a function that takes another function as its argument. This is the decorator. `func` will hold a reference to whatever function you decorate.
2. `def wrapper():` - Defines a new inner function that will _replace_ the original function. This is where you add the extra behavior.
3. `print("Before hello")` - The extra behavior _before_ calling the original function.
4. `func()` - Calls the original function that was passed in. This is how the original behavior is preserved.
5. `print("After hello")` - The extra behavior _after_ calling the original function.
6. `return wrapper` - Returns the wrapper function (not calling it - no parentheses). This is critical: the decorator must return the replacement function.

**Using the decorator:**

7. `@decorate_hello` - Syntactic sugar. This is equivalent to writing `say_hello = decorate_hello(say_hello)` after the function definition. It passes `say_hello` into `decorate_hello`, and rebinds `say_hello` to whatever is returned (which is `wrapper`).
8. `def say_hello():` - The original function definition.
9. `say_hello()` - Now `say_hello` actually points to `wrapper`, so calling it runs the wrapper, which runs the "before", then the original, then the "after".

A decorator needs to be a callable that accepts a function and returns a new function (the wrapper). The pattern is always:
1. Outer function receives the original function
2. Inner function (wrapper) adds behavior around calling the original
3. Outer function returns the wrapper

This "function returning a function" structure is what makes decoration work - Python replaces the original function reference with whatever the decorator returns.

## Example 2:  Timing decorator with arguments

### Two Decorators

1. `@wraps`: Meta-decorator that preserves function identity
2. `@timer`: Main decorator that adds timing functionality

Think of it as:

- `@timer` wraps your function with timing logic
- `@wraps` ensures the wrapped function keeps its original identity

This is crucial for:

- Debugging
- Documentation tools
- Framework introspection
 
```python
import time
from typing import Any, Callable
from functools import wraps

def timer(description: str) -> Callable:                            # Outer function - takes decorator parameter
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:  # Takes function to be decorated
        @wraps(func)                                                # Preserves original function metadata
        def wrapper(*args: Any, **kwargs: Any) -> Any:              # Handles any function arguments
            print(f"Arguments: {args}")
            print(f"Keyword Arguments: {kwargs}")
            start = time.time()                                     # Start timing
            result = func(*args, **kwargs)                          # Run original function
            end = time.time()                                       # End timing
            print(f"{description}: {end - start:.10f} seconds")     # Print timing
            return result                                           # Return original function result
        return wrapper                                              # Return wrapped function
    return decorator                                                # Return decorator function

# Usage Example
@timer("Sorting operation")
def sort_numbers(nums: list[int]) -> list[int]:
    return sorted(nums)

# What happens when called:
# 1. timer("Sorting operation") creates decorator
# 2. @decorator wraps sort_numbers
# 3. wrapper() runs when sort_numbers() called
# 4. Times execution and returns result
# Usage
numbers = list(range(10))
sorted_nums = sort_numbers(numbers)
```

This is a **decorator with parameters** — it adds an extra layer of nesting compared to the simple decorator you saw earlier.

**Why the extra layer?** When you write `@timer("Sorting operation")`, Python first _calls_ `timer("Sorting operation")`, which returns the actual decorator. So you need three levels:

1. `timer(description)` — receives the decorator's config (the description string)
2. `decorator(func)` — receives the function being decorated (same role as `decorate_hello` from before)
3. `wrapper(*args, **kwargs)` — the replacement function that runs at call time

**Key new concepts:**

- `*args, **kwargs` — makes the wrapper generic. It accepts any positional and keyword arguments and forwards them to `func()`, so this decorator can wrap _any_ function regardless of its signature.
- `@wraps(func)` — without this, `sort_numbers.__name__` would return `"wrapper"` instead of `"sort_numbers"`. `@wraps` copies the original function's metadata (name, docstring, etc.) onto the wrapper. It's itself a decorator (with a parameter!).
- `return result` — unlike the simple decorator, this one captures and returns the original function's return value, so `sorted_nums` gets the actual sorted list.

**Execution flow:**

```
@timer("Sorting operation")     →  timer("Sorting operation") returns decorator
def sort_numbers(nums): ...     →  decorator(sort_numbers) returns wrapper
                                   sort_numbers now points to wrapper

sort_numbers(numbers)           →  wrapper(numbers) runs:
                                     prints args, starts timer
                                     calls original sort_numbers(numbers)
                                     stops timer, prints elapsed time
                                     returns the sorted list
```

### Example 1 vs. Example 2

> [!TIP] The simple decorator is great for learning the concept. The parameterized version is what you'd actually use in real code because it's reusable and works on any function

|#|Feature|Simple decorator (`decorate_hello`)|Parameterized decorator (`timer`)|
|---|---|---|---|
|1|**Decorator parameters**|No — behavior is hardcoded|Yes — `"Sorting operation"` is passed in, so you can reuse the same decorator with different configs|
|2|**Any arguments**|No — `wrapper()` takes no args, only works on zero-parameter functions|Yes — `*args, **kwargs` makes it work on any function regardless of signature|
|3|**Metadata preservation**|No — `say_hello.__name__` would return `"wrapper"`|Yes — `@wraps(func)` keeps the original name, docstring, etc.|
|4|**Return value forwarding**|No — `func()` return value is discarded|Yes — `result = func(*args, **kwargs)` captures and returns it to the caller|

### Example: Why do we need `@wraps`?
`@wraps` from `functools` preserves original function metadata:
    - Function name
    - Docstring
    - Argument list
```python
# Without @wraps
def timer(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@timer
def greet(name):
    """Says hello"""
    print(f"Hello {name}")

print(greet.__name__)  # Prints: wrapper
print(greet.__doc__)   # Prints: None

# With @wraps
def timer_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@timer_with_wraps
def greet(name):
    """Says hello"""
    print(f"Hello {name}")

print(greet.__name__)  # Prints: greet
print(greet.__doc__)   # Prints: Says hello
```

Output
```
wrapper
None
greet
Says hello
```