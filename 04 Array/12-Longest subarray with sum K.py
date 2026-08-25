class Solution:
    def longestSubarray(self, nums, k):
        add=nums[0]
        length=0
        maximum=0
        j=0
        i=0
        while i<len(nums):
            while j<=i and add>k:
                add-=nums[j]
                j+=1
            if add==k:
                length=i-j+1
                maximum=max(maximum,length)
            i+=1
            if i<len(nums):
                add+=nums[i]
        return maximum
obj=Solution()
arr=[2,3,5,7,4,2,5,6,2]
print(obj.longestSubarray(arr,10))
#time complexity:-O(n)
#space complexity:-O(1)