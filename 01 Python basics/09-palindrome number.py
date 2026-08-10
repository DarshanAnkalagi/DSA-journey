class Solution:
    def fun(self, n):
        x=0
        m=n
        while n>0:
            digit=n%10
            x=x*10+digit
            n=n//10
        if m==x:
            print("true")
        else:
            print("false")
              
obj=Solution()
obj.fun(121)