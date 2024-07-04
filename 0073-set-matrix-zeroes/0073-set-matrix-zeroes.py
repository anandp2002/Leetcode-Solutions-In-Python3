class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])

        first_row_has_zero=False
        first_col_has_zero=False

        #iterating throgh matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==0:
                    if row==0:
                        first_row_has_zero=True
                    if col==0:
                        first_col_has_zero=True
                    matrix[row][0]=matrix[0][col]=0

        #update the matrix except row 0 and col 0
        for row in range(1,m):
            for col in range(1,n):
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col]=0

        #update first row and col
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col]=0
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0]=0
        