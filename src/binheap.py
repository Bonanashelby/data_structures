"""Binary Min Heap."""


class Node(object):
    """Node class for use in min heap data structure."""

    def __init__(self, data, next_node=None, prior_node=None):
        """Initialize a node when adding to the heap."""
        self.data = data
        self.next_node = next_node
        self.prior_node = prior_node


class Heap(object):
    """Min Heap Data Structure."""

    def __init__(self):
        """Initialize an empty min heap."""
        self._length = 0
        self.parent = None
        self.left_child = None
        self.right_child = None

    # def push(self, val):
    #     """Push a value to the heap."""
    #     if not val:
    #         raise TypeError('Please provide the correct value.')
    #     self._length += 1 
    #     if self.parent = None:
    #         new_node = Node(val)
    #         self.parent = new_node
    #     else:
    #         new_node = Node(val,)
