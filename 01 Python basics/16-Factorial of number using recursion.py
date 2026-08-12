class solution:
    def fun(self,n):
        if n==1:
            return 1
        return n*self.fun(n-1)
obj=solution()
print(obj.fun(4))