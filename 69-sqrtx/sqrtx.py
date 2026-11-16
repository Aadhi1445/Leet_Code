class Solution:
    def mySqrt(self, x: int) -> int:
        start=0
        end=x//2
        if x<2:
            return x
        while start<=end:
            mid=(start+end)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                end=mid-1
            else:
                start=mid+1
        return end
        # for i in range(x+1):
        #     if i*i==x:
        #         return i
        #     elif i*i>x:
        #         return i-1
        # return 0
            


        