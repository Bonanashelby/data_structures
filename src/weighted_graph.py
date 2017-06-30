"""Graph Data Structure."""
from priorityq import PriorityQueue


class Weighted(dict):
    """Thi is our class for our graph."""

    def nodes(self):
        """Return a list of nodes in the graph."""
        return list(self.keys())

    def edges(self):
        """Return a list of edges in the graph."""
        empty_list = []
        for key, value in self.items():
            if value != {}:
                for neighbor, weight in value.items():
                    empty_list.append((key, neighbor, weight))
        return empty_list

    def add_node(self, val):
        """Add a new node with value to the graph."""
        if val in self.keys():
            raise ValueError("This value is already in your graph.")
        self[val] = {}
        # that they can only add a dictionary- no vals in dict that is anything but a dict

    def add_edge(self, val1, val2, weight):
        """Add a new edge to the graph."""
        self.setdefault(val1, {})[val2] = weight
        self.setdefault(val2, {})

    def del_nodes(self, val):
        """Delete the node containing val from list."""
        if val not in self.keys():
            raise ValueError("There is no value to delete.")
        for node in self.values():
            if val in node:
                del node[val]
        del self[val]

    def del_edges(self, val1, val2):
        """Delete the edge connecting val1 and val2 from the graph."""
        if val2 in self[val1]:
            del self[val1][val2]
        else:
            raise KeyError("There are not edges to delete.")

    def has_node(self, val):
        """True is node containing val is in graph, false otherwise."""
        return val in self

    def neighbors(self, val):
        """Return the list of all nodes connected to the node by edges."""
        if val not in self:
            raise ValueError('That value is not in the graph.')
        return self[val]

    def adjacent(self, val1, val2):
        """Return true is val1 and val2 connected, false otherwise."""
        if val1 not in self or val2 not in self:
            raise ValueError("The values are not in the graph.")
        return val2 in self[val1]

    # (('A', 0), 0) -> ('A', 0) -> ('A') -> {'B': 7, 'C': 9}
    def dijkstra(self, start_node):
        """Find the shortest path to nodes from starting node."""
        if not self.has_node(start_node):
            raise IndexError('Node not in this weighted graph.')
        current_node = (start_node, 0)
        visited = {}
        priorityq = PriorityQueue()
        priorityq.insert(current_node, 0)
        while priorityq.size() > 0:
            current_node = priorityq.pop()
            next_nodes = self[current_node[0]]
            for key, value in next_nodes.items():
                distance_from_start_node = value + current_node[1]
                priorityq.insert(
                    (key, distance_from_start_node), distance_from_start_node
                )
                if key in visited and distance_from_start_node > visited[key]:
                    continue
                visited.update({key: distance_from_start_node})
        return visited
