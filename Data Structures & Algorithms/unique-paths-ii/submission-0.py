class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            return 0

        def memo(r,c,rows,cols,cache):
            if r == rows or c == cols:
                return 0
            
            if cache[r][c] != -1:
                return cache[r][c]

            if r == rows - 1 and c == cols - 1:
                return 1

            cache[r][c] = (memo(r+1,c,rows,cols,cache) if r + 1 < rows and obstacleGrid[r+1][c] == 0 else 0) + (memo(r,c+1,rows,cols,cache) if c + 1 < cols and obstacleGrid[r][c+1] == 0 else 0)

            return cache[r][c]

        return memo(0,0,rows,cols, [[-1]*cols for i in range(rows)])
            