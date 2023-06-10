# class UnionFind:
#     def __init__(self, n):
#         self.rank = [1] * n
#         self.parent = [i for i in range(n)]
#
#     def find(self, x) -> int:
#         while x != self.parent[x]:
#             self.parent[x] = self.parent[self.parent[x]]
#             x = self.parent[x]
#         return x
#
#     def union(self, x1, x2):
#         p1, p2 = self.find(x1), self.find(x2)
#         if p1 == p2:
#             return False
#
#         if self.rank[p1] > self.rank[p2]:
#             self.parent[p2] = p1
#             self.rank[p1] += 1
#         else:
#             self.parent[p1] = p2
#             self.rank[p2] += 1
#         return True

from Algorithms.UnionFind import UnionFind

def accountsMerge(accounts):
    # email : parentIndex
    email_to_parent = {}
    length = len(accounts)
    union_find = UnionFind(length)

    for i in range(length):
        for j in range(1, len(accounts[i])):
            email = accounts[i][j]
            if email in email_to_parent:
                # since hashmap is email: index_of_acc
                # we should use UnionFind.find to look for the parent
                prev_par = union_find.find(email_to_parent[email])
                union_find.union(i, prev_par)
            else:
                # store the index of account
                # which is the starting index in parent arr in UnionFind to lookup the parent
                email_to_parent[email] = i

    account_emails = {}

    for email, acc_index in email_to_parent.items():
        par = union_find.find(acc_index)
        if par in account_emails:
            account_emails[par].append(email)
        else:
            account_emails[par] = [email]

    res = []
    for acc_index, emails in account_emails.items():
        res.append([accounts[acc_index][0]] + sorted(emails))

    return res




