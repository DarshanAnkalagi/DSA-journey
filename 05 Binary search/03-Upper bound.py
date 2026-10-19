class Solution:
    def upperBound(self, nums, target):
        ans=len(nums)
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                ans=mid
                right=mid-1
        return ans
obj=Solution()
arr=[2,3,4,5,6,7]
print(obj.upperBound(arr,6))
#time complexity:-O(log(n))
#space cpmplexity:-O(1)
