class pattern:
    def fun(self,n):
        size=2*n-1
        for i in range(0,2*n-1):
            for j in range(0,2*n-1):
                value=n-min(i,j,size-1-i,size-1-j)
                print(value,end="")
            print()        
obj=pattern()
obj.fun(5)