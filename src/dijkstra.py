"""Dijkstra algorithm for our shortest path graph."""
from weighted_graph import Weighted
from priorityq import PriorityQueue


def dijkstra(weighted_graph, start_node):
    """Find the shortest path to nodes from starting node."""
    if not weighted_graph.has_node(start_node):
        raise IndexError('Node not in this weighted graph.')
    current_node = {start_node: 0}
    peeped = []  #  list of dictionaries
    priorityq = PriorityQueue()
    priorityq.insert(start_node.key, start_node.value)
    while len(priorityq) > 0:
        # current_node = priorityq.pop()
        # look at that nodes neighbors

        # insert neighbors into the queue with priority of
        # edge weight plus current node weight.

        # The priority queue automatically organizes them
        # by the minimum value, so we're good there.

        # We've looked at both of the current nodes neighbors,
        # so we're good to move on to the next node.

        # If the current node's weight is less than the one
        # in the peeped list, swap them out.

        # continue
