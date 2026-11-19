class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        start = 0
        end = len(letters) - 1
        k = '{'

        while start <= end:
            mid = (start + end) // 2

            if letters[mid] > target:
                k = letters[mid]
                end = mid - 1
            else:
                start = mid + 1

        if k == '{':
            return letters[0]

        return k
        # start=0
        # end=len(letters)-1
        # k='{'
        # while start<end:
        #     mid=(start+end)//2
        #     if letters[mid]>target:
        #         if letters[mid]<k:
        #             k=letters[mid]
        #             target=letters[mid]
        #             end=mid
        #     else:
        #         start=mid+1
        # if k=='{':
        #    return letters[0]
        # return target
        

        # target=ord(target)
        # k=ord('z')
        # k=0
        # k=chr(123)
        # for i in letters:
        #     if i>target:
        #         if i<=k:
        #             k=i

        #         # k=i
        # if k==(chr(123)):
        #     return letters[0]
        # return k

                
            

        