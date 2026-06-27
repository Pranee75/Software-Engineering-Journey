'''
Problem: Second largest number in an array 
Approach: Scan the array twice 
TC: O(n)
SC: O(1)

'''
class Solution:
    def secondLargestElement(self, nums):
        largestnumber=nums[0]
        secondlargest=-1
        for i in nums:
            if i>largestnumber:
                largestnumber=i
        
        for j in nums:
            if j>secondlargest and j<largestnumber:
                secondlargest=j
        
        return secondlargest

