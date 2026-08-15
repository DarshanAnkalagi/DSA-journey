class solution:
    def fun(self,n,st):
        def check(i):
            if i==n-i-1:
                print("true")
                return
                 
            if st[i]!=st[n-i-1]:
                print("false")
                return
                
            check(i+1)
        check(0)
                    
obj=solution()
st="ahaha"
obj.fun(len(st),st)


