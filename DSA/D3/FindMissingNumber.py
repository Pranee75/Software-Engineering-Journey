'''
Problem: Find the Missing Number
Approach: sum approach and XOR approach

TC: O(n) for the sum approach, O(n) for the XOR approach
SC: O(1) for both approaches


'''
from pyclbr import Class
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

sol = Solution()
print(sol.missingNumber([3, 0, 1]))  # Output: 2

"OR by using XOR approach"

class Solution:
    def missingNumber(self, nums: List[int]) -> int:    
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing