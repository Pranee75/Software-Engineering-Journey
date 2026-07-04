# Counting Frequencies

from collections import defaultdict

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = defaultdict(int)

for word in words:
    counts[word] += 1

print(dict(counts)) # {'apple': 3, 'banana': 2, 'orange': 1}


# Grouping Items

from collections import defaultdict

data = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana"), ("veg", "spinach")]
grouped = defaultdict(list)

for cat, item in data:
    grouped[cat].append(item)

print(dict(grouped)) 


# Graph Representation

from collections import defaultdict

edges = [(1, 2), (1, 3), (2, 3), (1, 2)]
graph = defaultdict(set)

for u, v in edges:
    graph[u].add(v)
    graph[v].add(u) # For undirected graph

print(dict(graph)) 