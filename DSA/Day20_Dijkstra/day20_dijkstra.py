# DAY 20 - DSA Practice (Dijkstra Algorithm)

import heapq

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Graph representation
graph = {
    0: {1: 4, 2: 1},
    1: {3: 1},
    2: {1: 2, 3: 5},
    3: {}
}

# Run algorithm
result = dijkstra(graph, 0)

print("Shortest distances from node 0:")
for node, distance in result.items():
    print(node, "->", distance)