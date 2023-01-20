
class DSU:
    def __init__(self, n: int):
        self.par = list(range(n+1))
    
    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x: int, y: int):
        parx, pary = self.find(x), self.find(y)
        
        if parx != pary:
            self.par[pary] = parx
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAccountNum = {}
        
        dsu = DSU(len(accounts))
        
        for accountNum, emails in enumerate(accounts):
            for email in emails[1:]:
                if email in emailToAccountNum:
                    oldVal = emailToAccountNum[email]
                    dsu.union(oldVal, accountNum)
                else:
                    emailToAccountNum[email] = accountNum
        
        accountNumToEmails = collections.defaultdict(list)
        
        for email, accountNum in emailToAccountNum.items():
            accountNumToEmails[dsu.find(accountNum)].append(email)
        
        ans = []
        
        ans = [
            [accounts[accountNum][0]] + sorted(emails) for accountNum, emails in accountNumToEmails.items()
        ]
        
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         emailToAccountNum = {}
        
#         dsu = DSU(len(accounts))
#         for accountNum, account in enumerate(accounts):
#             for email in account[1:]:
#                 print("email", email)
#                 print("accountNum of email: " ,emailToAccountNum.get(email, -1))
#                 print()
#                 if email in emailToAccountNum:
#                     oldVal = emailToAccountNum[email]
#                     dsu.union(oldVal, accountNum)
#                 else:
#                     emailToAccountNum[email] = accountNum
        
#         accNumToEmails = {}
        
#         for email, accountNum in emailToAccountNum.items():
#             if dsu.find(accountNum) in accNumToEmails:
#                 accNumToEmails[dsu.find(accountNum)].append(email)
#             else:
#                 accNumToEmails[dsu.find(accountNum)] = [email]
            
#         ans = []
#         for accountNum, emails in accNumToEmails.items():
#             emailList = [accounts[accountNum][0]] + sorted(emails)
#             ans.append(emailList)
#         return ans


            
                
        