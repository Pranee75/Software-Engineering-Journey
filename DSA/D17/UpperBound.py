"""
Problem: Upper Bound
Approach: Binary Search
TC: O(log n)
SC: O(1)

"""

class Solution:
    def upperBound(self, nums, x):
        low = 0
        high = len(nums)
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] <= x:
                # If element is <= x, the upper bound must be to the right
                low = mid + 1
            else:
                # If element is > x, this could be the upper bound,
                # but we continue searching left for an earlier index
                high = mid
                
        return low
    
    
sol=Solution()
print(sol.upperBound([1, 2, 4, 4, 5], 4)) 
