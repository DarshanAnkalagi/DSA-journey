class solution:
    def union_array(self,nums1,nums2):
        arr3=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j]:
                if not arr3 or arr3[-1]!=nums2[j]:
                    arr3.append(nums2[j])
                j+=1
            elif nums1[i]<nums2[j]:
                if not arr3 or arr3[-1]!=nums1[i]:
                    arr3.append(nums1[i])
                i+=1
            else:
                if not arr3 or arr3[-1]!=nums1[i]:
                    arr3.append(nums1[i])
                i+=1
                j+=1
        while i<len(nums1):
            if not arr3 or arr3[-1]!=nums1[i]:
                arr3.append(nums1[i])
            i+=1
        while j<len(nums2):
            if not arr3 or arr3[-1]!=nums2[j]:
                arr3.append(nums2[j])
            j+=1
        return arr3
obj=solution()
arr1=[1,2,3,3,4,5,5]
arr2=[2,3,4,5,5,6,7,7]
print(obj.union_array(arr1,arr2))
#time complexity:-O(m+n)
#space complexity:-O(m+n)




            
                            
            
                