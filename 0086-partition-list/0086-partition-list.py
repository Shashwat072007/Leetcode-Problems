# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        bh=ListNode(0)
        ah=ListNode(0)
        b=bh
        a=ah
        current=head
        while current:
            if current.val<x:
                b.next=current
                b=b.next
            else:
                a.next=current
                a=a.next
            current=current.next
        a.next=None
        b.next=ah.next
        return bh.next