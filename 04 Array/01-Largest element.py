class solution():
    def largest(self,arr):
        large=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>large:
                large=arr[i]
        return large

obj=solution()
arr=[4,2,8,5,0,5,2,1]
print(obj.largest(arr))
#time complexity:-O(n)
#space complexity:-O(n)



        