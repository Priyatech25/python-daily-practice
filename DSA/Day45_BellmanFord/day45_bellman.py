# DAY 46 - Bellman Ford Algorithm

def bellman_ford(vertices, edges, source):
    dist = [float('inf')] * vertices
    dist[source] = 0

    # Relax edges V-1 times
    for _ in range(vertices - 1):
        for u, v