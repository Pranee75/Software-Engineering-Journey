'''
Problem: Largest element in an array
Approach: Traverse the array once and keep track of the maximum element.
TC: O(n), where n is the number of elements in the array.
SC: O(1), as we are using a constant amount of space.

'''

class Solution:
    def largestElement(self, nums):
        largestnumber=nums[0]
        for i in nums:
            if i>largestnumber:
                largestnumber=i
        return largestnumber

