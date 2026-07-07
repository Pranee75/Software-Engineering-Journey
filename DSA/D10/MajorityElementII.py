"""
Problem: Majority Element II
Approach: Hashing
TC: O(n)
SC: O(n)

"""

class Solution:
    def majorityElementTwo(self, nums):
        ans = []
        count = {}
        for n in nums:
            count[n]=count.get(n,0)+1
        for n,c in count.items():
            if c>len(nums)//3:
                ans.append(n)
        return ans
    
sol=Solution()
nums=[1,1,1,3,3,2,2,2]
print(sol.majorityElementTwo(nums))