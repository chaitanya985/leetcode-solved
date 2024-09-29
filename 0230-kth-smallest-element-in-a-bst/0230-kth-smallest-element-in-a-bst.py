# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        kth=[]

        while root or kth:

            if root:

                kth.append(root)

                root=root.left

            else:

                root=kth.pop()

                k-=1

                if k==0:

                    return root.val

                root=root.right
        