class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        count=Counter()

        for i, v in nums1+nums2:

            count[i]+=v

        return sorted(count.items())
        