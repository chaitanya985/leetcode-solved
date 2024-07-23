class Solution:
    def myAtoi(self, s: str) -> int:

        s=s.strip()

        if not s:

            return 0

        sign=1

        if s[0]=="-":

            sign=-1

            s=s[1:]

        elif s[0]=="+":

            s=s[1:]

        result=0

        for char in s:

            if not char.isdigit():

                break

            result=result*10+int(char)  

        result=max(-2**31,min(sign*result,2**31-1))

        return result 