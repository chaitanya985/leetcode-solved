class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count=Counter(magazine)

        for c in ransomNote:

            count[c]-=1

            if count[c] < 0:

                return False

        return True
        