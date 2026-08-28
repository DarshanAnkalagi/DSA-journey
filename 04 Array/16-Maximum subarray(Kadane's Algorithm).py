class Solution(object):
    def maxSubArray(self, nums):
        add=0
        maxi=float('-inf')
        for i in range(0,len(nums)):

            add+=nums[i]
                
            if add>maxi:
                maxi=add

            if add<0:
                add=0
            
        return maxi
obj=Solution()
arr=[-2,3,4-3,5,3]
print(obj.maxSubArray(arr))
#time complexity:-O(n)
#space complexity:-O(1)
