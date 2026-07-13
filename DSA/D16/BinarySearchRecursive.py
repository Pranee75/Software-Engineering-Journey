"""
Problem: Binary Search
Approach: Recursive
Tc: O(log n)
SC: O(log n)

"""

class Solution:
    def search(self, nums, target, low=None, high=None):
        # Initialize boundaries on the first call
        if low is None: low = 0
        if high is None: high = len(nums) - 1
            
        # Base case: Search space is exhausted
        if low > high:
            return -1
        
        mid = low + (high - low) // 2
        
        # Target found
        if nums[mid] == target:
            return mid
        # Target is in the right half
        elif nums[mid] < target:
            return self.search(nums, target, mid + 1, high)
        # Target is in the left half
        else:
            return self.search(nums, target, low, mid - 1)
        
sol=Solution()
print(sol.search([-1,0,3,5,9,12], 9)) 