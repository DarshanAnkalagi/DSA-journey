class pattern:
    def fun(self,n):
        for i in range(1,n+1):
            space=n-i
            star=2*i-1
            print(space*" "+star*'*')
        for i in range(n,0,-1):
                    space=n-i
                    star=2*i-1
                    print(space*" "+star*'*')
        
obj=pattern()
obj.fun(5)