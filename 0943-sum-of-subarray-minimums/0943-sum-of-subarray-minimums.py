class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        MOD = 10**9 + 7
        
        stack = []
        
        total_sum = 0
        
        n = len(arr)
        
        left = [0] * n
        
        right = [0] * n
        
        for i in range(n):
        
            while stack and arr[stack[-1]] > arr[i]:
        
                stack.pop()
        
            left[i] = i + 1 if not stack else i - stack[-1]
        
            stack.append(i)
        
        stack.clear()
        
        for i in range(n - 1, -1, -1):
        
            while stack and arr[stack[-1]] >= arr[i]:
        
                stack.pop()
        
            right[i] = n - i if not stack else stack[-1] - i
        
            stack.append(i)
        
        for i in range(n):
        
            total_sum += arr[i] * left[i] * right[i]
        
            total_sum %= MOD
        
        return total_sum
        