class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        direction=0
        left,right=0,len(matrix[0])-1
        top,down=0,len(matrix)-1

        while(left<=right and top<=down):
            if(direction==0):
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top+=1
            elif(direction==1):
                for i in range(top,down+1):
                    res.append(matrix[i][right])
                right-=1
            elif(direction==2):
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down-=1
            else:
                for i in range(down,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
            direction=(direction+1)%4
        
        return res