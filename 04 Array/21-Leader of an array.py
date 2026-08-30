class Solution:
    def leaders(self, nums):
        arr=[]
        maxi=nums[-1]
        arr.append(maxi)
        for i in range(len(nums)-2,-1,-1):
            
            if nums[i]>maxi:
                arr.append(nums[i])
                maxi=nums[i]
            
        arr.reverse()
        return arr
obj=Solution()
arr=[2,5,1,5,8,1,4]
print(obj.leaders(arr))
#time complexity:-O(n)
#space complexity:-O(n)