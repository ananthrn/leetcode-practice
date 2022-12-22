class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        
        bolded = set()
        for word in words:
            start = 0
            findIndex = s.find(word, 0)
            
            while findIndex != -1:
                bolded = bolded.union(set(range(findIndex, findIndex + len(word))))
                findIndex = s.find(word, findIndex + 1)
        
        print("bolded: ", bolded)
        
        ans = []
        
        ind = 0
        
        while ind < len(s):
            if ind in bolded:
                ans.append("<b>")
                while ind < len(s) and ind in bolded:
                    ans.append(s[ind])
                    ind += 1
                ans.append("</b>")
            else:
                ans.append(s[ind])
                ind +=1
        
        return "".join(ans)
        