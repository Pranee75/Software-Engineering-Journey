# Try except structure

def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Please provide numbers only."
    else:
        return f"Result: {result}"
    finally:
        print("Execution complete.")

# Test
print(safe_division(10, 2))
print(safe_division(10, 0))


# Handling multiple exceptions

def parse_list(data):
    try:
        value = int(data[0])
        print(100 / value)
    except (ValueError, IndexError) as e:
        print(f"Caught an expected error: {e}")
    except Exception as e:
        print(f"Caught an unexpected error: {e}")

# Test
parse_list(["abc"]) # Triggers ValueError
parse_list([])      # Triggers IndexErro


# Custom exception

class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass

def check_age(age):
    if age < 18:
        raise ValueTooSmallError("Age must be at least 18.")
    return "Access Granted"

try:
    print(check_age(15))
except ValueTooSmallError as e:
    print(f"Custom Exception: {e}")


# Finally block

def read_file(filename):
    try:
        f = open(filename, 'r')
        print(f.read())
    except FileNotFoundError:
        print("File not found.")
    finally:
        print("Closing file stream (if it was opened).")
        # In real code: f.close() if 'f' in locals() else None

read_file("non_existent_file.txt")


# Advanced exception chaining 

def process_data():
    try:
        # Simulating a database error
        raise ValueError("Database connection failed")
    except ValueError as original_error:
        # Re-raising with context
        raise RuntimeError("Data processing pipeline stopped") from original_error

try:
    process_data()
except RuntimeError as e:
    print(f"Caught: {e}")
    print(f"Caused by: {e.__cause__}")
