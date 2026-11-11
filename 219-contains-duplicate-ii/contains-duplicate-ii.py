class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                n=abs(d[nums[i]]-i)
                if n<=k:
                    return True
                d[nums[i]]=i
            else:
                d[nums[i]]=i
        return False






