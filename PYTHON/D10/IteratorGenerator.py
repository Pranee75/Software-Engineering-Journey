# Implementing a Custom Iterator

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

# Usage
for num in Counter(1, 3):
    print(num)


# The Generator Pattern (using yield)

def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage
for num in fibonacci_gen(5):
    print(num)


# Generator Expressions

# List comprehension (stores all in memory)
list_comp = [x*x for x in range(10)] 

# Generator expression (lazy evaluation)
gen_exp = (x*x for x in range(10)) 

print(next(gen_exp)) # 0
print(next(gen_exp)) # 1

