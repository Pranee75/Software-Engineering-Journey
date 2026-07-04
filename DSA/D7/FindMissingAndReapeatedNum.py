"""
Problem: Find the missing and repeated number in an array of size n containing numbers from 1 to n. 
Approach: Use the mathematical properties of the sum and sum of squares to find the missing and repeated numbers.
TC: O(n)
SC: O(1)

"""

class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n=len(nums)
        sn=(n*(n+1))//2
        s2n=(n*(n+1)*(2*n+1))//6
        s,s2=0,0
        for i in range(len(nums)):
            s+=nums[i]
            s2+=nums[i]*nums[i]
        val1=s-sn
        val2=s2-s2n
        val2=val2//val1
        x=(val1+val2)//2
        y=val2-x
        return x,y

sol=Solution()
print(sol.findMissingRepeatingNumbers([3, 1, 3]))