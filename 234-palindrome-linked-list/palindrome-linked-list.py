# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        vals=[]

        current=head

        while current:

            vals.append(current.val)

            current=current.next

        return vals==vals[::-1]
        