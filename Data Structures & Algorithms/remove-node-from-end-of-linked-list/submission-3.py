# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        p = head
        count = 0
        while p:
            count += 1
            p = p.next

        dummy = ListNode(next=head)
        p = dummy
        for i in range(count - n):
            p = p.next
        p.next = p.next.next
        return dummy.next
        
        """p = head
        for i in range(count - n):
            p = p.next
    
        if p == head:
            return None
        if n == 1:
            p.next = None
            return head
        p.next = p.next.next
        return head"""
        
        