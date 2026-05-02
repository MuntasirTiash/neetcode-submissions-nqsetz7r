class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        max_area = 0

        def dfs(grid,r,c):
            if min(r,c)<0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1
            area += dfs(grid,r+1,c)
            area += dfs(grid,r,c+1)
            area += dfs(grid,r-1,c)
            area += dfs(grid,r,c-1)

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(grid, r, c)
                    if area > max_area:
                        max_area = area

        return max_area