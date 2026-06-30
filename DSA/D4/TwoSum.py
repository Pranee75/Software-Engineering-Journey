'''
Problem: Two sum problem
Approach: Hashing
TC: O(n)
SC: O(n)

'''

class Solution():
    def twosum(self,nums,k):
        dict1={}
        for i,num in enumerate(nums):
            if k-num in dict1:
                return [dict1[k-num],i]
            dict1[num]=i
        return []
    
sol=Solution()
print(sol.twosum([1,2,3,4,5],9))