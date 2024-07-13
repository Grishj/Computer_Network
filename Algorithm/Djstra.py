import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            distance = dist[u] + weight

            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(pq, (distance, v))

    return dist

# Example graph represented as an adjacency list
graph = [
    [(1, 10), (2, 3)],  # Node 0
    [(2, 1), (3, 2)],   # Node 1
    [(1, 4), (3, 8), (4, 2)],  # Node 2
    [(4, 7)],  # Node 3
    [(3, 9)]   # Node 4
]

start = 0
distances = dijkstra(graph, start)

for i in range(len(distances)):
    print(f"Distance from node {start} to node {i} is {distances[i]}")
