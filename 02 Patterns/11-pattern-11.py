class pattern:
    def fun(self,n):
        
        for i in range(n,0,-1):
            space=" "*(2*n-2*i)
            star='*'*i
            print(star+space+star)
        for i in range(1,n+1):
            space=" "*(2*n-2*i)
            star='*'*i
            print(star+space+star)

                   
obj=pattern()
obj.fun(5)
                