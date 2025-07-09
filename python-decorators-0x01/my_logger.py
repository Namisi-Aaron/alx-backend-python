from datetime import datetime

def log_calls(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f"[{timestamp}] Calling '{func.__name__}' with args: {args}, kwargs: {kwargs}")

        result = func(*args, **kwargs)
        return result
    return wrapper

#Uncomment this lines to test this decorator
# 
# # @log_calls
# def add(x, y):
#     return x + y

# @log_calls
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# result1 = add(5, 3)
# print(f"Add result: {result1}")

# result2 = greet("Alice", greeting="Hi")
# print(f"Greet result: {result2}")