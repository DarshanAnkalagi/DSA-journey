class solution:
    def fun(self,n,arr):
        def reverse(i):
            if i==n//2:
                return
            temp=arr[i]
            arr[i]=arr[n-i-1]
            arr[n-i-1]=temp
            reverse(i+1)
        reverse(0)
obj=solution()
arr=[1,2,3,4,5]
obj.fun(len(arr),arr)
print(arr)

        