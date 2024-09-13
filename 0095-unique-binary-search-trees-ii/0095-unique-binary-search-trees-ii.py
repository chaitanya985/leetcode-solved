# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        if n == 0:
            
            return []
        
        def generate_trees(start, end):
            
            if start > end:
            
                return [None]
            
            all_trees = []
            
            for i in range(start, end + 1):
            
                left_trees = generate_trees(start, i - 1)
            
                right_trees = generate_trees(i + 1, end)
            
                for left in left_trees:
            
                    for right in right_trees:
            
                        root = TreeNode(i)
            
                        root.left = left
            
                        root.right = right
            
                        all_trees.append(root)
            
            return all_trees
        
        return generate_trees(1, n)
        