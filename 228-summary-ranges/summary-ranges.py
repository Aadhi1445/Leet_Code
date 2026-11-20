class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ind=0
        n=len(nums)
        result=[]
        while ind<n:
            start=nums[ind]
            while ind+1<n and nums[ind+1]==nums[ind]+1:
                ind+=1
            end=nums[ind]
            if start==end:
                result.append(str(start))
            else:
                result.append(f'{start}->{end}')
            ind+=1
        return result


        