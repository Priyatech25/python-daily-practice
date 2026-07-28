"""
Day 46 - Clone Graph

Problem:
Given a reference to a node in a connected graph,
return a deep copy (clone) of the graph.

Each node contains:
- value
- list of neighbors

Example:

1 ---- 2
|      |
|      |
4 ---- 3

Output:
A new graph with the same structure.
"""


# Graph Node
# -------------------------

class Node:

    def __init__(self, val):
        self.val = val
        self.neighbors = []

# Clone Graph
# -------------------------

def clone_graph(node):

    if node is None:
        return None

    visited = {}

    def dfs(current):

        if current in visited:
            return visited[current]

        copy = Node(current.val)

        visited[current] = copy

        for neighbor in current.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)


# Display Graph
# -------------------------

def print_graph(node):

    visited = set()

    def dfs(current):

        if current in visited:
            return

        visited.add(current)

        print("Node", current.val, "->",
              [neighbor.val for neighbor in current.neighbors])

        for neighbor in current.neighbors:
            dfs(neighbor)

    dfs(node)



# Create Sample Graph
# -------------------------

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

print("Original Graph:")
print_graph(node1)

print()

cloned = clone_graph(node1)

print("Cloned Graph:")
print_graph(cloned)