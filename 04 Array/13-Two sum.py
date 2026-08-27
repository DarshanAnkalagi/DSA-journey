class Solution(object):
    def twoSum(self, nums, target):
        dictionary={}
        for i,num in enumerate(nums):
            x=target-num
            if x in dictionary:
                return [dictionary[x],i]
            dictionary[num]=i
obj=Solution()
arr=[2,4,6,8,0]
print(obj.twoSum(arr,6))
#time complexity:-O(n)
#space complexity:-O(n)
