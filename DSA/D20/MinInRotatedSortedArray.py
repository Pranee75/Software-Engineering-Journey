"""
Problem: Find minimum in a rotated sorted array
Approach: Binary Search
TC: O(log n)
SC: O(1)

"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1   
        while low < high:
            mid = (low + high) // 2
        
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
                
       
        return nums[low]
    
sol=Solution()
print(sol.findMin([4,5,6,1,2,3]))