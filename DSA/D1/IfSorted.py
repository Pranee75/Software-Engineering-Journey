'''
Problem: Check if array is sorted. 
Approach: Iterate through the array and check if each element is less than or equal to the next element. 
If any element is greater than the next element, return False. If the loop completes without finding any such pair, return True.
TC: O(n), where n is the number of elements in the array.
SC: O(1), as we are using a constant amount of space.

'''

class Solution:
    def isSorted(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
    
solution = Solution()
print(solution.isSorted([1, 2, 3, 4, 5]))