'''
Problem: Move all zeros to the end of the array while maintaining the relative order of the non-zero elements.
Approach: Two pointer approach. 
TC: O(n) where n is the number of elements in the array.
SC: O(1) as we are not using any extra space.   

'''

class Solution:
    def moveZeroes(self, nums):
        j=-1
        for i in range(len(nums)):
            if i==0:
                j=i
                break
        
        for i in range(j+1,len(nums)):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
                i+=1
            i+=1
            
        return nums
            
sol=Solution()
print(sol.moveZeroes([0,1,0,3,12]))

"OR"


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        
        # Iterate through the array
        for current in range(len(nums)):
            # If the current element is not 0, swap it with the 
            # position of the last zero we found
            if nums[current] != 0:
                nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1
        return nums
sol = Solution()    
print(sol.moveZeroes([0, 1, 0, 3, 12]))    