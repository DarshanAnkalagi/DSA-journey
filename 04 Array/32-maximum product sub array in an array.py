class Solution(object):
    def maxProduct(self, nums):
        maxi=nums[0]
        mini=nums[0]
        num=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxi,mini=mini,maxi
            maxi=max(nums[i],maxi*nums[i])
            mini=min(nums[i],mini*nums[i])
            num=max(num,maxi)
        return num
obj=Solution()
arr=[2,3,4,5,-2,4,5]
print(obj.maxProduct(arr))
#time complexity:-O(n)
#space complexity:-O(1)