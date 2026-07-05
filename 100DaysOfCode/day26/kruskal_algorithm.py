# Day 27 - Kruskal's Algorithm

class DisjointSet:
    def __init__(self, vertices):
        self.parent = list(range(vertices))

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False


def kruskal(vertices, edges):

    edges.sort(key=lambda edge: edge[2])

    ds = DisjointSet(vertices)

    mst = []
    total_weight = 0

    for u, v, weight in edges:

        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


vertices = 4

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, total_weight = kruskal(vertices, edges)

print("Edges in Minimum Spanning Tree:")

for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")

print("\nTotal Weight:", total_weight)