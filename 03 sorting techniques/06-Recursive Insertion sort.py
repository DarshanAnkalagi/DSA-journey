class solution:
    def r_sort(self,a,i,n):
        if n==i:
            return
        
        j=i
        while j>0 and a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
            j-=1
        self.r_sort(a,i+1,n)

obj=solution()
arr=[2,4,1,3,2,5,0,2]
obj.r_sort(arr,0,len(arr))
print(arr)
#time complexity:-O(n^2)
#space complexity:-O(n)

         

            