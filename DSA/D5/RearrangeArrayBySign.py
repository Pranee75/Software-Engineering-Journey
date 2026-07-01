"""
Problem: Rearrange Array by Sign
Approach: Create a new array of the same size. Use two pointers, one for positive numbers and one for negative numbers.
TC: O(n)
SC: O(n) for the new array

"""
class Solution:
    def rearrangeArray(self, nums):
        arr=[0]*len(nums)
        pos,neg=0,1
        for i in range(len(nums)):
            if nums[i]<0:
                arr[neg]=nums[i]
                neg+=2
            if nums[i]>=0:
                arr[pos]=nums[i]
                pos+=2
        return arr

sol=Solution()
print(sol.rearrangeArray([3,1,-2,-5,2,-4]))