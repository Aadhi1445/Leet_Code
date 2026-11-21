class Solution:
    def addDigits(self, num: int) -> int:
        def add(x):
            total=0
            while x>0:
                r=x%10
                total+=r
                x=x//10
            return total
        while num>9:
            num=add(num)
        return num

        