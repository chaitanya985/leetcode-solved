class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def backtrack(start, path, remain, k):

            if remain==0 and len(path)==k:

                res.append(path)

                return

            for i in range(start, 10):

                if i > remain:

                    break

                backtrack(i+1, path+[i], remain-i, k)

        res = []
        
        backtrack(1, [], n, k)
        
        return res
        