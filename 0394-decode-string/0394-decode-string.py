class Solution:
    def decodeString(self, s: str) -> str:

        stack, num, curr=[], 0, ''

        for char in s:

            if char.isdigit():

                num=num*10+int(char)

            elif char=='[':

                stack.append((curr, num))

                curr, num = '', 0

            elif char==']':

                laststr, lastnum=stack.pop()

                curr=laststr + curr * lastnum

            else:

                curr+=char

        return curr


        