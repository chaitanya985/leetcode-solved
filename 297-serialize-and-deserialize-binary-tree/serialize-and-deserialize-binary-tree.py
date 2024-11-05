# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):

        if root is None:
            
            return ''
        
        res = []

        def preorder(root):
        
            if root is None:
        
                res.append("#,")
        
                return
        
            res.append(str(root.val) + ",")
        
            preorder(root.left)
        
            preorder(root.right)

        preorder(root)
        
        return ''.join(res)

    def deserialize(self, data):
        
        if not data:
        
            return None
        
        vals = data.split(',')

        def inner():
        
            first = vals.pop(0)
        
            if first == '#':
        
                return None
        
            return TreeNode(int(first), inner(), inner()) 
        
        return inner()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))