import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

def find_optimal_route(graph, start, destination):
    distances = dijkstra(graph, start)
    if distances[destination] == float('inf'):
        return None
    route = []
    node = destination

    while node != start:
        route.append(node)
        neighbors = graph[node]
        min_distance = float('inf')
        next_node = None
        for neighbor, weight in neighbors.items():
            if distances[neighbor] + weight == distances[node] and distances[neighbor] < min_distance:
                min_distance = distances[neighbor]
                next_node = neighbor
        if next_node is None or next_node in route:
            return None
        node = next_node

    route.append(start)
    route.reverse()
    return route

def get_graph_from_user():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for i in range(num_nodes):
        node = input(f"Enter node {i+1}: ")
        graph[node] = {}
        num_neighbors = int(input(f"Enter the number of neighbors for node {node}: "))
        for j in range(num_neighbors):
            neighbor, weight = input(f"Enter neighbor {j+1} and its weight for node {node} (separated by space): ").split()
            graph[node][neighbor] = int(weight)
    return graph

start_location = input("Enter the start location: ")
destination_location = input("Enter the destination location: ")
graph = get_graph_from_user()

optimal_route = find_optimal_route(graph, start_location, destination_location)

if optimal_route is None:
    print("No valid route exists from the start to the destination.")
else:
    print("Optimal Route:", ' -> '.join(optimal_route))


"""Enter the start location: a
Enter the destination location: e
Enter the number of nodes: 5
Enter node 1: a
Enter the number of neighbors for node a: 4
Enter neighbor 1 and its weight for node a (separated by space): b 3
Enter neighbor 2 and its weight for node a (separated by space): c 99
Enter neighbor 3 and its weight for node a (separated by space): d 7
Enter neighbor 4 and its weight for node a (separated by space): e 99
Enter node 2: b
Enter the number of neighbors for node b: 4
Enter neighbor 1 and its weight for node b (separated by space): a 3
Enter neighbor 2 and its weight for node b (separated by space): c 4
Enter neighbor 3 and its weight for node b (separated by space): d 2
Enter neighbor 4 and its weight for node b (separated by space): e 99
Enter node 3: c
Enter the number of neighbors for node c: 4
Enter neighbor 1 and its weight for node c (separated by space): a 99
Enter neighbor 2 and its weight for node c (separated by space): b 4
Enter neighbor 3 and its weight for node c (separated by space): d 5
Enter neighbor 4 and its weight for node c (separated by space): e 6
Enter node 4: d
Enter the number of neighbors for node d: 4
Enter neighbor 1 and its weight for node d (separated by space): a 7
Enter neighbor 2 and its weight for node d (separated by space): b 2
Enter neighbor 3 and its weight for node d (separated by space): c 5
Enter neighbor 4 and its weight for node d (separated by space): e 4
Enter node 5: e
Enter the number of neighbors for node e: 4
Enter neighbor 1 and its weight for node e (separated by space): a 99
Enter neighbor 2 and its weight for node e (separated by space): b 99
Enter neighbor 3 and its weight for node e (separated by space): c 6
Enter neighbor 4 and its weight for node e (separated by space): d 4
Optimal Route: a -> b -> d -> e"""
