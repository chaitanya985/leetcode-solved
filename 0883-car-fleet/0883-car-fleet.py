class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        ind=sorted(range(len(position)), key=lambda i: position[i])

        ans=pre=0

        for i in ind[::-1]:

            t=(target - position[i]) / speed[i]

            if t > pre:

                ans+=1

                pre=t

        return ans
        