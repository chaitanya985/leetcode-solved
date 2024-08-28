# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:

            return

        slow, fast=head, head

        while fast and fast.next:

            slow=slow.next

            fast=fast.next.next

        prev, curr=None, slow

        while curr:

            curr.next, prev, curr=prev, curr, curr.next

        first, last=head, prev

        while last.next:

            first_next, last_next=first.next, last.next

            first.next, last.next, first = last, first_next, first_next

            last=last_next
        