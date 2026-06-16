import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        heap = [(grid[0][0], 0, 0)]

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while heap:
            level, r, c = heapq.heappop(heap)
            if r == len(grid) - 1 and c == len(grid) - 1:
                return level
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr == len(grid) or
                        nc < 0 or nc == len(grid[r]) or
                        (nr, nc) in visited):
                    continue
                visited.add((nr, nc))
                heapq.heappush(heap, (max(grid[nr][nc], level), nr, nc))





