import heapq
import numpy as np

#Get the closest vertex in the graph to match the users position
def define_starting_vertex(graph, user_position):
    return min(graph.keys(), key=lambda x: np.linalg.norm(np.array(x) - np.array(user_position)))

def dijkstra(graph, user_position):
    start = define_starting_vertex(graph, user_position)
    print(start)
    # distances, previous = {}, {}
    # for u in graph:
    #     distances[u] = float("inf") #Distance from start
    #     previous[u] = None #Successor vertex
    #
    # distances[start] = 0 #Distance from start
    #
    # heap = []
    # heapq.heappush(heap, (0, start))
    #
    # while heap:
    #     distance, current = heapq.heappop(heap)
    #
    #     #Shorter path already found
    #     if distance > distances[current]:
    #         continue
    #
    #     # Traverse through neighbors
    #     for neighbor, cost in graph[current]:
    #         pass
