# Frequency Counter

from collections import Counter

def get_frequencies(arr):
    return dict(Counter(arr))

print(get_frequencies([1, 2, 2, 3, 3, 3])) 


# Group Anagrams

from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        # Sort the string to use as a canonical key
        key = "".join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# First Unique Character

def first_unique(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

print(first_unique("leetcode")) 
