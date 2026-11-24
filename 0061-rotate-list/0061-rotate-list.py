class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head
        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l += 1
        k %= l
        if k == 0:
            return head
        slow = fast = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head