'''
Problem: Linear search
TC: O(n)
SC: O(1)

'''

class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1