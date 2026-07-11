"""
Problem: Non overlapping Intervals
Approach: Sort the intervals based on the start time. 
          Then iterate through the intervals and check if the current interval overlaps with the previous one. 
          If it does, we can remove one of them. We can keep track of the end time of the last added interval to help with this check.
TC: O(n log n) due to sorting, where n is the number of intervals.
SC: O(1) if we don't consider the space used for sorting, otherwise O(n) for the sorted intervals.

"""

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end=float('-inf')
        removed_count=0
        for start,cur_end in intervals:
            if start>=end:
                end=cur_end
            else:
                removed_count+=1
        return removed_count
    
sol=Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) 