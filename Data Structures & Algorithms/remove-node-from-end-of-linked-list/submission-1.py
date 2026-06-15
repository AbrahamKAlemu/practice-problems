class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        c = 0

        while p:
            c += 1
            p = p.next
        
        if c == n:
            return head.next

        p = head
        for i in range(c - n - 1):
            p = p.next

        p.next = p.next.next
        return head