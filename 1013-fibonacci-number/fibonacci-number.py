class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        a,b=0,1
        l=[]
        ct=0
        while ct<n:
            ct+=1
            l.append(a)
            
            c=a+b
            a=b
            b=c
        return l[-1]+l[-2]


        