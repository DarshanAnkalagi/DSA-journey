class Solution(object):
    def rotate(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(i+1,n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        for i in range(m):
            matrix[i].reverse()
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
obj.rotate(matrix)
for i in range(m):
    print(matrix[i])
#time complexity:-O(n^2)
#space complexity:-O(1)
