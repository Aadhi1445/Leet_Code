class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def fun(mid):
            c=0
            for i in piles:
                if i%mid==0:
                    c+=i//mid
                else:
                    c+=(i//mid)+1
            return c

        start=1
        end=max(piles)
        while start<=end:
            mid=(start+end)//2
            k=fun(mid)
            # if k==h:
            #     return k
            if k<=h:
                end=mid-1
            else:
                start=mid+1
        return start
        