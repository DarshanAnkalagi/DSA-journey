class Solution(object):
    def nextPermutation(self, nums):

        point=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                point=i
                break
        if point==-1:
            nums.reverse()
            return nums
        for i in range(len(nums)-1,-1,-1):
            if nums[point]<nums[i]:
                temp=nums[point]
                nums[point]=nums[i]
                nums[i]=temp
                break
        i=point+1
        j=len(nums)-1
        while i<j:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            i+=1
            j-=1
        return nums
obj=Solution()
arr=[2,3,1]
print(obj.nextPermutation(arr))


#time complexity:-O(n)
#space complexity:-O(1)

