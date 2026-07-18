"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = { None : None }
        p = head
        while p:
            new_node = Node(p.val)
            nodes[p] = new_node
            p = p.next

        p = head
        while p:
            nodes[p].next = nodes[p.next]
            nodes[p].random = nodes[p.random]
            p = p.next
        
        return nodes[head]

        