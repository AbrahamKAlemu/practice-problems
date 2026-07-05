from collections import defaultdict

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            if not node:
                return None
            
            new_node = Node(node.val)
            visited[node] = new_node
            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))
            return visited[node]
        return dfs(node)