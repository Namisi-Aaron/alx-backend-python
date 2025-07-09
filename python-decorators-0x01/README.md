## Decorators: Modifying Functions and Methods

Decorators are functions that modify the behavior of another function or method.
They are applied using the *@decorator_name* syntax and can be used to add, modify, or extend the behavior of the original function without altering its code.

### Key Concepts:

**Basic Decorator Structure**: A decorator function typically wraps another function using an inner wrapper function.

**Decorator with Arguments**: Decorators can handle functions with varying arguments by using *args and **kwargs.

### Examples:

#### Simple Decorator:

```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")
```
#### Decorator with Arguments:

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")
```
### Benefits:
 - **Code Reusability**: Apply the same behavior across multiple functions.
 - **Separation of Concerns**: Keep the core logic separate from the cross-cutting concerns like logging or access control.