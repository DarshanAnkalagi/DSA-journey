class Solution(object):
    def generate(self, numRows):
        matrix=[]
        for i in range(numRows):
            row=[]
            for j in range(i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    num=matrix[i-1][j-1]+matrix[i-1][j]
                    row.append(num)

            matrix.append(row)    
        return matrix
obj=Solution()
print(obj.generate(5))
#time complexity:-O(n^n)
#space complexity:-O(n^n)
