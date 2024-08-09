class Solution:
    def beautySum(self, s: str) -> int:

        beauty = 0
        
        for i in range(len(s)):
        
            freq = [0] * 26
        
            for j in range(i, len(s)):
        
                freq[ord(s[j]) - ord('a')] += 1
        
                beauty += max(freq) - min(x for x in freq if x > 0)
        
        return beauty
