from sortedcontainers import SortedList

class TrieNode:
    def __init__(self,
                 id = 0,
                 children = dict(),
                 strings = SortedList(),
                ):
        self.id = id
        self.children = dict(children)
        self.strings = SortedList(strings)
class Trie:
    
            
    def __init__(self, products: List[str]):
        self.products = products
        self.root = TrieNode()
        self.nodes = 0
        for product in products:
            self.insert(product)
    
    def insert(self, string: str):
        curNode = self.root
        
        if string not in curNode.strings:
            curNode.strings.add(string)
            if len(curNode.strings) > 3:
                curNode.strings.pop()
        
        # print(f"-------Inserting {string}:--------")
        for ind, char in enumerate(string):
            
            if char not in curNode.children:
                self.nodes +=1
                curNode.children[char] = TrieNode(id = self.nodes)
            
            curNode = curNode.children[char]
            
            if string not in curNode.strings:
                curNode.strings.add(string)
                if len(curNode.strings) > 3:
                    curNode.strings.pop()
                    
#             print("substr: ", string[0: ind + 1])
#             print("curNode.id: ", curNode.id)
#             print("curNode.strings: ", curNode.strings)
#             print()
        
        # print(f"-------Finished Inserting {string}:--------")
    def getProducts(self, string: str):
        
        ans = []
        
        curNode = self.root
        print(f"-------Searching {string}:--------")
        for ind, char in enumerate(string):
            
            # print("curNode.strings: ", curNode.strings)
            nextNode = None
            
            if curNode is not None and char in curNode.children:
                nextNode = curNode.children[char]
            
            if nextNode is None:
                ans.append([])
            else:
                ans.append(list(nextNode.strings))
            
            # print("substr: ", string[0: ind + 1])
            # print("nextNode.id: ", nextNode.id)
            # print("nextNode.strings: ", nextNode.strings)
            # print()
            curNode = nextNode
        
        return ans
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie(products)
        ans= trie.getProducts(searchWord)
        
        return ans
        
        