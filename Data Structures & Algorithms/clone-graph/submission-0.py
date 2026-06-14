"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}

        def dfs(node):
            if node in seen:
                return seen[node]
            
            new_node = Node(node.val)
            seen[node] = new_node
            
            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))

            seen[node] = new_node
            return new_node
        
        return dfs(node) if node else None
