# Comparing Memory Usage between List Comprehensions vs Generator Expressions

import sys

# Suppose we have a range of 1,000,000 numbers
n = 1000000

list_comp = [x * x for x in range(n)]
gen_exp = (x * x for x in range(n))

print(f"List size in memory: {sys.getsizeof(list_comp)} bytes")
print(f"Generator size in memory: {sys.getsizeof(gen_exp)} bytes")


# Infinite Streams (Where List Comp Fails)

def infinite_integers():
    n = 0
    while True:
        yield n
        n += 1

# Using a generator expression to process an infinite stream
even_gen = (x for x in infinite_integers() if x % 2 == 0)

# We can safely take the first 5 without crashing the system
for _ in range(5):
    print(next(even_gen))

    

