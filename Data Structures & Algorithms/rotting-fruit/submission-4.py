from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        minutes = 0
        visited = set()
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                visited.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < len(grid) and
                            0 <= nc < len(grid[nr]) and
                            grid[nr][nc] == 1):
                        fresh -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))

            minutes += 1
        
        if fresh != 0:
            return -1  
        return minutes 
                