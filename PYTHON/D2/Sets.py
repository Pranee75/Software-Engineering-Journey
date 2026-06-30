# Contains Duplicate

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1, 2, 3, 1])) 

# Intersection of Two Arrays

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

print(intersection([1, 2, 2, 1], [2, 2])) 

# Happy Number

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        # Calculate sum of squares of digits
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1

print(is_happy(19)) 

# Longest Consecutive Sequence

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Only start counting if 'num' is the start of a sequence
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1
            
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1
            
            longest = max(longest, current_streak)
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))