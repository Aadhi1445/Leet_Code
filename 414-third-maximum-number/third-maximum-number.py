class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        if len(nums)>=3:
            return nums[-3]
        return nums[-1]

        # a = float('-inf')
        # b = float('-inf')
        # c = float('-inf')
        # for i in nums:
        #     if i == a or i == b or i == c:
        #         continue
        #     if i > a:
        #         c = b
        #         b = a
        #         a = i
        #     elif i > b:
        #         c = b
        #         b = i
        #     elif i > c:
        #         c = i
        # if c == float('-inf'):
        #     return a
        # return c


        # s=set(nums)
        # if len(nums)<=2:
        #     return max(s)
        # d={}
        # for i in range (len(nums)):
        #     if nums[i] in d:
        #         pass
        #     else:
        #         d[nums[i]]=i
        # for 


        
        
        





        