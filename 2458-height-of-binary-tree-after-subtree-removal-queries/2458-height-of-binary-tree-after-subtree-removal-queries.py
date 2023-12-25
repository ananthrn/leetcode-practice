# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sortedcontainers
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        valDepthMap = dict()
        valHeightMap = dict()
        depthHeightList = collections.defaultdict(sortedcontainers.SortedList)
        
        def dfs(node: Optional[TreeNode], currentDepth: int):
            if node is None:
                return -1
            
            valDepthMap[node.val] = currentDepth
            leftHeight = dfs(node.left, currentDepth + 1)
            rightHeight = dfs(node.right, currentDepth + 1)
            thisHeight = max(currentDepth, leftHeight, rightHeight)
            depthHeightList[currentDepth].add(thisHeight)
            valHeightMap[node.val] = thisHeight
            return thisHeight
        
        def processQuery(queryVal: int) -> int:
            nodeDepth = valDepthMap[queryVal]
            heightList = depthHeightList[nodeDepth]
            
            if len(heightList) == 0:
                assert False, "Should not happen"
            elif len(heightList) == 1:
                return nodeDepth - 1 # no other node is on this depth
            else:
                if valHeightMap[queryVal] != heightList[-1]:
                    return heightList[-1]
                else:
                    return heightList[-2]
                
        dfs(root, 0)
        
        print("valDepthMap: ", valDepthMap)
        print("valHeightMap: ", valHeightMap)
        print("depthHeightList: ", dict(depthHeightList))
        
        ans = list(map(processQuery, queries))
        
        return ans
        
        
        