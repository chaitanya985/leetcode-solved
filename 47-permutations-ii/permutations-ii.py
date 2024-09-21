class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start):

            if start==len(nums):

                res.add(tuple(nums))

            for i in range(start, len(nums)):

                nums[i],nums[start]=nums[start],nums[i]

                backtrack(start+1)

                nums[i],nums[start]=nums[start],nums[i]

        res = set()
        
        nums.sort()
        
        backtrack(0)
        
        return [list(p) for p in res]


        