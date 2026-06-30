'''
Problem: Find the length of the longest subarray with a given sum K. 
Approach: Two pointer approach/ Sliding window approach (Only for positive numbers)
TC: O(n)
SC: O(1)

'''

class Solution:
    def longestSubarray(self, nums, k):
        left,right=0,0
        sum1=0
        maxlen=0
        
        for right in range(len(nums)):
            sum1+=nums[right]
            while left<=right and sum1>k:
                sum1-=nums[left]
                left+=1

            if sum1==k:
                maxlen=max(maxlen,right-left+1)

        return maxlen

sol=Solution()
nums=[1,2,3,4,5]
k=9
print(sol.longestSubarray(nums,k))
