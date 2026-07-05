"""
Problem: Rotate matrix by 90 degrees
Approach: Transpose the matrix and then reverse each row
TC: O(n^2)
SC: O(1)

"""

class Solution:
    def rotateMatrix(self, matrix):
        n = len(matrix)
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()


