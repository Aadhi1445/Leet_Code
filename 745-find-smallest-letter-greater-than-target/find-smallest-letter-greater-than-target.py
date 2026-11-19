class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        # target=ord(target)
        # k=ord('z')
        # k=0
        k=chr(123)
        for i in letters:
            if i>target:
                if i<=k:
                    k=i

                # k=i
        if k==(chr(123)):
            return letters[0]
        return k

                
            

        