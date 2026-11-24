class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        d = ListNode(0)
        c = head
        while c:
            t = c.next
            p = d
            while p.next and p.next.val <= c.val:
                p = p.next
            c.next = p.next
            p.next = c
            c = t
        return d.next
