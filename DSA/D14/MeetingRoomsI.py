"""
Problem: Meeting Rooms
Approach: Greedy
TC: O(nlogn)
SC: O(1)

"""

class Solution:
    def maxMeetings(self, start, end):
        meetings=list(zip(start,end))
        meetings.sort(key=lambda x: x[1])
        end_time=-1
        count=0
        for start,cur_end in meetings:
            if start>end_time:
                count+=1
                end_time=cur_end
        return count

sol=Solution()
print(sol.maxMeetings([1,3,0,5,8,5], [2,4,6,7,9,9]))