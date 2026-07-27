"""
Problem: Minimum Number of Days to Make m Bouquets
Approach: Binary search 
TC: O(N log D) Where N is the number of elements in bloomDay and D is the range of days 
SC: O(1)

"""

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def canMakeBouquets(days: int) -> bool:
            bouquets = 0
            flowers = 0
            
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0  
            
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if canMakeBouquets(mid):
                ans = mid
                right = mid - 1  # Try to find a smaller valid day
            else:
                left = mid + 1   # Need more days
                
        return ans
