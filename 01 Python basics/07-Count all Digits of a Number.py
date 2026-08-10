class Solution:
    def countDigit(self, n):
        count=0
        while n>0:
            n=n//10
            count+=1
        print(count)
obj=Solution()
obj.countDigit(456)