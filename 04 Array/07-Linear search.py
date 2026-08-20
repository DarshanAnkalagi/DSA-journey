class solution:
    def search(self,nums,target):
        for i in range(0,len(nums)):
            if nums[i]==target:
                return i
        return -1
obj=solution()
arr=[2,4,6,3,5,2,4,5]
print(obj.search(arr,5))
#time complexity:-O(n)
#space complexity:-O(1) 
#        