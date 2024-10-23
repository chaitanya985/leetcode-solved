class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:

            return 0

        if len(nums)==1:

            return nums[0]

        def rob_linear(houses: List[int]) -> int:

            prev, curr=0, 0

            for money in houses:

                prev, curr=curr, max(curr, prev + money)

            return curr

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
        