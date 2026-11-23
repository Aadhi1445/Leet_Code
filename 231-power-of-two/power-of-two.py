class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        c=1
        while True:
            k=2**c
            if k==n:
                return True
            if k>n:
                return False
            c+=1
            




        # return n > 0 and (n & (n - 1)) == 0

        