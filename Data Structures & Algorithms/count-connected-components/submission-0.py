from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            while par[node] != node:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
        def union(v1, v2):
            v1 = find(v1)
            v2 = find(v2)

            if v1 == v2:
                return 0
            if rank[v1] > rank[v2]:
                par[v2] = v1
                rank[v1] += rank[v2]
            else:
                par[v1] = v2
                rank[v2] += rank[v1]
            return 1

        connections = 0
        for v1, v2 in edges:
            connections += union(v1, v2)
        return n - connections
