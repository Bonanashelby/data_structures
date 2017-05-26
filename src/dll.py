"""Write an implementation of linked lists in Python."""


class Node(object):
    def __init__(self, data, next_node=None, prior_node=None):
        self.data = data
        self.next_node = next_node
        self.prior_node = prior_node


class DoubleLinkedList(object):
    """Double linked version of a list"""

    def __init__(self):
        """Initialize an empty double linked list."""
        self._length = 0
        self.tail = None
        self.head = None

    def push(self, val):
        """Push a value to the head of the list."""
        if not val:
            raise TypeError('Please provide a not null value.')
        if self.tail is None and self.head is None:
            new_node = Node(val)
            self.tail = new_node
            self.head = new_node
            self._length += 1
        else:
            new_node = Node(val, None, self.head)
            self.head.next_node = new_node
            self.head = new_node
            self._length += 1


    def append(self, val):
        """Appends a val to the tail of a list."""
        if not val:
            raise TypeError('Please provide a not null value.')
        if self.tail is None and self.head is None:
            new_node = Node(val)
            self.tail = new_node
            self.head = new_node
            self._length += 1
        else:
            new_node = Node(val, self.tail, None)
            self.tail.prior_node = new_node
            self.tail = new_node
            self._length += 1


    def pop(self):
        """Pop pops from the head of the list."""
        if not self.head:
            raise IndexError('There\'s nothing to remove from the linked list.')
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


    def shift():
        """tail pop."""
        pass


    def __len__(self):
        return self._length


    def remove(self, val):
        if val is None:
            raise IndexError('That value is not in this particular linked list.')
        if self.head.data == val:
            print("I'm here")
            print(self.pop())
            print(self.head.data)
            return None
        current_node = self.head
        print(current_node.next_node.data)
        print(current_node.next_node.next_node.data)
        while current_node != None:
            if current_node.next_node.data != val:
                print('My value does not equal the current node.')
                current_node = current_node.next_node
            else:
                removed_node = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
                self._length -= 1
                if removed_node.next_node != None:
                    removed_node.next_node = None
                break
