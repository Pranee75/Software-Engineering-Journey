"""
Problem: Maximum Product Subarray
Approach: The idea is to calculate the prefix and suffix product of the array. 
We will iterate through the array and calculate the prefix product and suffix product at each index. 
We will keep track of the maximum product found so far and return it at the end.
TC: O(n) 
SC: O(1)

"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        prefix,suffix=1,1
        maxi=float('-inf')
        for i in range(len(nums)):
            prefix=1 if prefix==0 else prefix
            suffix=1 if suffix==0 else suffix
            
            prefix=prefix*nums[i]
            suffix=suffix*nums[len(nums)-i-1]
            maxi=max(maxi,max(prefix,suffix))
        return maxi 
             
sol=Solution()
print(sol.maxProduct([2,3,-2,4]))