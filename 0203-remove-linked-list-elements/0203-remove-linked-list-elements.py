class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0, head)
        previous = dummy
        current = head
        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        return dummy.next