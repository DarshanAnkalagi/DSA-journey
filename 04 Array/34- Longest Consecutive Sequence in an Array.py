class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        count=1
        maxi=1
        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0
            
        for i in range(0,len(nums)-1):
            if nums[i]+1==(nums[i+1]):
                count+=1
                maxi=max(maxi,count)
            elif nums[i]==nums[i+1]:
                continue
            else:
                count=1

                
        return maxi


obj=Solution()
arr=[2,1,3,5,4]
print(obj.longestConsecutive(arr))
#time complexity:-O(nlogn)
#space comppledxity:-O(1)
