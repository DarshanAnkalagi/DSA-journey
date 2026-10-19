class Solution:
    def lowerBound(self, nums, target):
        ans=len(nums)
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=target:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
            
obj=Solution()
nums=[2,3,4,5,6,7]
print(obj.lowerBound(nums,4))
#time complexity:-O(Log(n))
#space complexity:-O(1)
