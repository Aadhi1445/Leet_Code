class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        l=[]
        for i in range(1,numRows+1):
            k=1
            ll=[]
            for j in range(1,i+1):
                ll.append(k)
                k=k*(i-j)//j
            l.append(ll)
        return l
