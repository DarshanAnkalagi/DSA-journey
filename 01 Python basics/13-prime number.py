import math
class solution:
    def fun(self,n):
        count=0
        for i in range(1,int(math.sqrt(n))+1):
            
            if n%i==0:
                count+=1
                if n//i!=i:
                    count+=1
        if count==2:
            print(f"{n} is prime number")  
        else:
            print(f"{n} is  not a prime number")

        
obj=solution()
obj.fun(45)
            