# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Grammar:
    s := expression
    term := factor | factor {(*/) factor}
    factor := digit | '(' expression ')'
    digit := [0..9]
    """
    def expTree(self, s: str) -> 'Node':
        tokens = collections.deque(list(s))
        return self.parse_expression(tokens)
    
    def parse_expression(self, tokens):
        lhs = self.parse_term(tokens)
        
        while len(tokens) > 0 and tokens[0] in ['+', '-']:
            op = tokens.popleft()
            rhs = self.parse_term(tokens)
            lhs = Node(val = op, left=lhs, right=rhs)
        
        return lhs
    
    def parse_term(self, tokens):
        lhs = self.parse_factor(tokens)
        
        while len(tokens) >0 and tokens[0] in ['*', '/']:
            op = tokens.popleft()
            rhs = self.parse_factor(tokens)
            lhs = Node(val = op, left = lhs, right = rhs)
        
        return lhs
    
    def parse_factor(self, tokens):
        if tokens[0] == '(':
            tokens.popleft()
            val = self.parse_expression(tokens)
            tokens.popleft()
            return val
        else:
            val = tokens.popleft()
            return Node(val)
        
            
        
        