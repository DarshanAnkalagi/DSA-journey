import math
class solution:
    def fun(self,n):
        ls=[]
        for i in range(1,int(math.sqrt(n))+1):
            
            if n%i==0:
                ls.append(i)

                if n//i!=i:
                    ls.append(n//i)
        ls.sort()       
        print(ls)
obj=solution()
obj.fun(45)
            