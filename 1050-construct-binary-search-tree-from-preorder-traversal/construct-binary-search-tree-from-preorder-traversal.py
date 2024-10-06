# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def build(preorder, bound):

            if not preorder or preorder[0] > bound:

                return None

            root=TreeNode(preorder.pop(0))

            root.left=build(preorder, root.val)

            root.right=build(preorder, bound)

            return root

        return build(preorder, float('inf'))
        