# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        return max(self.dfs(root, True), self.dfs(root, False))

    @cache
    
    def dfs(self, root: TreeNode, isRoot: bool) -> int:

        if not root:

            return 0

        if isRoot:

            return root.val + self.dfs(root.left, False) + self.dfs(root.right, False)

        else:

            return self.rob(root.left) + self.rob(root.right)
        