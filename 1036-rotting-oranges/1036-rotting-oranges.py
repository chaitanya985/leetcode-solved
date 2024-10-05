class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols=len(grid), len(grid[0])

        queue=deque()

        count=0

        for r in range(rows):

            for c in range(cols):

                if grid[r][c]==2:

                    queue.append((r, c))

                elif grid[r][c]==1:

                    count+=1

        minutes=0

        directions=[(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue and count > 0:

            for _ in range(len(queue)):

                r, c=queue.popleft()

                for dc, dr in directions:

                    nr, nc=r+dr, c+dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]==1:

                        grid[nr][nc]=2

                        count-=1

                        queue.append((nr, nc))

            minutes+=1

        return minutes if count==0 else -1