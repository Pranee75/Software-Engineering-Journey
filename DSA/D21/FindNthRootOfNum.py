"""
Problem: Find the Nth Root of a Number
Approach: Binary search
TC: O(log m) where m is the number 
SC: O(1)

"""

class Solution:
    def NthRoot(self, n, m):
        low,high=0,m
        while low<=high:
            mid=(low+high)//2
            val=mid**n
            if val==m:
                return mid
            elif val<m:
                low=mid+1
            else:
                high=mid-1
        return -1
    
sol=Solution()
print(sol.NthRoot(4,27))