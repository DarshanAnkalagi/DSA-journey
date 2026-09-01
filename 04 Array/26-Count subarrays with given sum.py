class Solution(object):
    def subarraySum(self, nums, k):
        dct={}
        dct[0]=1
        prefixsum=0
        count=0
        for i in range(len(nums)):
            prefixsum+=nums[i]
            remove=prefixsum-k
            if remove in dct:
                count+=dct[remove]
            if prefixsum in dct:
                dct[prefixsum]+=1
            else:
                dct[prefixsum]=1
        return count
obj=Solution()
arr=[2,4,6,8,3,6,9,9,6,3,1,0]
print(obj.subarraySum(arr,6))
#time complexity:-O(n)
#space complexity:-O(n)