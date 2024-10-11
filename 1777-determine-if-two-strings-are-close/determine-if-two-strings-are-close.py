class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        count1,count2=Counter(word1),Counter(word2)

        return sorted(count1.values())==sorted(count2.values()) and set(count1.keys()) == set(count2.keys())
        