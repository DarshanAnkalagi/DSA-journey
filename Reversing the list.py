#Reverse the given array without creating another array
class solution:
    def process(self,ar):
        left=0
        right=len(ar)-1
        while left<right:
            ar[left],ar[right]=ar[right],ar[left]
            left+=1
            right-=1
        print(ar)
obj=solution()
obj.process([2,3,4,5,6,7])


#printing the array in reverse order
class rev:
    def fun(self,arr):
        n=len(arr)
        new=arr[::-1]
        for i in range(0,n):
            print(new[i])
obj=rev()
obj.fun([2,3,5,4,1])


        
