class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        answer = []
 

        if n < 4:
            return answer
 
        nums.sort()
 
        for first in range(n - 3):

            if first > 0 and nums[first] == nums[first - 1]:
                continue
 
            for second in range(first + 1, n - 2):
 
                if (
                    second > first + 1
                    and nums[second] == nums[second - 1]
                ):
                    continue
 
                left = second + 1
                right = n - 1
 
                while left < right:
                    current_sum = (
                        nums[first]
                        + nums[second]
                        + nums[left]
                        + nums[right]
                    )
 
          
                    if current_sum < target:
                        left += 1
 
                    elif current_sum > target:
                        right -= 1
 
                    else:
                        answer.append([
                            nums[first],
                            nums[second],
                            nums[left],
                            nums[right]
                        ])
 
                        left += 1
                        right -= 1
 
                   
                        while (
                            left < right
                            and nums[left] == nums[left - 1]
                        ):
                            left += 1
 
                        while (
                            left < right
                            and nums[right] == nums[right + 1]
                        ):
                            right -= 1
 
        return answer
 
obj=Solution()
arr=[2,-2,0,0,1,1,2]
print(obj.fourSum(arr))
#time complexity:-O(n^3)
#space complexity:-O(1)