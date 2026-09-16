class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        arr=[]
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    arr.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return arr
obj=Solution()
arr=[-2,0,1,1,2]
print(obj.threeSum(arr))
#time complexity:- O(nlogn +n^2)
#space complexity:-O(1)
