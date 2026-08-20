
class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        sum=n*(n+1)//2
        for i in nums:
            sum-=i
        return sum
obj=Solution()
arr=[0,1,2,3,4,5,6,7,8]
print(obj.missingNumber(arr))
#time complexity:-O(n)
#space complexity:-O(1)
