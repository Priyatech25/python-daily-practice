# Day 29 - Topological Sort (Kahn's Algorithm)

from collections import deque

def topological_sort(vertices, edges):

    graph = {i: [] for i in range(vertices)}
    indegree = [0] * vertices

    # Build graph and calculate indegree
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque()

    # Add all vertices with indegree 0
    for i in range(vertices):
        if indegree[i] == 0:
            queue.append(i)

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != vertices:
        print("Cycle detected! Topological Sort not possible.")
    else:
        print("Topological Order:")
        print(result)


vertices = 6

edges = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1)
]

topological_sort(vertices, edges)