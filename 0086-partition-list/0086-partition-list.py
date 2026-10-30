class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        lh = ListNode(0)
        gh = ListNode(0)
        l = lh
        g = gh
        current = head
        while current:
            if current.val<x:
                l.next = current
                l = l.next
            else:
                g.next = current
                g = g.next
            current = current.next
        g.next = None
        l.next = gh.next
        return lh.next