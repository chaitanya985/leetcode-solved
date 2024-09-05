class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:

            return 0

        return haystack.find(needle)
        