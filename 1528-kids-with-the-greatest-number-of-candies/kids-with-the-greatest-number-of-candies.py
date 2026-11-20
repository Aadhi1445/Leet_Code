class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result=[]
        length=len(candies)
        for i in candies:
            i=i+extraCandies
            c=0
            for j in candies:
                if i>=j:
                    c+=1
            if c==length:
                result.append(True)
            else:
                result.append(False)
        return result


        