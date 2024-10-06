# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def dfs(root):

            if root is None:

                return False

            if k-root.val in res:

                return True

            res.add(root.val)

            return dfs(root.left) or dfs(root.right)

        res=set()

        return dfs(root)
        