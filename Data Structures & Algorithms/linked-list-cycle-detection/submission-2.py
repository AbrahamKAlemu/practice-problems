# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p = head
        seen = set()
        while p:
            if p in seen:
                return True
            seen.add(p)
            p = p.next
        return False