class Solution:
    def reverseVowels(self, s: str) -> str:

        vow={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        i, j=0, len(s)-1

        chars=list(s)

        while i<j:

            if chars[i] not in vow:

                i+=1

            elif chars[j] not in vow:

                j-=1

            else:

                chars[i], chars[j]=chars[j], chars[i]

                i+=1

                j-=1

        return ''.join(chars)
        