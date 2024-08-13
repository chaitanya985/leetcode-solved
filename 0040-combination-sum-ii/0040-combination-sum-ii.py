class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(i, s):

            if s > target:
                
                return
        
            if s == target:
        
                ans.append(t.copy())
        
                return
        
            for j in range(i, len(candidates)):
        
                if j > i and candidates[j] == candidates[j - 1]:
        
                    continue
        
                t.append(candidates[j])
        
                backtrack(j + 1, s + candidates[j])
        
                t.pop()

        ans = []
        
        candidates.sort()
        
        t = []
        
        backtrack(0, 0)
        
        return ans
        