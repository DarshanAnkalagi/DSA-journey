class pattern:
    def fun(self,n):
        
        for i in range(1,n+1):
            a=65
            for j in range(1,n-i+1):
                print(" ",end="")
            for k in range(1,i+1):
                print(chr(a),end="")
                a+=1
            for l in range(a-2,64,-1):
                print(chr(l),end="")
            print()
                        
obj=pattern()
obj.fun(4)