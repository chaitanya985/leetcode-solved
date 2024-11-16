class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        even, odd=0, 1

        res=[0]*len(nums)

        for num in nums:

            if num % 2 == 0:

                res[even]=num

                even+=2

            else:

                res[odd]=num

                odd+=2

        return res