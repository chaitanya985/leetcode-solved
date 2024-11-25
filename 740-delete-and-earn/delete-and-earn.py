class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        count=Counter(nums)

        max_num=max(count)

        dp=[0]*(max_num+1)

        for i in range(1, max_num+1):

            dp[i]=max(dp[i-1],dp[i-2] + i * count[i])

        return dp[max_num]
        