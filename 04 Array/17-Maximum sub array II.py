class Solution:
    def maxSubArray(self, nums):
        add=0
     
        maxi=float('-inf')
    
        for i in range(0,len(nums)):
            if add==0:
                start=i

            add+=nums[i]
               
            if add>maxi:
                maxi=add
                end=i

            if add<0:
                add=0
        if start==end:
            print(nums[start])
        else:
            print(nums[start:end+1])
        return maxi
obj=Solution()
arr=[2, 3, 5, -2, 7, -4]
print(obj.maxSubArray(arr))
#time complexity:-O(n)
#space complexity:-O(1)
