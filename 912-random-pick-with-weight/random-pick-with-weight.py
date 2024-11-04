class Solution:

    def __init__(self, w: List[int]):

        self.weights=w
        
    def pickIndex(self) -> int:

        return random.choices(range(len(self.weights)), weights=self.weights)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()