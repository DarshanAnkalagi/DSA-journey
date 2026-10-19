class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        index=0
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>target:
                index=mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                return mid
        if nums[len(nums)-1]<target:
            return len(nums)
        return index
obj=Solution()
arr=[2,3,4,5,6,7,9]
print(obj.searchInsert(arr,5))
#time complexity:-O(Log n)
#space cpmplexity:-O(1)
