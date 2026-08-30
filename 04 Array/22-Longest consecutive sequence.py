class Solution:
    def longestConsecutive(self, nums):
        longest=1
        count=0
        if len(nums)==0:
            return 0
        for i in nums:
            if i-1 not in nums:
                count=1
                x=i
                while x+1 in nums:
                    count+=1
                    x=x+1
                longest=max(count,longest)
        return longest
obj=Solution()
arr=[1,2,5,4,6,3,10,11,7]
print(obj.longestConsecutive(arr))
#time complexity:-O(n)
#space cpmplexity:-O(1)