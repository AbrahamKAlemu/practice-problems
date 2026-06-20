from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s, t, w in times:
            adj[s].append((w, t))

        heap = [(0, k)]
        visited = set()

        weight = 0
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return weight
            for nei in adj[node]:
                if nei[1] not in visited:
                    heapq.heappush(heap, (weight + nei[0], nei[1]))

        return -1
        
        