class Solution(object):
    def setZeroes(self, matrix):
        col=1
        m=len(matrix)
        n=len(matrix[0])
        first_row_zero=False
        first_col_zero=False

        for i in range(m):
            if matrix[i][0]==0:
                first_col_zero=True
                break
        for j in range(n):
            if matrix[0][j]==0:
                first_row_zero=True
                break
    
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if first_row_zero==True:
            for i in range(n):
                matrix[0][i]=0
        if first_col_zero==True:
            for i in range(m):
                matrix[i][0]=0

obj=Solution()
print("enter number of rows and cols respectively\n")
m=int(input())
n=int(input())
print("enter all elements\n")
matrix=[]
for i in range(m):
    row=[]
    for i in range(n):
        x=int(input())
        row.append(x)
    matrix.append(row)

obj.setZeroes(matrix)
for i in matrix:
    print(i)
#time complexity:-O(n^2)
#space complexity:-O(1)
