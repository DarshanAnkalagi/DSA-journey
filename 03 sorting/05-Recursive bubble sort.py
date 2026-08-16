class solution:

    def fun(self,a,n):
        if n==1:
            return 
        for i in range(0,n-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
        self.fun(a,n-1)
        
        
obj=solution()
arr=[4,6,2,1,0]
obj.fun(arr,len(arr))
print(arr)
#time complexity:-O(n^2)
#space complexity:-O(n)
