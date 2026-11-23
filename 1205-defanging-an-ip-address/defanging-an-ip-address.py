class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
        # l=[]
        # for i in address:
        #     if i!='.':
        #         l.append(i)
        #     else:
        #         l.append('[.]')
        # return ''.join(l)