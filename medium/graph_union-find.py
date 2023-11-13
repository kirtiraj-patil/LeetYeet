class DisjointSet:
    def __init__(self, n):
        # n nodes numbered from 1 - n, doing 1-based indexing. 0 is useless in that case
        self.rank = [0] * n
        self.parent = []
        for i in range(n + 1):
            self.parent.append(i)

    def getParent(self, u):
        print("called for ", u)
        if self.parent[u] == u:
            print("returning ", u)
            return u

        print(
            "trying to find the ultimate parent for: ",
            u,
            " current parent: ",
            self.parent[u],
        )
        self.parent[u] = self.getParent(self.parent[u])
        print("updated the parent to: ", self.parent[u])
        return self.parent[u]

    def unionByRank(self, u, v):
        pu = self.parent[u]
        pv = self.parent[v]

        if pu == pv:
            return

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

        print("done")

    def areConnected(self, u, v):
        pu = self.getParent(u)
        pv = self.getParent(v)
        if pu == pv:
            return True
        return False


d = DisjointSet(9)
d.unionByRank(1, 2)
d.unionByRank(2, 3)
d.unionByRank(2, 4)
d.unionByRank(5, 6)
d.unionByRank(6, 7)
d.unionByRank(1, 5)
print("2, 7 are connected: ", d.areConnected(2, 7))
