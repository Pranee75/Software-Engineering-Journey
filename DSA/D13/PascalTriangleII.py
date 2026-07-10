"""
Problem: Generate the first numRows of Pascal's triangle.
Approach: Build the triangle row by row. Each row is initialized with 1s. 
          For any interior element at index j of row i, calculate its value by 
          summing the two elements directly above it from the previous row 
          (triangle[i-1][j-1] and triangle[i-1][j]).
TC: O(numRows^2) - We iterate through each row (numRows), and for each row, 
    we iterate through its elements, resulting in a total of 1 + 2 + 3 + ... + n 
    operations, which is O(n^2).
SC: O(numRows^2) - We store the entire triangle structure, which contains n(n+1)/2 total elements.
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
    
        for i in range(numRows):
            # Start each row with a 1
            row = [1] * (i + 1)
        
            # Fill the middle elements (if any)
            # Each element is the sum of the two elements directly above it
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            triangle.append(row)
        
        return triangle
    
sol=Solution()
print(sol.generate(5))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]