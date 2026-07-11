import random

numbers = [10, 20, 30, 40, 50]

print(random.randint(1, 100))
print(random.choice(numbers))
print(random.sample(numbers, 3))

random.shuffle(numbers)
print(numbers)