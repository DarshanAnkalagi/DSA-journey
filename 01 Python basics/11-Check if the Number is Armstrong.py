class Solution:
    def fun(self, n):
        count=0
        m=n
        while n>0:
            n=n//10
            count+=1
        sum=0
        while m>0:
            l=m%10
            sum=sum+pow(l,count)
            m=m//10
        print(sum)


obj=Solution()
obj.fun(153)