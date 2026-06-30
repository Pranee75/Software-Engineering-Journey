'''
This function takes any number of arguments and returns their sum.
'''
def add(*numbers):
    return sum(numbers)

print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4,5))

'''
This function takes keyword arguments and prints them.
'''

def student(**details):
    print("Student Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

student(name="Praneetha", age=21)