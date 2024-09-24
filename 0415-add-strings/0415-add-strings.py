class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        res, carry=[], 0

        num1, num2=num1[::-1], num2[::-1]

        for i in range(max(len(num1), len(num2))):

            digit1=int(num1[i]) if i < len(num1) else 0

            digit2=int(num2[i]) if i < len(num2) else 0

            total=digit1+digit2+carry

            res.append(str(total%10))

            carry=total//10

        if carry:

            res.append(str(carry))

        return ''.join(res[::-1])
        