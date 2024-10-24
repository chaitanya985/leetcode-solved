# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:

            return []

        res, queue=[], [root]

        while queue:

            level, next_queue=[], []

            for node in queue:

                level.append(node.val)

                if node.left:

                    next_queue.append(node.left)

                if node.right:

                    next_queue.append(node.right)

            res.append(level)

            queue=next_queue

        return res
        