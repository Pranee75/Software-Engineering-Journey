"""
Problem: Smallest Divisor Given a Threshold
Approach: Binary Search
TC: O(N log M) where N is the number of elements in nums and M is the maximum value in nums
SC: O(1)

"""

import math
class Solution:
    def SumByD(self,arr,n):
        sum=0
        for i in range(len(arr)):
            sum+=math.ceil(arr[i]/n)
        return sum
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low,high=1,max(nums)
        while low<=high:
            mid=(low+high)//2
            if self.SumByD(nums,mid)<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low 

