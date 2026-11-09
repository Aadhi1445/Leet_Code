class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        #     elif nums[i]>target:
        #         nums[i-1]=target
        #         return i
        