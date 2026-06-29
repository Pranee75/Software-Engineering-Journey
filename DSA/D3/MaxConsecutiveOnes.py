'''
Problem: Find the Maximum Number of Consecutive 1's in a Binary Array
Approach: Iterate through the array and keep track of the current count of consecutive 1's and the maximum count seen so far.
TC: O(n) 
SC: O(1) 

'''

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max1,counter=0,0
        for i in nums:
            if i==1:
                counter+=1
                max1=max(max1,counter)
            else:
                counter=0
        return max1
    
sol=Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # Output: 3