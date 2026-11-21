class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()
        l=[]
        for i in s:
            if 'A'<=i<='Z':
                i=ord(i)
                l.append(chr(i+32))
            else:
                l.append(i)
        return ''.join(l)

        