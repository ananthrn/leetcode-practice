# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        def serializeHelper(rootNode):
            if rootNode is None:
                data.append("#")
                return
            
            data.append(str(rootNode.val))
            
            serializeHelper(rootNode.left)
            serializeHelper(rootNode.right)
        
        serializeHelper(root)
        
        return " ".join(data)
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        dataDeque = collections.deque(data.split())
        def deserializeHelper(dataDeque) -> TreeNode:
            if len(dataDeque) == 0:
                return None
            
            val = dataDeque.popleft()
            if val == "#":
                return None
            
            root = TreeNode(int(val))
            root.left = deserializeHelper(dataDeque)
            root.right = deserializeHelper(dataDeque)
            
            return root
        
        return deserializeHelper(dataDeque)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))