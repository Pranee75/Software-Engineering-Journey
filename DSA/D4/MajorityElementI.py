'''
Problem: Majority Element I
Approach: Hashing   
TC: O(n)
SC: O(n)

'''

class Solution:
    def majorityElement(self, nums):
        dict1={}
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]]=1
        for key in dict1:
            if dict1[key]>len(nums)//2:
                return key
            
        return -1
    
sol=Solution()
print(sol.majorityElement([3,2,3]))


