"""Implement a graph depth and breadth traversal."""
from graph_1 import Graph
from stack import Stack
from que_ import Queue


def depth_first_traversal(graph, start):
    """Traverse a graph by depth."""
    if not isinstance(graph, Graph):
        raise TypeError('Must provide graph.')
    if not graph.has_node(start):
        raise KeyError('Node not in graph.')
    peeped = []
    stack = Stack()
    stack.push(start)
    while len(stack) > 0:
        node = stack.pop()
        if node not in peeped:
            peeped.append(node)
        for neighbor in graph._graph[node][::-1]:
            if neighbor not in peeped:
                stack.push(neighbor)
    return peeped


def breadth_first_traversal(graph, start):
    """Traverse a graph by breadth."""
    if not isinstance(graph, Graph):
        raise TypeError('Must provide graph.')
    if not graph.has_node(start):
        raise KeyError('Node not in graph.')
    peeped = []
    queue = Queue()
    queue.enqueue(start)
    while len(queue) > 0:
        node = queue.dequeue()
        if node not in peeped:
            peeped.append(node)
        for neighbor in graph._graph[node]:
            if neighbor not in peeped:
                queue.enqueue(neighbor)
    return peeped
