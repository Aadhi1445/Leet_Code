class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        l=nums
        # for i in range(len(l)):
        #     ssum=sum(l[0:i])
        #     esum=sum(l[i+1:len(l)])
        #     if ssum==esum:
        #         return i
        # return -1
        sum=0
        ll=[]
        for i in l:
            sum+=i
            ll.append(sum)
        for i in range(len(l)):
            if i==0:
                ss=0
            else:
                ss=ll[i-1]
            es=ll[len(l)-1]-ll[i]
            if ss==es:
                return i
        return -1

        