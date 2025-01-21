class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
class Solution:
    # 196 ms, 82.09%. 
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         parent = {}

#         def find(email):
#             if parent[email] != email:
#                 parent[email] = find(parent[email])  # Path compression
#             return parent[email]

#         def union(email1, email2):
#             parent1, parent2 = find(email1), find(email2)
#             if parent1 != parent2:
#                 parent[parent2] = parent1

#         # Step 1: Initialize Union-Find
#         email_to_name = {}
#         for account in accounts:
#             name = account[0]
#             first_email = account[1]
#             for email in account[1:]:
#                 parent.setdefault(email, email)
#                 union(first_email, email)
#                 email_to_name[email] = name

#         # Step 2: Group emails by root
#         components = defaultdict(list)
#         for email in parent:
#             root = find(email)
#             components[root].append(email)

#         # Step 3: Format the output
#         merged_accounts = []
#         for root, emails in components.items():
#             merged_accounts.append([email_to_name[root]] + sorted(emails))

#         return merged_accounts
