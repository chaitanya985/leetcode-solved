# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if not headA or not headB:

            return None

        pa=headA

        pb=headB

        while pa != pb:

            pa = headB if pa is None else pa.next

            pb = headA if pb is None else pb.next

        return pa
        