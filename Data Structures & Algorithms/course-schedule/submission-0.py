from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        
        visited = set()
        path = set()
        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            path.remove(node)
            visited.add(node)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return len(visited) == numCourses