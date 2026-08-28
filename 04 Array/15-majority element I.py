class Solution(object):
    def majorityElement(self, nums):
        dct={}
        for i in nums:
            if i in dct:
                dct[i]+=1
            else:
                dct[i]=1
        for i in dct:
            if dct[i]>len(nums)/2:
                return i

obj=Solution()
arr=[2,2,4,5,7,2,2,7,6,6,6,6,2,2,2,2]
print(obj.majorityElement(arr))
#time complexity:-O(n)
#space complexity:-O(n/2)

