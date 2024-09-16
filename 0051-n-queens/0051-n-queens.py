class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def backtrack(row, cols, diag1, diag2, board):

            if row==n:

                res.append(board[:])

                return

            for col in range(n):

                if col in cols or (row-col) in diag1 or (row+col) in diag2:

                    continue

                cols.add(col)

                diag1.add(row-col)

                diag2.add(row+col)

                board[row]='.'*col+'Q'+'.'*(n-col-1)

                backtrack(row+1, cols, diag1, diag2, board)

                cols.remove(col)

                diag1.remove(row-col)

                diag2.remove(row+col)

        res = []
        
        backtrack(0, set(), set(), set(), ['.' * n for _ in range(n)])
        
        return res
        