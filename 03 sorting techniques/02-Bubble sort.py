class Solution(object):
    def sortArray(self, nums):
        for i in range(0,len(nums)-1):
            for j in range(0,len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp                
        return nums
obj=Solution()
arr=[2,3,5,1,2,7,5]
print(obj.sortArray(arr))
#Time complexity:- O(n^2)
#Space complexity:- O(1)