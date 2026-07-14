# Decorator

def my_decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# General-Purpose Decorator

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(5, 7)


# Decorator with Arguments

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("World")


# Class-Based Decorator

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")

say_hi()
say_hi()


# Preserving Metadata

from functools import wraps

def debug(func):
    @wraps(func)  # This preserves __name__ and __doc__
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@debug
def greet():
    """Returns a greeting string."""
    return "Hi there!"

print(greet.__name__) # Should be 'greet', not 'wrapper'
print(greet.__doc__)  # Should be 'Returns a greeting string.'