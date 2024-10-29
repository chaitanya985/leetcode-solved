class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def dfs(x, y):

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):

                return False

            if grid[x][y]==1:

                return True

            grid[x][y]=1

            up=dfs(x-1, y)

            down=dfs(x+1, y)

            left=dfs(x, y-1)

            right=dfs(x, y+1)

            return up and down and left and right

        count=0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j]==0:

                    if dfs(i, j):

                        count+=1

        return count


        