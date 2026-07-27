"""
Problem: Koko eating Bananas
Approach: Binary search
TC: O(log m) where m is the maximum number of bananas in a single pile (max(piles)).
SC: O(1)

"""

import math 
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low,high=1,max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2

            hours=0
            for i in piles:
                hours+=math.ceil(i/mid)
            if hours<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans 


sol=Solution()
print(sol.minEatingSpeed([3,5,2,8],6))

