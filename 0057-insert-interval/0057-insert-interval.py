class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left=[x for x in intervals if x[1] < newInterval[0]]

        right=[x for x in intervals if x[0] > newInterval[1]]

        if left+right != intervals:

            newInterval[0]=min(newInterval[0], intervals[len(left)][0])

            newInterval[1]=max(newInterval[1], intervals[~len(right)][1])

        return left + [newInterval] + right


        