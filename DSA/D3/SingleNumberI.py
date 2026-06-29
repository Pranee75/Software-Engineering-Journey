'''
Problem: Single Number I
Approach: Use XOR operation to find the single number in the array.
TC: O(n)
SC: O(1)


'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num=0
        for i in nums:
            num^=i
        return num