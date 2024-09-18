class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        running_sum=[]

        total=0

        for num in nums:

            total+=num

            running_sum.append(total)

        return running_sum