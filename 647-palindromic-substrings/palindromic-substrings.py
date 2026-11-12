class Solution:
    def countSubstrings(self, s: str) -> int:
        # def check(s):
        #     left=0
        #     right=len(s)-1
        #     while left<=right:
        #         if s[left]!=s[right]:
        #             return False
        #         left+=1
        #         right-=1
        #     else:
        #         return True
        # c=0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         k=s[i:j+1]
        #         if check(k):
        #             c+=1
        # return c




        def check(left, right):
            count = 0
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                count += 1
                left -= 1
                right += 1
            return count
        c = 0
        for i in range(len(s)):
            c += check(i, i)       # Odd length
            c += check(i, i + 1)   # Even length
        return c