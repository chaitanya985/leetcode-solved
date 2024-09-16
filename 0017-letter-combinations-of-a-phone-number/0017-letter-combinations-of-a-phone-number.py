class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:

            return []

        maps=['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs',
        'tuv', 'wxyz']

        res=['']

        for d in digits:

            res=[p+c for p in res for c in maps[int(d)]]

        return res
        