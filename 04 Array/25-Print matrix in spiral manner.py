class Solution(object):
    def spiralOrder(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=n-1
        top=0
        bottom=m-1
        arr=[]*m*n
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                arr.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                arr.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    arr.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    arr.append(matrix[i][left])
                left+=1
        return arr
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
print(obj.spiralOrder(matrix))
#time complexity:-O(n*m)
#space complexity:-O(n*m)

