# DAY 15 - DSA Practice (Graph DFS)

# Graph using adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

visited = set()


# DFS function
def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)


print("DFS Traversal:")
dfs(0)