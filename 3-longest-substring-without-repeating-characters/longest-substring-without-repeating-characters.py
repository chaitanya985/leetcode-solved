class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChars = {}

        for i, char in enumerate(s):
            if char in usedChars and start <= usedChars[char]:
                start = usedChars[char] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChars[char] = i

        return maxLength
        