
from collections import defaultdict
class UnionFind:
    def __init__(self, stringSet):
        self.parent = dict()
        for string in stringSet:
            self.parent[string] = string
    
    def getRoot(self, string):
        par = self.parent[string]
        if par != string:
            self.parent[string] = self.getRoot(par)
        return self.parent[string]
    
    def checkSame(self, string1, string2):
        return self.getRoot(string1) == self.getRoot(string2)
    
    def union(self, string1, string2):
        root1 = self.getRoot(string1)
        root2 = self.getRoot(string2)
        
        if root1 == root2:
            return
        
        self.parent[root2] = root1
    
        
    

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1) != len(sentence2):
            return False
        
        unifiedSet = set(sentence1).union(sentence2)
        for string1, string2 in similarPairs:
            unifiedSet.add(string1)
            unifiedSet.add(string2)
            
        UF = UnionFind(unifiedSet)
        
        for string1, string2 in similarPairs:
            UF.union(string1, string2)
        
        return all([UF.checkSame(string1, string2) for (string1, string2) in zip(sentence1, sentence2)])
        
        
        
        