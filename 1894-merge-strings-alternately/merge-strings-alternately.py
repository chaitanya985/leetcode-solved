class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged=[]

        min_length=min(len(word1), len(word2))

        for i in range(min_length):

            merged.append(word1[i])

            merged.append(word2[i])

        merged.append(word1[min_length:])

        merged.append(word2[min_length:])

        return ''.join(merged)
        