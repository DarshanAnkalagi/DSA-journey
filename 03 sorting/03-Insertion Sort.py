class Solution(object):
    def sortArray(self,a):
        for i in range(0,len(a)-1):
            j=i
            while j>0 and a[j]<a[j-1]:
                temp=a[j]
                a[j]=a[j-1]
                a[j-1]=temp
                j-=1
        return a
            
obj=Solution()
arr=[2,3,5,1,2,7,5]
print(obj.sortArray(arr))
#Time complexity:- O(n^2)
#Space complexity:- O(1)