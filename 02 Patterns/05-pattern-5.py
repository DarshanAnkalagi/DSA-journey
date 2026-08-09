
class pattern:
    def fun(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                
                if i-j==1:
                    print(0,end="")
                    continue
                if (i-j)%2==0:
                    print(1,end="")
                else:
                    print(0,end="")
            print("")
obj=pattern()
obj.fun(5)
#alternative Logic:-

def pattern(n):
    for i in range(1, n + 1):
        start = 1 if i % 2 != 0 else 0

        for j in range(i):
            print(start, end="")
            start = 1 - start

        print()