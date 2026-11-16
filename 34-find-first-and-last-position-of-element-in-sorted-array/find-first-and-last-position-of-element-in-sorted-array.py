class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        s = 0
        e = len(nums)-1

        lb = -1
        up = -1
        while s <= e:
            mid = (s+e)//2

            if nums[mid] >= target:
                if nums[mid] == target:
                    lb = mid
                e = mid-1
            else:
                s = mid+1
        s = 0
        e = len(nums)-1

        while s <= e:
            mid = (s+e)//2

            if nums[mid] <= target:
                if nums[mid] == target:
                    up = mid
                s = mid+1
            else:
                e = mid-1

        return [lb, up]
        

        # start=0
        # end=len(nums)-1
        # while start<=end:
        #     mid=(start+end)//2
        #     if nums[mid]==target:
        #             break
        #     elif nums[mid]>target:
        #         end=mid-1
        #     else:
        #         start=mid+1
        # else:
        #     return [-1,-1]
        # # a=-1
        # # b=-1
        # while start<=end:
        #     mid=(start+end)//2
        #     if nums[mid]>=target:
        #         a=mid
        #         end=mid-1
        #     else:
        #         start=mid+1
        # start=0
        # end=len(nums)-1
        # b=len(nums)-1
        # while start<=end:
        #     mid=(start+end)//2
        #     if nums[mid]>target:
        #         b=mid
        #         end=mid-1
        #     else:
        #         start=mid+1
        # return [a,b-1]
        
        