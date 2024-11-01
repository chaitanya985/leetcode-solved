class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        mod_map = {0: -1}
        
        total = 0
        
        for i, num in enumerate(nums):
        
            total += num
        
            if k != 0:
        
                total %= k
        
            if total in mod_map:
        
                if i - mod_map[total] > 1:
        
                    return True
        
            else:
        
                mod_map[total] = i
        
        return False
        