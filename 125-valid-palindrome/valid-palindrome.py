class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        # s=s.lower()
        for i in s:
            if i.isalpha() or i.isdigit():
                l.append(i.lower())
        left=0
        right=len(l)-1
        while left<=right:
            if l[left]!=l[right]:
                return False
            left+=1
            right-=1
        else:
            return True
        