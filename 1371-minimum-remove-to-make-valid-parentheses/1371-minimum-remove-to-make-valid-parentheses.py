class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack=[]

        rem=set()

        for i, char in enumerate(s):

            if char=='(':

                stack.append(i)

            elif char==')':

                if stack:

                    stack.pop()

                else:

                    rem.add(i)

        rem=rem.union(set(stack))

        return ''.join(char for i, char in enumerate(s) if i not in rem)



        