"""Deque Composition."""
from dll import DoubleLinkedList


class Deque(object):
    """Class deque for deque composition."""

    def __init__(self):
        """Init for deque."""
        self._new_dll = DoubleLinkedList()

    def append(self, val):
        """Enqueue function for queue pushes value to head."""
        return self._new_dll.push(val)

    def appendleft(self, val):
        """Append vals to the front of deque."""
        return self._new_dll.append(val)

    def pop(self):
        """Pop from dll."""
        return self._new_dll.pop()

    def popleft(self):
        """Shift for popleft."""
        return self._new_dll.shift()

    def peek(self):  # pragma no cover
        """Return a new value without dequeuing it."""
        print(self._new_dll.head.data)

    def peekleft(self):  # pragma no cover
        """Return a new value from the left without dequeing it."""
        print(self._new_dll.tail.data)

    def __len__(self):
        """Length function for the queue."""
        return len(self._new_dll)
