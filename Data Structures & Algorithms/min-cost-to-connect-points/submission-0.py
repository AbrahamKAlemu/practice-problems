import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    dst = abs(x1 - x2) + abs(y1 - y2)
                    adj[i].append((dst, j))
        
        heap = [(0, 0)]
        visited = set()

        weight = 0
        while heap:
            w, idx = heapq.heappop(heap)
            if idx in visited:
                continue
            weight += w
            visited.add(idx)
            if len(visited) == len(points):
                return weight
            for wt, i in adj[idx]:
                if i not in visited:
                    heapq.heappush(heap, (wt, i))
            

