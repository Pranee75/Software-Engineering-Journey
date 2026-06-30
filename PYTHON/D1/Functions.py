"Functions in Python"


def add(a, b):
    return a + b

def greet(name="Praneetha"):
    print(f"Hello {name}")

def multiply(a, b=10):
    return a * b


result = add(5, 3)  # Output: 8
print(result)

greet("Alice")  # Output: Hello Alice

product = multiply(5, 3)  # Output: 15
print(product)

default_product = multiply(5)  # Output: 50
print(default_product)