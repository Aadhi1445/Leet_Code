class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        if n==0:
            return 
        k=k%n
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])











        # """
        # Do not return anything, modify nums in-place instead.
        # """
        # for i in range(k):
        #     a=nums[len(nums)-1]
        #     for j in range(len(nums)-2,-1,-1):
        #         nums[j+1]=nums[j]
        #     nums[0]=a
        


        