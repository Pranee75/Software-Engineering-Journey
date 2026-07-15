# Infinite iterators

import itertools
counter = itertools.count(10,2)
print([next(counter) for _ in range(3)])

cycler = itertools.cycle("AB")
print([next(cycler) for _ in range(5)])

print(list(itertools.repeat("Hi",3)))


# Combination Iterators

from itertools import product,permutations,combinations
print(list(product([1,2],repeat=2)))
print(list(permutations("ABC",2)))
print(list(combinations("ABC",2)))


# Terminating/Processing Iterators

print(list(itertools.chain[1,2],[3,4]))
print(list(itertools.accumulate([1,2,3,4])))

data=[1,1,2,3,3]
for key, group in itertools.groupby(data):
    print(key,list(group))


# Utilities

from itertools import islice, dropwhile, takewhile

data=range(10)
print(list(islice(data,2,6)))
print(list(takewhile(lambda x:x<3,[1,2,3,4])))
print(list(itertools(lambda x:x<3,[1,2,3,4])))

