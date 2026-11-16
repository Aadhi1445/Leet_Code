class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start=0
        end=len(nums)-1
        ans=len(nums)
        while start<=end:
            mid=(start+end)//2
            if nums[mid]>=target:
                ans=mid
                end=mid-1
                
            else:
                start=mid+1
        return ans




        # nums.append(target)
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i


            # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        #     elif nums[i]>target:
        #         nums[i-1]=target
        #         return i
        