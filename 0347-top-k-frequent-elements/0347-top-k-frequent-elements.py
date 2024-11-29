class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count=Counter(nums)

        freq=sorted(count, key=lambda x:(-count[x], x))

        return freq[:k]
        