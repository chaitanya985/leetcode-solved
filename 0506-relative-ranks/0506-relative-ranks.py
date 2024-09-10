class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        sorted_scores=sorted(score, reverse=True)

        rank_dict={s:i+1 for i, s in enumerate(sorted_scores)}

        result=[]

        for s in score:

            if rank_dict[s]==1:

                result.append("Gold Medal")

            elif rank_dict[s]==2:

                result.append("Silver Medal")

            elif rank_dict[s]==3:

                result.append("Bronze Medal")

            else:
                result.append(str(rank_dict[s]))

        return result
        