class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:

        res=list(s)

        i, j=0, len(res)-1

        while i<j:

            res[i] = res[j] = min(res[i], res[j])

            i=i+1

            j-=1

        return ''.join(res)
        