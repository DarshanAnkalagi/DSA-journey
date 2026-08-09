class pattern:
    def fun(self,n):
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (i==n or i==1 or j==n or j==1):
                    print('*',end="")
                else:
                    print(" ",end="")
            print()
                        
obj=pattern()
obj.fun(4)