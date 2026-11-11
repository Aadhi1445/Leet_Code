class Solution:
    def isHappy(self, n: int) -> bool:
        k=n
        s=set()
        def fun(n):
            sum=0
            while n>0:
                r=n%10
                sum+=r**2
                n=n//10
            return sum
        while True:
            k=fun(k)
            if k==1:
                return True
            if k in s:
                return False
            s.add(k)

            