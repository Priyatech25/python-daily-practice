# DAY 21 - DSA Practice (Topological Sort)

from collections import deque

def topological_sort(graph):
    
    indegree = {node: 0 for node in graph}

    # Calculate indegree
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    # Queue for nodes with indegree 0
    queue = deque([node for node in indegree if indegree[node] == 0])

    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order


# Graph (DAG)
graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    1: [],
    0: []
}

print("Topological Sort Order:")
print(topological_sort(graph))