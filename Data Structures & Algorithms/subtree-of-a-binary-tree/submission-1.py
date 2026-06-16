# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def findRoot(node):
            if not node:
                return False
            res = False
            if node.val == subRoot.val:
                res = same(node, subRoot)
            return findRoot(node.left) or findRoot(node.right) or res
        
        def same(node, sub):
            if not node and not sub:
                return True
            if not node or not sub or node.val != sub.val:
                return False
            return same(node.left, sub.left) and same(node.right, sub.right)
        
        return findRoot(root)

        