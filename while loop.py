#Given a digit d (0 to 9), find the sum of the first 50 positive integers (integers > 0) that end with digit d.
class sum:

    def fun(self,d):
        i=0
        sum=0
        if d==0:
            d=10
        
        while(i<50):
            sum=sum+d
            d=d+10
            i=i+1
        print(sum)

            
obj=sum()
obj.fun(0)

