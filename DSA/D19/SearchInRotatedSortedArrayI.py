"""
Problem: Search for a target value in a rotated sorted array (Unique Elements). If the target exists, return its index. Otherwise, return -1.
Approach: Use a modified binary search algorithm to find the target value in the rotated sorted array. 
The algorithm will check which part of the array is sorted and determine if the target lies within that range. 
If it does, continue searching in that half; otherwise, search in the other half.
TC: O(log n) 
SC: O(1)

"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
                
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
    
sol=Solution()
print(sol.search([4,5,6,7,0,1,2],0))