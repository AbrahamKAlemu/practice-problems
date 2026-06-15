from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        seen = set()

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    seen.add((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0] , [-1, 0]]

        time = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    R, C = r + dr, c + dc
                    if (R < 0 or R == len(grid) or
                            C < 0 or C == len(grid[R]) or 
                            (R, C) in seen or grid[R][C] == 0):
                        continue
                    queue.append((R, C))
                    grid[R][C] = 2
                    seen.add((R, C))

            if queue:
                time += 1

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1
        return time
        