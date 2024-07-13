import heapq

def dijkstra(adj_list, start):
    # initializes the distance to each node as infinity.
    distances = {node: float('inf') for node in adj_list}
    start = 'B'
    distances[start] = 0

    # Priority queue to track nodes and current shortest distance
    priority_queue = [(0, start)]

    while priority_queue:#execute as long as the priority_queue is not empty.
       
        current_distance, current_node = heapq.heappop(priority_queue)

        # shorter path to this node has already been processed, so the algorithm skips
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in adj_list[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                #if current node distance is small than already been processed, put it in queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

adj_list = {
    'A': {'B': 3, 'C': 8},
    'B': {'A': 3, 'C': 2, 'E': 5},
    'C': {'A': 8, 'B': 2, 'D': 1, 'E': 6},
    'E': {'B': 5, 'C': 6, 'D': 2, 'F': 5},
    'D': {'C': 1, 'E': 2, 'F': 3},
    'F': {'D': 3, 'E': 5}
}

distances = dijkstra(adj_list, 'A')
print("Shortest distances from node A:")
for node, distance in distances.items():
    print(f"Node {node}: {distance}")
    
