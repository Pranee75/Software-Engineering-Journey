"""
Problem: Lower Bound in a Sorted Array
Approach: Binary Search
TC: O(log n)
SC: O(1)

"""

class Solution:
    def lowerBound(self, nums, x):
        low = 0
        high = len(nums)
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] < x:
                low = mid + 1
            else:
                high = mid
                
        return low


sol=Solution()
print(sol.lowerBound([1, 2, 4, 4, 5], 4))