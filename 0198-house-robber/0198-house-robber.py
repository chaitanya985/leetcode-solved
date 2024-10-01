class Solution:
    def rob(self, nums: List[int]) -> int:

        not_rob, rob=0, nums[0]

        for num in nums[1:]:

            not_rob, rob=rob, max(num + not_rob, rob)

        return rob
        