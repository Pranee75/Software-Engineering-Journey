# map(): Transforming Data

# Double every number in a list
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # Output: [2, 4, 6, 8]



# filter(): Selecting Data

# Keep only even numbers
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]



# reduce(): Aggregating Data


from functools import reduce
# Sum all elements
nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)
print(total)  # Output: 10


# Sorting with a Custom key

# Sort a list of tuples by the second element
points = [(1, 5), (3, 2), (5, 8)]
points.sort(key=lambda p: p[1])
print(points)  # Output: [(3, 2), (1, 5), (5, 8)]

# Sort a list of dictionaries by a specific key
students = [{'name': 'Alice', 'grade': 88}, {'name': 'Bob', 'grade': 95}]
students.sort(key=lambda s: s['grade'])


# Conditional Logic in Lambdas

# Convert sales to "High" or "Low" status
sales = [8000, 15000, 9500]
status = list(map(lambda x: "High" if x > 10000 else "Low", sales))
print(status)  # Output: ['Low', 'High', 'Low']


# Combining Patterns

# Filter numbers >= 3, then square them
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, filter(lambda x: x >= 3, nums)))
print(result)  # Output: [9, 16, 25]


# sorted(): Ordering Data

pairs = [(1, 5), (3, 2), (5, 8)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

people = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}]
sorted_people = sorted(people, key=lambda x: x['age'], reverse=True)
