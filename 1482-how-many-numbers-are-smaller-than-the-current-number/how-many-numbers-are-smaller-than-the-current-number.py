class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for i in nums:
            c = 0
            for j in nums:
                if  i > j:
                    c += 1
            result.append(c)
        return result
        