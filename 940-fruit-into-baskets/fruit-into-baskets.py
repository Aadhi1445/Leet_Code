class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l=fruits
        mf=le=r=0
        d={}
        while r<len(l):
            d[l[r]]=d.get(l[r],0)+1
            while len(d)>2:
                d[l[le]]=d.get(l[le])-1
                if d[l[le]]==0:
                    d.pop(l[le])
                le+=1
            mf=max(mf,r-le+1)
            r+=1
        return mf



        