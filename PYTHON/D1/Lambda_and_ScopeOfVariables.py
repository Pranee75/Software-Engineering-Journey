'''
Lambda Function. 

'''
square = lambda x: x*x
print("Square of 5 is:", square(5))


'''
Scope of variables in Python.

'''

x = 10

def fun():
    x = 20
    print("Inside function:", x)

fun()
print("Outside function:", x)