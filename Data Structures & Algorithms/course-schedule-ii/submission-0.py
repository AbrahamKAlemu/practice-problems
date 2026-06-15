from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        for cla, pre in prerequisites:
            adj[cla].append(pre)

        res = []
        path = set()
        visited = set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            visited.add(course)
            res.append(course)
            
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            
        