# Day 28 - Disjoint Set Union (Union-Find)

class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    # Find with Path Compression
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    # Union by Rank
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v

        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u

        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1


ds = DisjointSet(7)

ds.union(0, 1)
ds.union(1, 2)
ds.union(3, 4)
ds.union(5, 6)

print("Parent Array:")
print(ds.parent)

print("\nAre 0 and 2 connected?", ds.find(0) == ds.find(2))
print("Are 0 and 4 connected?", ds.find(0) == ds.find(4))

ds.union(2, 4)

print("\nAfter Union(2, 4):")
print("Are 0 and 4 connected?", ds.find(0) == ds.find(4))