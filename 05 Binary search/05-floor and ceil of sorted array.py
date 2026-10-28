class Solution:
    def getFloorAndCeil(self, nums, x):
        df=-1
        dc=-1
        f=0
        c=len(nums)-1
        while f<=c:
            mid=(f+c)//2
            if nums[mid]>=x:
                dc=mid
                c=mid-1
            else:
                f=mid+1
        f=0
        c=len(nums)-1
        while f<=c:
            mid=(f+c)//2
            if nums[mid]<=x:
                df=mid
                f=mid+1
            else:
                c=mid-1
  
        
        f_value=nums[df] if df!=-1 else -1
        c_value=nums[dc]if dc!=-1 else -1
        return [f_value,c_value]       
obj=Solution()
nums=[2,3,4,5,6,7]
print(obj.getFloorAndCeil(nums,6))
#time complexity:-n(log n)
#space complexity:-n(1)
