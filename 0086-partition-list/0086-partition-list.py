class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        d1 = ListNode(0)
        d2 = ListNode(0)
        b = d1
        a = d2
        current = head
        while current:
            if current.val<x:
                b.next = current
                b = b.next
            else:
                a.next = current
                a = a.next
            current = current.next
        a.next = None
        b.next = d2.next
        return d1.next