class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        q=time//(n-1)
        r=time%(n-1)
        if q%2==0:
            return r+1
        else:
            return n-r
        # if n>time:
        #     return time+1
        # p=1
        # d=1
        # for i in range(time):
        #     p=p+d
        #     if p==n or p==1:
        #         d=-d
        # return p



        