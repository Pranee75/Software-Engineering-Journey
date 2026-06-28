'''
Problem: Union of two sorted arrays.
Approach:Two pointer approach.
TC: O(n+m) where n and m are the number of elements in the two arrays.
SC: O(n+m) where n and m are the number of elements in the two arrays

'''

class Solution:
    def unionArray(self, nums1, nums2):
        i, j = 0, 0
        result = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                val = nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                val = nums2[j]
                j += 1
            else:
                val = nums1[i]
                i += 1
                j += 1
            
            if not result or result[-1] != val:
                result.append(val)
        
        while i < len(nums1):
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1
            
        return result

# Running the code
sol = Solution()
print(sol.unionArray([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8, 9]))