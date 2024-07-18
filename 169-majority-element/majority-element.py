class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counts=Counter(nums)

        return max(counts.keys(), key=counts.get)
        