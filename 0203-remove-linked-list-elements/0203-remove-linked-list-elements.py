class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if head is None:
            return None
        if head.val == val:
            return self.removeElements(head.next,val)
        else:
            head.next = self.removeElements(head.next,val)
            return head