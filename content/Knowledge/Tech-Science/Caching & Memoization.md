---
tags:
  - softwareengineering
  - Coding
  - Concepts
  - Programming
  - OptimizationTechniques
---
# ``@functools.cache`` vs . Manual dictionary implementation

| Feature                           | `@functools.cache`                                              | Manual Dictionary Implementation                                                             |
| --------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Implementation**                | Built-in decorator, concise syntax.                             | Requires explicit dictionary management within the function.                                 |
| **Argument Handling**             | Automatically handles positional and keyword arguments as keys. | Requires manual creation of a hashable key from arguments (often a tuple).                   |
| **Cache Invalidation**            | Provides a basic `cache_clear()` method.                        | Requires manual implementation of invalidation logic.                                        |
| **Performance (Generally)**       | Optimized C implementation, generally efficient.                | Performance depends on the efficiency of your manual key creation and dictionary operations. |
| **Readability & Maintainability** | More readable and clearly indicates memoization.                | Caching logic mixed with core function logic, potentially less readable.                     |
| **Boilerplate Code**              | Minimal (just the decorator).                                   | More code required for dictionary management and checks.                                     |
| **Error Potential**               | Less prone to errors in handling arguments as keys.             | More prone to errors in creating consistent and correct keys.                                |
| **Built-in Features**             | Includes basic cache info via `cache_info()`.                   | Requires manual tracking of cache statistics.                                                |
## **Example Comparison:**

### **Using `@functools.cache`:**

```python
import functools

@functools.cache
def expensive_function(a, b, c=10):
    print(f"Calculating for {a}, {b}, {c}")
    return a + b + c

print(expensive_function(1, 2))
print(expensive_function(1, 2))
print(expensive_function(1, 3, c=5))
print(expensive_function(1, 3, c=5))
```

### **Using a Manual Dictionary:**

```python
def expensive_function_manual():
    cache = {}

    def wrapper(a, b, c=10):
        key = (a, b, c)
        if key in cache:
            print(f"Cache hit for {key}")
            return cache[key]
        else:
            print(f"Calculating for {a}, {b}, {c}")
            result = a + b + c
            cache[key] = result
            return result
    return wrapper

expensive_func = expensive_function_manual()
print(expensive_func(1, 2))
print(expensive_func(1, 2))
print(expensive_func(1, 3, c=5))
print(expensive_func(1, 3, c=5))
```

As we can see, the `@functools.cache` approach is significantly more compact and easier to understand.

**In summary, while the underlying principle of caching is the same, `@functools.cache` provides a more convenient, often more efficient, and cleaner way to implement memoization in Python compared to manually managing a dictionary. It handles the complexities of argument hashing and provides basic cache management out of the box, leading to more readable and maintainable code.**