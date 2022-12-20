class TrieNode:
    def __init__(self):
        self.children = dict()
        self.fileContent = ""

class Trie:
    def __init__(self):
        self.rootNode = TrieNode()
    
    def createPath(self, path: List[str], fileContent: str):
        currentNode = self.rootNode
        
        for dirName in path:
            if dirName not in currentNode.children:
                currentNode.children[dirName] = TrieNode()
            currentNode = currentNode.children[dirName]
        
        currentNode.fileContent += fileContent
    
    def getDirectory(self, path: List[str]) -> List[str]:
        currentNode = self.rootNode
        
        for dirName in path:
            currentNode = currentNode.children[dirName]
        
        # print("path: ", path)
        # print("path")
        # print("currentNode: ", currentNode.children)
        # print("currentNode.fileContent: ", currentNode.fileContent)
        return path[-1:] if currentNode.fileContent != "" else sorted(currentNode.children.keys())
        
    def getFileContent(self, path: List[str]) -> str:
        currentNode = self.rootNode
        
        for dirName in path:
            currentNode = currentNode.children[dirName]
        
        return currentNode.fileContent
        
class FileSystem:

    def __init__(self):
        self.trie = Trie()

    def ls(self, path: str) -> List[str]:
        splitPath = path.split("/")[1:] if path != "/" else []
        return self.trie.getDirectory(splitPath)

    def mkdir(self, path: str) -> None:
        splitPath = path.split("/")[1:] if path != "/" else []
        self.trie.createPath(splitPath, "")

    def addContentToFile(self, filePath: str, content: str) -> None:
        splitPath = filePath.split("/")[1:] if filePath != "/" else []
        self.trie.createPath(splitPath, content)

    def readContentFromFile(self, filePath: str) -> str:
        splitPath = filePath.split("/")[1:] if filePath != "/" else []
        return self.trie.getFileContent(splitPath)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)