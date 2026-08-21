class Solution(object):
    def singleNumber(self, nums):
        if len(nums)==1:
            return nums[0]
        dictionary={}
        for i in range(0,len(nums)):
            dictionary[nums[i]]=dictionary.get(nums[i],0)+1
            #if nums[i] in dictionary:
            #    dicitionary[nums[i]]+=1
            #else:
            #    dictionary[nums[i]]=0
        for i in dictionary:
            if dictionary[i]==1:
                return i 
        return 0
#time complexity:-O(n+k)
#Space complexity;-O(k)