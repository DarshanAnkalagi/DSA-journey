class Solution(object):
    def rearrangeArray(self, nums):
        i=0
        j=1
        arr=[0]*len(nums)
        for k in nums:
            if k>0:
                arr[i]=k
                i+=2
            if k<0:
                arr[j]=k
                j+=2
        return arr
obj=Solution()
arr=[-2,3,-4,5,6,-4,-5,2]
print(obj.rearrangeArray(arr))
#time complexity:-O(n)
#space complexity:-O(n)

