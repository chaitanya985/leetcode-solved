class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n=len(nums)

        res=n+1

        s=j=0

        for i, x in enumerate(nums):

            s+=x

            while j<n and s>=target:

                res=min(res, i-j+1)

                s-=nums[j]

                j+=1

        return res if res <= n else 0


        