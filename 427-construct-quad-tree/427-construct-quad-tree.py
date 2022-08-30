"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def traverse(self, row_low, row_high, col_low, col_high, grid) -> 'Node':
        values = set([grid[row][col] 
                      for row in range(row_low, row_high + 1) 
                      for col in range(col_low, col_high + 1)])
        
        if len(values) == 0:
            return None
        elif len(values) == 1:
            val = next(iter(values))
            return Node(
                val= val,
                isLeaf=True,
                topLeft=None,
                topRight=None,
                bottomLeft=None,
                bottomRight=None
            )
        else:
            row_mid = (row_low + row_high)//2
            col_mid = (col_low + col_high)//2
            topLeft = self.traverse(
                row_low=row_low,
                row_high=row_mid,
                col_low=col_low,
                col_high=col_mid,
                grid=grid
            )
            bottomLeft = self.traverse(
                row_low=row_mid+1,
                row_high=row_high,
                col_low=col_low,
                col_high=col_mid,
                grid=grid
            )
            bottomRight = self.traverse(
                row_low=row_mid+1,
                row_high=row_high,
                col_low=col_mid+1,
                col_high=col_high,
                grid=grid
            )
            topRight = self.traverse(
                row_low=row_low,
                row_high=row_mid,
                col_low=col_mid+1,
                col_high=col_high,
                grid=grid
                
            )
            
            return Node(
                val=0,
                isLeaf=False,
                topLeft=topLeft,
                topRight=topRight,
                bottomLeft=bottomLeft,
                bottomRight=bottomRight
            )
        
    def construct(self, grid: List[List[int]]) -> 'Node':
        m, n = len(grid), len(grid[0])
        
        return self.traverse(
                row_low=0,
                row_high=m-1,
                col_low=0,
                col_high=n-1,
                grid=grid
        )
        