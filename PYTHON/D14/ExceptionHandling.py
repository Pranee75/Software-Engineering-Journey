# Handling Multiple Exceptions & Input Validation

def safe_division():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))
        result = num1 / num2
    except ValueError:
        print("Error: Please enter valid integers.")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution complete.")

safe_division()


# Custom Exceptions

class InsufficientFundsError(Exception):
    """Exception raised when withdrawal amount exceeds balance."""
    def __init__(self, message="Insufficient funds in your account."):
        self.message = message
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Attempted to withdraw {amount} with balance {balance}")
    return balance - amount

try:
    print(withdraw(100, 150))
except InsufficientFundsError as e:
    print(f"Caught an error: {e}")


# Safe Access (Lists & Dictionaries)

def safe_access_demo():
    my_list = [10, 20, 30]
    my_dict = {"a": 1, "b": 2}

    # Handling IndexError
    try:
        print(my_list[5])
    except IndexError:
        print("Index out of range!")

    # Handling KeyError
    try:
        print(my_dict["c"])
    except KeyError:
        print("Key not found!")

safe_access_demo()


# Retry Logic 

import random

def unreliable_operation():
    if random.choice([True, False]):
        raise ConnectionError("Server connection failed")
    return "Data retrieved!"

def fetch_data_with_retry(retries=3):
    for i in range(retries):
        try:
            return unreliable_operation()
        except ConnectionError as e:
            print(f"Attempt {i+1} failed: {e}")
    return "All retries failed."

print(fetch_data_with_retry())



