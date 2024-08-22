class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        result=[]

        for i in range(len(nums)):

            index=abs(nums[i])-1

            if nums[index] < 0:

                result.append(index+1)

            else:
                nums[index]=-nums[index]

        return result

        