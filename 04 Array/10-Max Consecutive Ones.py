
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        Mcount=0
        
        for i in range(0,len(nums)):
            if nums[i]==0:
                count=0
               
            else:
                count+=1
                if count>Mcount:
                    Mcount=count
        return Mcount 
obj=Solution()
arr=[0,0,0,1,1,1,1,0]
print(obj.findMaxConsecutiveOnes(arr))
#time complexity:-O(n)
#space complexity:-O(1)
