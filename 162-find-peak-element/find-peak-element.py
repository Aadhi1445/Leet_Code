class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        index=0
        for i in range(len(nums)):
            if i==0 and (len(nums)>1):
                if nums[i]>nums[i+1]:
                    index=i
            elif i!=(len(nums)-1):
                if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                    index=i
            else:
                if nums[i]>nums[i-1]:
                    index=i
        return index




        