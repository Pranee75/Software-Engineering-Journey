"""
Problem: Minium number of Platforms
Approach: Greedy approach. 
The idea is to sort the arrival and departure times of trains and then use two pointers to traverse through the sorted lists. 
We will keep track of the number of platforms needed at any given time and update the maximum number of platforms required.
TC: O(nlogn) 
SC: O(1) 

"""

class Solution:
    def findPlatform(self, Arrival, Departure):
        Arrival.sort()
        Departure.sort()
        n=len(Arrival)
        platforms_needed=0
        max_platforms=0
        i,j=0,0
        while i<n and j<n:
            if Arrival[i]<=Departure[j]:
                platforms_needed += 1
                i += 1
            else:
                platforms_needed -= 1
                j += 1
            if platforms_needed > max_platforms:
                max_platforms = platforms_needed
            
        return max_platforms
    
sol=Solution()
Arrival=[900, 940, 950, 1100, 1500, 1800]
Departure=[910, 1200, 1120, 1130, 1900, 2000]
print(sol.findPlatform(Arrival, Departure)) 