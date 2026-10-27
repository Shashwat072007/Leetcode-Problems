class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        current = head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current 
            current = next_node
        return previous 