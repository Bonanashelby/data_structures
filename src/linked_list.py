"""Write an implementation of linked lists in Python."""


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    """Linked version of a list"""
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def push(self, node_object):
        node_instantiation = Node(node_object, self.head)
        self.head = node_instantiation



    def __pop__(self):
        pass


    def __len__(self):
        pass


    def __repr__(self):
        pass

    def size(self):
        pass

    def search(self, val):
        pass

    def remove(self, node):
        pass

    def display(self):
        pass