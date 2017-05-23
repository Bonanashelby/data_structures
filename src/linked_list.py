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
        if linkedlist empty set make the
        single node both the head and tail
        find next object and unhead it


    def pop(self):
        node_to_be_removed = self.head
        starting from tail, if its next node != self.head
        go to its next node and compare it until
        next node equals self.head
        set that node equal to self.head
        node_to_be_removed = node.next node
        return node_to_be_removed



    def len(self):  # size
        count = 0
        starting from self.tail, go to its next_node 
        add 1 to count, then go to that node's next node
        until you reach self.head, where None
        #possible recursion


    def search(self, val):
        if val != self.head, go it its node.next_node
        and run the same comparison
        until val == node.data
        else return None
        # also recursion

    def remove(self, node):
        run search and find the value, but remove it
        if tail, set its next_node to be the tail
        if head, set its values appropriately

    def display(self):
        print(('{},'.format(the_nodes)))