import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [-1] * n
    dist[start] = 0
    pq = [(0, start)]

    steps = []
    steps.append((list(pq), dist[:], prev[:]))

    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            distance = dist[u] + weight
            if distance < dist[v]:
                dist[v] = distance
                prev[v] = u
                heapq.heappush(pq, (distance, v))
                steps.append((list(pq), dist[:], prev[:]))

    return dist, prev, steps

def print_steps_table(steps):
    print(f"{'Step':<5} {'Priority Queue':<30} {'Distances':<30} {'Predecessors':<30}")
    for i, (pq, dist, prev) in enumerate(steps):
        print(f"{i:<5} {str(pq):<30} {str(dist):<30} {str(prev):<30}")

def reconstruct_path(start, target, prev):
    path = []
    at = target
    while at != -1:
        path.append(at)
        at = prev[at]
    path.reverse()
    if path[0] == start:
        return path
    return []

# Example graph represented as an adjacency list
graph = [
    [(1, 10), (2, 3)],  # Node 0
    [(2, 1), (3, 2)],   # Node 1
    [(1, 4), (3, 8), (4, 2)],  # Node 2
    [(4, 7)],  # Node 3
    [(3, 9)]   # Node 4
]

start = 0
target = 4

# Run Dijkstra's algorithm
distances, predecessors, steps = dijkstra(graph, start)

# Reconstruct the path from start to target
path = reconstruct_path(start, target, predecessors)

# Print the results
print(f"Distance from node {start} to node {target} is {distances[target]}")
print("Path taken:", path)
print("\nSteps Table:")
print_steps_table(steps)
