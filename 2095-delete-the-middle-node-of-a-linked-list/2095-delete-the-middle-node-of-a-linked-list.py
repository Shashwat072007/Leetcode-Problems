class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return None
        previous = None
        slow = fast = head
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next
        previous.next = slow.next
        return head