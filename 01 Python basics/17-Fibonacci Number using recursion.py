class solution:
    def fun(self,n):
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fun(n-1)+self.fun(n-2)

obj=solution()
print(obj.fun(6))
