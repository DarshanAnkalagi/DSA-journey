class Solution(object):
    def majorityElement(self, nums):
        count1=0
        count2=0
        el1=float('-inf')
        el2=float('inf')
        ls=[]
        for i in range(0,len(nums)):
            if count1==0 and nums[i]!=el2:
                count1=1
                el1=nums[i]
            elif count2==0 and nums[i]!=el1:
                count2=1
                el2=nums[i]
            elif nums[i]==el1:
                count1+=1
            elif nums[i]==el2:
                count2+=1
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        for i in range(0,len(nums)):
            if nums[i]==el1:
                count1+=1
            if nums[i]==el2:
                count2+=1
        if count1>len(nums)/3:
            ls.append(el1)
        if count2>len(nums)/3:
            ls.append(el2)
        return ls
     
obj=Solution()
nums=[2,3,5,7,2,2,4,6,4,3,4,4,5,7,7,2,2,2,2,2]
print(obj.majorityElement(nums))
#time complexity:-O(n)
#space complexity:-O(1)
