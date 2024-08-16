class Solution:
    def checkValidString(self, s: str) -> bool:

        left=0

        right=0

        for char in s:

            if char=="(":

                left+=1

            elif char==")":

                left-=1

            else:
                right+=1

            if left < 0:

                if right > 0:

                    left+=1

                    right-=1

                else:
                    return False

        left=0

        right=0

        for char in reversed(s):

            if char==")":

                left+=1

            elif char=="(":

                left-=1

            else:
                right+=1

            if left < 0:

                if right > 0:

                    left+=1

                    right-=1

                else:
                    return False

        return True

            
        