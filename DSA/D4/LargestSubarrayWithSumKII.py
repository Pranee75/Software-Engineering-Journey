'''
Problem: Largest Subarray with sum K
Approach: Hashing (for positive and negative numbers)
TC: O(n)
SC: O(n)

'''

class Solution:
    def longest_subarray_with_sum_k(a, k):
    pre_sum_map = {}
    current_sum = 0
    max_len = 0
    
    for i in range(len(a)):
        current_sum += a[i]
        
        # Check if the entire prefix sums to k
        if current_sum == k:
            max_len = max(max_len, i + 1)
            
        # Check if (current_sum - k) exists in the map
        rem = current_sum - k
        if rem in pre_sum_map:
            length = i - pre_sum_map[rem]
            max_len = max(max_len, length)
            
        if current_sum not in pre_sum_map:
            pre_sum_map[current_sum] = i
            
    return max_len