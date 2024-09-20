class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        if k<0:
       
            return 0
       
        count=0
       
        count_nums=Counter(nums)
       
        for num in count_nums:
       
            if k==0:
       
                if count_nums[num] > 1:
       
                    count+=1
       
            else:
       
                if num+k in count_nums:
       
                    count+=1
       
        return count
        