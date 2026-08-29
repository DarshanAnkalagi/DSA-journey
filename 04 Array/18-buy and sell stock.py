class Solution(object):
    def maxProfit(self, nums):
        mini=nums[0]
        profit=0
        for i in range(1,len(nums)):
            cost=nums[i]-mini
            profit=max(cost,profit)
            mini=min(mini,nums[i])
        return profit
obj=Solution()
arr=[2,3,1,2,6,8,5]
print(obj.maxProfit(arr))
#time complexity:-O(n)
#space cpmplexity:-O(1)