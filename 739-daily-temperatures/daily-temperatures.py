class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer=[0] * len(temperatures)

        stack=[]

        for i, temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temp:

                ind=stack.pop()

                answer[ind]=i-ind

            stack.append(i)

        return answer
        