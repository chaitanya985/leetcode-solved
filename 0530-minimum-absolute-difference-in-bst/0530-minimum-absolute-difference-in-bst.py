# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inorder(node):

            if not node:

                return

            inorder(node.left)

            vals.append(node.val)

            inorder(node.right)

        vals=[]

        inorder(root)

        return min(abs(b-a) for a, b in zip(vals, vals[1:]))


        