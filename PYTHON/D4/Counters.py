# Anagram Check

from collections import Counter

def is_anagram(s1, s2):
    # If Counter objects are equal, the character frequencies are identical
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent")) 


# Top K Frequent Elements

from collections import Counter

def top_k_frequent(nums, k):
    # Counter.most_common(k) returns the k most frequent items as (element, count)
    count = Counter(nums)
    return [item for item, freq in count.most_common(k)]

print(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) 


# First Non-Repeating Character

from collections import Counter

def first_unique_char(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

print(first_unique_char("leetcode")) 


# Custom String/Multiset Operations

from collections import Counter

def can_construct(ransom_note, magazine):
    # Subtracting counters keeps only positive counts. 
    # If the resulting counter is empty (or has no positive values), 
    # then magazine had enough characters.
    diff = Counter(ransom_note) - Counter(magazine)
    return len(diff) == 0

print(can_construct("a", "b"))     
print(can_construct("aa", "aab"))  


