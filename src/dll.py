"""Write an implementation of linked lists in Python."""


class Node(object):
    """Node class for use in double linked list."""

    def __init__(self, data, next_node=None, prior_node=None):
        """Initialize a node when adding to the linked list."""
        self.data = data
        self.next_node = next_node
        self.prior_node = prior_node


class DoubleLinkedList(object):
    """Double linked version of a list."""

    def __init__(self):
        """Initialize an empty double linked list."""
        self._length = 0
        self.tail = None
        self.head = None

    def push(self, val):
        """Push a value to the head of the list."""
        if not val:
            raise TypeError('Please provide a not null value.')
        self._length += 1
        if self.tail is None and self.head is None:
            new_node = Node(val)
            self.tail = new_node
            self.head = new_node
        else:
            new_node = Node(val, None, self.head)
            self.head.next_node = new_node
            self.head = new_node

    def append(self, val):
        """Append a val to the tail of a list."""
        if not val:
            raise TypeError('Please provide a not null value.')
        self._length += 1
        if self.tail is None and self.head is None:
            new_node = Node(val)
            self.tail = new_node
            self.head = new_node
        else:
            new_node = Node(val, self.tail, None)
            self.tail.prior_node = new_node
            self.tail = new_node

    def pop(self):
        """Pop pops from the head of the list."""
        if not self.head:
            raise IndexError(
                'There\'s nothing to remove from the linked list.')
        self._length -= 1
        if self.head == self.tail:
            last_pop = self.head
            self.head = None
            self.tail = None
            return last_pop.data
        popped = self.head
        self.head = self.head.prior_node
        popped.prior_node = None
        self.head.next_node = None
        return popped.data

    def shift(self):
        """Remove the node from the tail of the list."""
        if not self.head:
            raise IndexError(
                'There\'s nothing to remove from the linked list.')
        self._length -= 1
        if self.head == self.tail:
            last_pop = self.head
            self.head = None
            self.tail = None
            return last_pop.data
        shifted = self.tail
        self.tail = self.tail.next_node
        shifted.next_node = None
        self.tail.prior_node = None
        return shifted.data

    def __len__(self):
        """Return the length of the double linked list."""
        return self._length

    def remove(self, val):
        """Remove a node with the value provided."""
        if val is None:
            raise TypeError(
                'That value is not in this particular linked list.')
        if self.head.data == val:
            self.pop()
        elif self.tail.data == val:
            self.shift()
        current_node = self.head
        while current_node is not None:
            if current_node.data != val:
                current_node = current_node.prior_node
            else:
                new_next_node = current_node.next_node
                new_prior_node = current_node.prior_node
                current_node.next_node.prior_node = new_prior_node
                current_node.prior_node.next_node = new_next_node
                current_node.next_node = None
                current_node.prior_node = None
                self._length -= 1
                break
