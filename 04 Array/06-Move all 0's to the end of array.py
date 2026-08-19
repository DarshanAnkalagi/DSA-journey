#Without altering order of array
class Solution(object):
    def moveZeroes(self, nums):
        j=-1
        for i in range(0,len(nums)):
            if nums[i]==0:
                j=i
                break    
        for i in range(j+1,len(nums)):
            if nums[i]!=0 and nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
obj=Solution()
arr=[0,3,4,5,6,0,0,7]
obj.moveZeroes(arr)
print(arr)         