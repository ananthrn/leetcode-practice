"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        data = ""
        def serializeHelper(rootNode: 'Node') -> None:
            nonlocal data
            if rootNode is None:
                data += " #"
            else:
                
                data += " " + str(rootNode.val)
                if rootNode.children is not None:
                    numChildren = len(rootNode.children)
                    data += " " + str(numChildren)
                    
                    for child in rootNode.children:
                        serializeHelper(child)
                else:
                    data += " " + "0"
        
        
        serializeHelper(root)
        
        # print("data: ", data)
        return data
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        dataList = deque(data.split())
        def deserializeHelper() -> 'Node':
            nonlocal dataList
            strVal = dataList.popleft()
            
            
            if strVal == "#":
                return None
            else:
                val = int(strVal)
                numChildren = int(dataList.popleft())
                
                if numChildren == 0:
                    return Node(val=val, children=[])
                else:
                    children = [deserializeHelper() for childNum in range(numChildren)]
                    return Node(val=val, children=children)
            
            return None
        
        return deserializeHelper()
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))