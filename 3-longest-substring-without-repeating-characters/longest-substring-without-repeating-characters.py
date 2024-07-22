class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dup=set()

        i=ans=0

        for j, c in enumerate(s):

            while c in dup:

                dup.remove(s[i])

                i+=1

            dup.add(c)

            ans=max(ans, j-i+1)

        return ans
        