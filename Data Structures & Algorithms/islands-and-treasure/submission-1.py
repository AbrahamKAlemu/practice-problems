from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        distance = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr == len(grid) or 
                            nc < 0 or nc == len(grid[nr]) or
                            (nr, nc) in visited or grid[nr][nc] == -1):
                        continue
                    grid[nr][nc] = distance
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            distance += 1


        