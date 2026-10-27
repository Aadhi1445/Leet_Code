class Solution(object):
    def maximumSubarraySum(self, nums, k):
        r=l=sum=max=0
        d={}
        while r<len(nums):
            sum+=nums[r]
            d[nums[r]]=d.get(nums[r],0)+1
            if r-l+1==k:
                if len(d)==k:
                    if sum>max:
                        max=sum
                sum-=nums[l]
                d[nums[l]]=d.get(nums[l])-1
                if d[nums[l]]==0:
                    d.pop(nums[l])
                l+=1
            r+=1
        return max
        