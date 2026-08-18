#Optimal solution
class solution():
    def fun(self,arr):
        if len(arr)<2:
            return -1
        
        second_large=float('-inf')
        large=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>large:
                second_large=large
                large=arr[i]
            elif arr[i]<large and arr[i]>second_large:
                second_large=arr[i]
        if second_large==float('-inf'):
            return -1
        return second_large
obj=solution()
arr=[3,5,2,5,7,9,5,2,22,5,4]
print(obj.fun(arr))
#time complexity=O(n)
#space complexity=O(n)
            

            

