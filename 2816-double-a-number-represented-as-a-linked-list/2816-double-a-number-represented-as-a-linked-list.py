class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        if head.val >= 5:
            dummy.val = 1
        current = head
        while current:
            carry = 1 if current.next and current.next.val >= 5 else 0
            current.val = (current.val * 2 + carry) % 10
            current = current.next
        return dummy if dummy.val == 1 else head