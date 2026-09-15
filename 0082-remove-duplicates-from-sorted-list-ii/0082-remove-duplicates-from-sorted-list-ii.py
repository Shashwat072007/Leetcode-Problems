class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        previous = dummy
        current = head

        while current:
            duplicate = False

            while current.next and current.val == current.next.val:
                duplicate = True
                current = current.next

            if duplicate:
                # Remove the entire group of duplicates
                previous.next = current.next
            else:
                # Move previous only when current is unique
                previous = previous.next

            current = current.next

        return dummy.next
