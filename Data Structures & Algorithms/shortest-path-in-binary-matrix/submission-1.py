class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        queue = deque()
        queue.append((0,0))
        visit = set()
        visit.add((0,0))

        length = 1
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,1],[-1,-1],[1,-1]]

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or (nr,nc) in visit or nr == ROWS or nc == COLS or grid[nr][nc] == 1):
                        continue
                    
                    queue.append((nr,nc))
                    visit.add((nr,nc))

            length +=1

        return -1