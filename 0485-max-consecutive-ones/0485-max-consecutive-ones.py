class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        cnt=ans=0

        for v in nums:

            if v==1:

                cnt+=1

                ans=max(cnt, ans)

            else:

                cnt=0

        return ans
        