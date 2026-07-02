"""
Problem: Longest Consecutive Sequence in an Array
Approach: Hashing
TC: O(n)
SC: O(n)

"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        count=0
        set1=set()
        longest=1
        if len(nums)==0:
            return 0
        for i in nums:
            set1.add(i)
        for i in set1:
            if i-1 not in set1:
                count=1
                x=i
                while (x+1) in set1:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest
    
sol=Solution()
print(sol.longestConsecutive([100,4,200,1,3,2])) 