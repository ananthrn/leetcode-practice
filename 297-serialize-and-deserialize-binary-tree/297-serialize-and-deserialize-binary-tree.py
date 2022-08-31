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
        serialized = ""
        def serializeHelper(rootNode):
            nonlocal serialized
            if rootNode:
                serialized += " " + str(rootNode.val)
                serializeHelper(rootNode.left)
                serializeHelper(rootNode.right)
            else:
                serialized = serialized + " #"
        
        serializeHelper(root)
        print("Serialized: ", serialized)
        return serialized
        
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        valList = data.split()
        ind = 0
        def deserializeHelper() -> TreeNode:
            nonlocal ind, valList
            print("ind: ", ind)
            
            if ind < len(valList):
                
                val = valList[ind]
                ind += 1
                if val == "#":
                    return None
                else:
                    rootNode = TreeNode(int(val))
                    rootNode.left = deserializeHelper()
                    rootNode.right = deserializeHelper()
                    return rootNode
            else:
                return None
        
        return deserializeHelper()
            
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))