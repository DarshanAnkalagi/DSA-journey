class Solution:
    def intersectionArray(self, nums1, nums2):
        arr=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                arr.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return arr        
obj=Solution()
nums1=[0,1,1,1,3,3,3,4]
nums=[0,0,0,1,1,1,2,2,3]
print(obj.intersectionArray(nums1,nums))
#time complexity:-O(m+n)
#Space complexity:-O(k)
