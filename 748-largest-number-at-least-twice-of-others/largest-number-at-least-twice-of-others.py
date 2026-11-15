class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        m=max(nums)
        for i in range(len(nums)):
            if nums[i]!=m:
                if (m<(nums[i]*2)):
                    return -1
        else:
            return nums.index(m)
        