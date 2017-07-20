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
        paths = {}
        while priorityq.size() > 0:
            current_node = priorityq.pop()
            next_nodes = self[current_node[0]]
            for key, value in next_nodes.items():
                distance_from_start_node = value + current_node[1]
                if key not in visited or distance_from_start_node < visited[key]:
                    if key == start_node:
                        continue
                    visited.update({key: distance_from_start_node})
                    path = current_node[0] + key
                    paths[path] = distance_from_start_node
                    priorityq.insert(
                        (key, distance_from_start_node), distance_from_start_node
                    )
        print(paths)
        return visited

    def bellman_ford(self, start_node):
        """Find the shortest path using Bellman-Ford."""
        #  If it doesn't have the node, raise an error.
        if not self.has_node(start_node):
            raise IndexError('Node not in this weighted graph.')
        #  This is the dictionary of the nodes that we'll be iterating over.
        #  Each node starts out as infinity
        nodes_dict = {key: float('Inf') for key in self.nodes()}
        nodes_dict[start_node] = 0
        traversed_edges = []
        #  Perform the whole iteration N - 1 times.
        # import pdb; pdb.set_trace()
        for i in range(len(self.nodes()) - 1):
            #  Iterate over each node in the nodes_dict dictionary
            for node, value in nodes_dict.items():
                #  If the node is in the graph, then do the following:
                if node in self:  # I don't remember why this is here, the node will be in the graph
                    #  Look at the nodes neighbors
                    neighbors = self[node]
                    #  For each of given nodes neighbors
                    for neighbor in neighbors:
                        #  If it is equal to the start node
                        if node == start_node and i == 0:
                            #  Then assign that nodes weight to the value in the nodes_dict
                            new_length = neighbors[neighbor]
                            nodes_dict.update({neighbor: new_length})
                        #  Else, if the value isn't the start node and it has a value
                        #  of infinity, continue to next neighbor since we haven't reached that
                        #  node yet.
                        elif value == float('Inf'):
                            continue
                        #  Otherwise, if it's not equal to the start node and it
                        #  has a weight, then update it the nodes_dict dictionary
                        else:
                            distance = neighbors[neighbor] + value
                            if (node, neighbor) in traversed_edges and distance < nodes_dict[neighbor]:
                                return ("Negative cycle detected.")
                            if distance > nodes_dict[neighbor]:
                                continue
                            nodes_dict[neighbor] = distance
                            traversed_edges.append((node, neighbor))
        return nodes_dict
        #  It is doing a breadfirst traversal, so it will not traverse the tree itself.
        #  It's going to look at whatever node is next in the nodes_dct dictionary, see (1)
        #  below
        #  Need to modify this to start from any node.


#  if key in visited and distance_from_start_node > visited[key]:
#   continue

# {'A': {'B': 7, 'C': 9}, 'B': {'D': 2, 'E': 4}, 'C': {'F': 6}}
# (1) {'A': inf, B': 7, 'C': 9, 'D': 9, 'E': 11, 'F': 15}
