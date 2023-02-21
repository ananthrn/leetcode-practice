import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node):
    
    def __init__(self, value="", leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode
        
        self.valueMap = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a // b,
        }
        
    def evaluate(self) -> int:
        if self.value in self.valueMap:
            leftValue = self.leftNode.evaluate()
            rightValue = self.rightNode.evaluate()
            
            return self.valueMap[self.value](leftValue, rightValue)
        else:
            return int(self.value)
        

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        def helper(postfix: List[str]) -> 'Node':
            if len(postfix) == 0:
                return None
            
            if postfix[-1] in {"+", "-", "*", "/"}:
                rootNode = TreeNode(value=postfix[-1])
                postfix.pop()
                rootNode.rightNode = helper(postfix)
                rootNode.leftNode = helper(postfix)
                return rootNode
            else:
                return TreeNode(value=postfix.pop())
                
        
        rootNode = helper(postfix)
        
        return rootNode
        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        