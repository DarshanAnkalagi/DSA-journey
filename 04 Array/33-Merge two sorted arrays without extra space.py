class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:]=nums2
        nums1.sort()
        return nums1
obj=Solution()
arr1=[1,2,3,4,0,0,0]
arr2=[4,4,6]
print(obj.merge(arr1,4,arr2,3))
#time complexity:-O(n)
#Space complexity:-O(m+nlog(m+n))
