class Solution:
    def nthUglyNumber(self, n: int) -> int:

        if n <= 0:
            return 0

        nums = [1]
        
        i2, i3, i5 = 0, 0, 0

        while len(nums) < n:
        
            m2 = nums[i2] * 2
        
            m3 = nums[i3] * 3
        
            m5 = nums[i5] * 5

            mn = min(m2, m3, m5)
        
            nums.append(mn)

            if mn == m2:
        
                i2 += 1
        
            if mn == m3:  
        
                i3 += 1
        
            if mn == m5:
        
                i5 += 1
        
        return nums[-1]
        