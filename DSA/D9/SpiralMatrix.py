"""
Problem: Spiral Matrix
Approach:We will maintain four boundaries (top, bottom, left, right) to keep track of the current layer of the matrix we are traversing. 
We will iterate through the matrix in a clockwise direction, updating the boundaries after each complete traversal of a layer.
TC: O(m*n) where m is the number of rows and n is the number of columns in the matrix.
SC: O(1) excluding the output array

"""

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        m=len(matrix[0])
        left,right=0,m-1
        top,bottom=0,n-1
        ans=[]
        while (top<=bottom and left<=right):

            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1

            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1

            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1

        return ans
    

sol=Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) 