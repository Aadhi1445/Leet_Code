class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        l=[]
        for i in range(1,rowIndex+2):
            k=1
            l1=[]

            for j in range(1,i+1):
                l1.append(k)
                k=k*(i-j)//j
            l.append(l1)
        return l[-1]




        