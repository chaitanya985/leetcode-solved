class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        tail = []
        
        for num in nums:
        
            idx = bisect.bisect_left(tail, num)
        
            if idx == len(tail):
        
                tail.append(num)
        
            else:
        
                tail[idx] = num
        
        return len(tail)
        