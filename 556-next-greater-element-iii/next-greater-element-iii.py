class Solution:
    def nextGreaterElement(self, n: int) -> int:

        digits=list(str(n))

        i=j=len(digits)-1

        while i>0 and digits[i-1] >= digits[i]:

            i-=1

        if i==0:

            return -1

        while digits[j] <= digits[i-1]:

            j-=1

        digits[i-1], digits[j] = digits[j], digits[i-1]

        digits[i:]=reversed(digits[i:])

        res=int(''.join(digits))

        return res if res < 2**31 else -1
        