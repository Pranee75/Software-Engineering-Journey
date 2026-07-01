"""
Problem: Next Permutation
Approach: 1. Find the first decreasing element from the right. Let's call it 'pivot'.
          2. If no such element exists, the permutation is the last permutation. Reverse the entire array to get the first permutation.
          3. If a pivot is found, find the smallest element to the right of the pivot that is greater than the pivot. Let's call it 'successor'.
          4. Swap the pivot and successor.  
          5. Reverse the elements to the right of the pivot.

TC: O(n)
SC: O(1)

"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind==-1:
            return nums.reverse()
        for i in range(len(nums)-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break
        nums[ind+1:]=reversed(nums[ind+1:])
        return nums


