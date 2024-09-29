# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(root, h):

            if root:

                if h==len(ans):

                    ans.append(root.val)

                dfs(root.right, h+1)

                dfs(root.left, h+1)

        ans=[]

        dfs(root, 0)

        return ans
        