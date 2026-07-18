"""
Problem: Search in Rotated Sorted Array II (Duplicates allowed )
Approach: Binary Search
TC: O(log n)
SC: O(1)

"""

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n=len(nums)
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                low+=1
                high-=1
                continue

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
        return False

sol=Solution()
print(sol.search([3,1,2,3,3,3,3,3],1))