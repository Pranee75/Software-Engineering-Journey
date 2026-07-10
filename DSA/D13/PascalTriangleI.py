"""
Problem: return the rowIndexth (0-indexed) row of the Pascal's triangle.
Approach: Use the binomial coefficient property: C(n, k) = C(n, k-1) * (n - k + 1) / k.
          This allows us to calculate each element directly from the previous one 
          in the same row without building the entire triangle.
TC: O(rowIndex) - We perform a single loop up to rowIndex.
SC: O(rowIndex) - We only store the resulting row of size rowIndex + 1.
"""

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
    
        # We calculate the next element based on the previous one
        # Formula: C(n, i) = C(n, i-1) * (n - i + 1) / i
        for i in range(1, rowIndex + 1):
            # Calculate current element using integer division
            next_val = row[-1] * (rowIndex - i + 1) // i
            row.append(next_val)
        
        return row
    

solution = Solution()
print(solution.getRow(3))  