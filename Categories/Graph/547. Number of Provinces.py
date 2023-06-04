def findCircleNum(isConnected) -> int:
    """
    More efficient
    """
    n = len(isConnected)
    visited = [False] * n

    def dfs(node):
        if visited[node]:
            return

        visited[node] = True
        for i in range(n):
            if isConnected[node][i]:
                dfs(i)

    res = 0
    for i in range(n):
        if not visited[i]:
            res += 1
            dfs(i)

    return res


# -------------- less efficient, both O(n2)

class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += 1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True


class Solution:
    def findCircleNum(self, isConnected) -> int:
        num_components = len(isConnected)
        union_find = UnionFind(num_components)


        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] and union_find.find(i) != union_find.find(j):
                    union_find.union(i, j)
                    num_components -= 1

        return num_components