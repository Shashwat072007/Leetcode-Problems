class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if head is None:
            return None
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        return head