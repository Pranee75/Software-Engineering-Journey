"""
Problem: Capacity to Ship Packages Within D Days
Approach: Binary Search 
TC: O(N log S) where N is the number of items in weights and S is the sum of all elements in weights
SC: O(1)

"""

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)   
        high = sum(weights) 
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            required_days = 1
            current_load = 0
            
            for w in weights:
                if current_load + w > mid:
                    required_days += 1
                    current_load = w
                else:
                    current_load += w

            if required_days <= days:
                ans = mid        
                high = mid - 1   
            else:
                low = mid + 1
                
        return ans

sol=Solution()
print(sol.shipWithinDays([2,3,5,1,5],2))