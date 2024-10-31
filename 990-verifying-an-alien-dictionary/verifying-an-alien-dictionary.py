class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_index={char: index for index, char in enumerate(order)}

        sorted_words=sorted(words, key=lambda word : [order_index[char] for char in word])

        return words==sorted_words
        