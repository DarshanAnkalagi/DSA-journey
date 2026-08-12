class solution:
    def fun(self,n):
        if n==0:
            return
        self.fun(n-1)
        print(n,end=" ")
obj=solution()
obj.fun(6)