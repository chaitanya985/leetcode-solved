class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack=[]

        for digit in num:

            while k>0 and stack and stack[-1] > digit:

                stack.pop()

                k-=1

            stack.append(digit)

        stack=stack[:-k] if k else stack

        return ''.join(stack).lstrip('0') or '0'
        