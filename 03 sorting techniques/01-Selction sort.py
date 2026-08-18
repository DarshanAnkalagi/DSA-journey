class Solution(object):
    def sortArray(self, nums):
        for i in range(0,len(nums)-1):
            min=i
            for j in range(i,len(nums)):
                if nums[j]<nums[min]:
                    min=j
            temp=nums[min]
            nums[min]=nums[i]
            nums[i]=temp
        return nums
obj=Solution()
arr=[2,3,5,1,2,7,5]
print(obj.sortArray(arr))
#Time complexity:- O(n^2)
#Space complexity:- O(1)s