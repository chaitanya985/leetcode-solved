class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def gcd(a, b):

            while b:

                a, b=b, a%b

            return a

        def canDivide(s, t):

            return s==t*(len(s)//len(t))

        g=str1[:gcd(len(str1), len(str2))]

        return g if canDivide(str1, g) and canDivide(str2, g) else ""
        