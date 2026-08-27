class Solution(object):
    def sortColors(self, nums):
        low,mid,high=0,0,len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            
obj=Solution()
arr=[0,1,2,1,0,1,2]
obj.sortColors(arr)
print(arr)
#time complexity:-O(n)
#space complexity:-O(1)

