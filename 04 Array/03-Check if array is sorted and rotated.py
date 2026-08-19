class Solution(object):
    def check(self,nums):
        count=0
        for i in range(0,len(nums)-1):
            if nums[i]<=nums[i+1]:
                continue
            elif nums[0]>=nums[len(nums)-1] and nums[i+1]<=nums[len(nums)-1]:
                count+=1
            else:
                return False
        if count==0 or count==1:
            return True
        else:
            return False
obj=Solution()
arr=[0,1,2,3,4,6,6,1,0]
print(obj.check(arr))
#time complexity:-O(n)
#space complexity:-O(1)