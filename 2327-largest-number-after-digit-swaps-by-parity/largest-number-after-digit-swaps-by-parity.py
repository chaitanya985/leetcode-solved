class Solution:
    def largestInteger(self, num: int) -> int:

        evens=sorted([int(d) for d in str(num) if int(d) % 2 == 0], reverse=True)

        odds=sorted([int(d) for d in str(num) if int(d) % 2 == 1], reverse=True)

        result=[]

        for d in str(num):

            if int(d) % 2 == 0:

                result.append(str(evens.pop(0)))

            else:
                result.append(str(odds.pop(0)))

        return int(''.join(result))


        