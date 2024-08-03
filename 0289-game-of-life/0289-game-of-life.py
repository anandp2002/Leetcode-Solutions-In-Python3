class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """       
        # Original | New | State
        #     0    |  0  |   0
        #     1    |  0  |   1
        #     0    |  1  |   2
        #     1    |  1  |   3

        rows,cols=len(board),len(board[0])

        # Helper function to count the no of neighbours having 1 in current state
        def countNeighbours(r,c):
            count=0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if ((i==r and j==c) or i<0 or j<0 or i==rows or j==cols):
                        continue
                    elif board[i][j] in [1,3]:
                        count+=1
            return count
        
        for r in range(rows):
            for c in range(cols):
                neighbour_ones=countNeighbours(r,c)
                if board[r][c]==1:
                    if neighbour_ones in [2,3]:
                        board[r][c]=3
                else:
                    if neighbour_ones==3:
                        board[r][c]=2

        #Replacing by 1 and 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==1:
                    board[r][c]=0
                elif board[r][c] in [2,3]:
                    board[r][c]=1
        