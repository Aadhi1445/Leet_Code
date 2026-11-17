class Solution:
    def findMin(self, nums: list[int]) -> int:
        # return min(nums)
        start,end=0,len(nums)-1
        minium=float('inf')
        while start<=end:
            mid=(start+end)//2
            if nums[mid]<minium:
                minium=nums[mid]
            if nums[mid]<nums[end]:
                end=mid-1
            else:
                start=mid+1
        return minium