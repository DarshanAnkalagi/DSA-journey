class Solution(object):
    def searchRange(self, nums, target):
       
        left, right = 0, len(nums) - 1
        ans1 = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans1 = mid
                right = mid - 1  # search left part
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
    
        left, right = 0, len(nums) - 1
        ans2 = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans2 = mid
                left = mid + 1  # search right part
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [ans1, ans2]
obj=Solution()
nums=[2,3,4,5,6,6,7,8]
print(obj.searchRange(nums,6))
#time complexity:-O(log n)
#space complexity:-O(1)
