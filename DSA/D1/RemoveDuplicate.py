'''
Problem: Remove duplicates from a sorted array in-place such that each element appears only once and returns the new length. 
Approach: Use 2 pointers
Tc: O(n), where n is the number of elements in the array.
Sc: O(1), as we are using a constant amount of space.   

'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                i=i+1
        return i+1