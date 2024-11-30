class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        maxm=ans=0

        for i, v in enumerate(arr):

            maxm=max(maxm, v)

            if i==maxm:

                ans+=1

        return ans
        