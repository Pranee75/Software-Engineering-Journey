'''
Problem: Leader in an array
Approach: Traverse the array from right to left and keep track of the maximum element seen so far. 
If the current element is greater than the maximum, it is a leader.

TC: O(n)    
SC: O(n) for storing the leaders in a list (Only to return the leaders in the same order as they appear in the array)
'''

class Solution:
    def leaders(self, nums):
        ans=[]
        max1=float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>max1:
                ans.append(nums[i])
            max1=max(nums[i],max1)

        ans.reverse()
        return ans