---
tags:
  - SoftwareEngineering
  - DataScience
---
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying i
## Example 1: Basic decorator
```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

Output
```
Before function call
Hello!
After function call
```


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
from functools import wraps

def timer(description):                         # Outer function - takes decorator parameter
    def decorator(func):                        # Takes function to be decorated
        @wraps(func)                            # Preserves original function metadata
        def wrapper(*args, **kwargs):            # Handles any function arguments
	        print(f"Arguments: {args}")
			print(f"Keyword Arguments: {kwargs}")
            start = time.time()                  # Start timing
            result = func(*args, **kwargs)       # Run original function
            end = time.time()                    # End timing
            print(f"{description}: {end - start:.2f} seconds")  # Print timing
            return result                        # Return original function result
        return wrapper                           # Return wrapped function
    return decorator                             # Return decorator function

# Usage Example
@timer("Sorting operation")
def sort_numbers(nums):
    return sorted(nums)

# What happens when called:
# 1. timer("Sorting operation") creates decorator
# 2. @decorator wraps sort_numbers
# 3. wrapper() runs when sort_numbers() called
# 4. Times execution and returns result
# Usage
numbers = list(range(1000))
sorted_nums = sort_list(numbers)
```

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