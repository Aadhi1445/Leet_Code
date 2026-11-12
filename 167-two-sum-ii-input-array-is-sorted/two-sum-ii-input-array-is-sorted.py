class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        right=len(numbers)-1
        left=0
        while left<right:
            sum=numbers[left]+numbers[right]
            if sum ==target:
                return [left+1,right+1]
            elif sum>target:
                right-=1
            else:
                left+=1
        