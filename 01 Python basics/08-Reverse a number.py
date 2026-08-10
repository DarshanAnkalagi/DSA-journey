class Solution:
    def fun(self, n):
        x=0
        while n>0:
            digit=n%10
            x=x*10+digit
            n=n//10
        print(x)    
                          
               
obj=Solution()
obj.fun(25)