class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        q=k//(n-1)
        r=k%(n-1)
        if q%2==0:
            return r
        else:
            return n-r-1