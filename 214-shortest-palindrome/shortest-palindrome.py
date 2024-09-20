class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if not s:
            
            return ""

        i, n = 0, len(s)
        
        for j in range(n - 1, -1, -1):
        
            if s[i] == s[j]:
        
                i += 1

        if i == n:
        
            return s

        remaining = s[i:]
        
        rem_rev = remaining[::-1]
        
        return rem_rev + self.shortestPalindrome(s[:i]) + remaining
        