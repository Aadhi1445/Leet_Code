class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        l=nums
        for i in range(len(l)):
            ssum=sum(l[0:i])
            esum=sum(l[i+1:len(l)])
            if ssum==esum:
                return i
        return -1
        