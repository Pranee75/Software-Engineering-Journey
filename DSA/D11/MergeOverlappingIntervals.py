"""
Problem: Merge overlapping intervals
Approach: Sort the intervals based on the start time. Then iterate through the sorted intervals and merge them if they overlap.
TC: O(n log n) due to sorting, where n is the number of intervals.
SC: O(n) for storing the merged intervals. (worst case, all intervals are non-overlapping)

"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n=len(intervals)
        intervals.sort()
        arr=[]
        for i in range(n):
            if not arr or intervals[i][0]>arr[-1][1]:
                arr.append(intervals[i])
            else:
                arr[-1][1]=max(arr[-1][1],intervals[i][1])

        return arr

sol=Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))  
