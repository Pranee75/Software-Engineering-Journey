'''
Problem: Left rotate an array by k elements.
Approach:
1. Take the first k elements and store them in a temporary array.   
2. Shift the remaining elements of the array to the left by k positions.
3. Copy the elements from the temporary array to the end of the original array.

TC: O(n) where n is the number of elements in the array.
SC: O(k) where k is the number of elements to be rotated.

'''

class Solution:
    def rotateArray(self, nums, k: int) -> None:
        k=k%len(nums)
        temp=nums[:k]
        j=0
        for i in range(k,len(nums)):
            nums[j]=nums[i]
            j+=1

        for l in range(len(nums)-k,len(nums)):
            nums[l]=temp[l-(len(nums)-k)]
        return print(nums)

sol=Solution()
sol.rotateArray([1,2,3,4,5,6,7],3)


'''
Efficient solution: nums[:]=nums[k:]+nums[:k]

'''


