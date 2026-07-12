"""
Problem: Merge two sorted arrays without extra space
Approach: Two Pointers
TC: O(n + m)
SC: O(1)

"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            # If nums1 still has elements and the current element in nums1 is larger than the one in nums2
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                # Otherwise, place the element from nums2
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            