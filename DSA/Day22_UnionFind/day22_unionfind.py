# DAY 22 - DSA Practice (Union Find / Disjoint Set)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    # Find with Path Compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union by Rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


# Testing
uf = UnionFind(5)

uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

print("Parent Array:", uf.parent)

# Check if connected
print("0 and 2 connected:", uf.find(0) == uf.find(2))
print("1 and 4 connected:", uf.find(1) == uf.find(4))