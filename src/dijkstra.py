"""Dijkstra algorithm for our shortest path graph."""
from weighted_graph import Weighted
from priorityq import PriorityQueue

#  {'A':{'B': 7, 'C': 9}, 'B': {'D': 2, 'E': 4}, 'C': {'F': 6}, 'D':{}, 'E': {}, 'F': {}}


def dijkstra(weighted_graph, start_node):
    """Find the shortest path to nodes from starting node."""
    if not weighted_graph.has_node(start_node):
        raise IndexError('Node not in this weighted graph.')
    current_node = {start_node: 0}
    visited = {}
    priorityq = PriorityQueue()
    priorityq.insert(current_node, 0)
    while len(priorityq) > 0:
        current_node = priorityq.pop()
        next_nodes = weighted_graph[list(current_node.keys())[0]]
        for key, value in next_nodes.items():
            distance_from_start_node = value + list(current_node.values())[0]
            priorityq.insert(
                {key: distance_from_start_node}, distance_from_start_node
            )
            if key in visited and distance_from_start_node > visited[key]:
                continue
            visited.update({key: distance_from_start_node})
    return visited
