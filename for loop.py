class sum:
    def fun(self,low,high):
        sum=0
        for i in range(low,high+1):

            sum=sum+i
        print(sum)
obj=sum()
obj.fun(4,7)
