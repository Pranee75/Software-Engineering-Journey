"""
Problem: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Approach: Kadane's Algorithm
TC: O(n)
SC: O(1)

"""
class Solution:
    def maxSubArray(self, nums):
        maxnum=nums[0]
        sum1=0
        #ansstart,ansend,start=0,0,0
        for i in range(len(nums)):
            ''' 
            if sum1==0:
                start=i
            '''
            sum1+=nums[i]
            if sum1>maxnum:
                maxnum=sum1
                #ansstart,ansend=start,i
            if sum1<0:
                sum1=0
        return maxnum

sol=Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))