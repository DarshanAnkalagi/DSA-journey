class pattern:
    def fun(self,n):
        
        for i in range(1,n+1):
            a=64+n
            for j in range(1,i+1):
                print(chr(a),end="")
                a-=1
            print()
obj=pattern()
obj.fun(5)
                

            