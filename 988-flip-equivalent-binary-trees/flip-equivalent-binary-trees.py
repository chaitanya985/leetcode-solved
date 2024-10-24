# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root1, root2):
            
            if root1 == root2 or (root1 is None and root2 is None):
            
                return True
            
            if root1 is None or root2 is None or root1.val != root2.val:
            
                return False
            
            return (dfs(root1.left, root2.left) and dfs(root1.right, root2.right)) or (
                dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
            )

        return dfs(root1, root2)
        