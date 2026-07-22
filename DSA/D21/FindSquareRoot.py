"""
Problem: Find Square root of a number
Approach: Binary Search
TC: O(log n)
SC: O(1)

"""

class Solution:
    def floorSqrt(self, n: int) -> int:
        if n==0 or n==1:
            return n
        
        low,high=0,n
        ans=0
        while low<=high:
            mid=(low+high)//2
            if mid*mid<=n:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    

sol=Solution()
print(sol.floorSqrt(36))