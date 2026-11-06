class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j

        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     if (nums[left] + nums[right]) == target:
        #         return [left, right]
        #     elif (nums[left]+nums[right]) > target:
        #         right -=1
        #     else:
        #         left +=1
        # return []


        