class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        intersections=[]

        for f_start, f_end in firstList:

            for s_start, s_end in secondList:

                if f_end < s_start:

                    break

                if s_end < f_start:

                    continue

                intersections.append([max(f_start, s_start), min(f_end, s_end)])

        return intersections
        