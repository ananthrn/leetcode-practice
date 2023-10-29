class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.parent = list(parent)
        self.n = n
        self.lcaTree = self.buildLCA()
    
    def buildLCA(self) -> List[List[int]]:
        lcaTree = [17 * [-1] for _ in range(self.n)]
        for node in range(self.n):
            lcaTree[node][0] = self.parent[node]
        
        for po in range(1, 17):
            for node in range(self.n):
                # print("node: ", node)
                # print("prevPowerParent: ", lcaTree[node][po-1])
                # print("prev of prev: ", -1 if lcaTree[node][po-1] == -1 else lcaTree[lcaTree[node][po-1]][po-1])
                # print()
                try:
                    lcaTree[node][po] = -1 if lcaTree[node][po-1] == -1 else lcaTree[lcaTree[node][po-1]][po-1]
                except:
                    print(f"Node: {node}, po: {po}")
        
        return lcaTree
    
    def getAncestorHelper(self, node:int, k: int) -> int:
        
        currentNode = node
        currentTwoPowerExp = 0
        while currentNode!= -1 and k > 0:
            if k%2 == 1:
                currentNode = self.lcaTree[currentNode][currentTwoPowerExp]
            
            k = k//2 
            currentTwoPowerExp += 1
        return currentNode
            
        
    def getKthAncestor(self, node: int, k: int) -> int:
        return self.getAncestorHelper(node, k)


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)