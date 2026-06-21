# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
        
        cur = prev.next
        q = None
        for i in range(right - left + 1):
            temp = cur.next
            cur.next = q
            q, cur = cur, temp
        
        prev.next.next = cur
        prev.next = q

        return dummy.next
        
        
        