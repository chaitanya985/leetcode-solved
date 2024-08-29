class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        stack = []
        
        total_sum = 0
        
        for value in arr:
        
            while stack and stack[-1] <= value:
        
                mid = stack.pop()
        
                if stack:
        
                    total_sum += mid * min(stack[-1], value)
        
                else:
        
                    total_sum += mid * value
        
            stack.append(value)
        
        while len(stack) > 1:
        
            total_sum += stack.pop() * stack[-1]
        
        return total_sum
        