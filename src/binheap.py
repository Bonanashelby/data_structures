"""Binary Min Heap."""

#  test iterable = [3, 5, 2, 4, 9, 1, 7, 8, 10, 6]


class BinHeap(object):
    """Min Heap Data Structure."""

    def __init__(self, iterable=[]):
        """Initialize an empty min heap."""
        if not isinstance(iterable, list):
            raise TypeError(
                'None or list types are the only valid arguments supported.')
        heap_list = iterable
        for item in heap_list[::-1]:
            item_index = heap_list.index(item)
            parent = int((item_index - 1) / 2)
            while item_index > 0:
                if heap_list[item_index] < heap_list[parent]:
                    curr_val = heap_list[parent]
                    heap_list[parent] = heap_list[item_index]
                    heap_list[item_index] = curr_val
                    item_index = parent
                    parent = int((item_index - 1) / 2)
                else:
                    break
        self._iterable = heap_list

    def push(self, val):
        """Push a value onto the heap."""
        pass

    def pop(self):
        """Pop the min value from the heap, return it, and resort the heap."""
        pass
