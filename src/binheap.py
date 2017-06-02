"""Binary Min Heap."""


class BinHeap(object):
    """Min Heap Data Structure."""

    def __init__(self, iterable=None):
        """Initialize an empty min heap."""
        iterable = [3, 5, 2, 4, 9, 1, 7, 8, 10, 6]
        for item in iterable[::-1]:
            item_index = iterable.index(item)
            parent = int((item_index - 1) / 2)
            while item_index > 0:
                if iterable[item_index] < iterable[parent]:
                    curr_val = iterable[parent]
                    iterable[parent] = iterable[item_index]
                    iterable[item_index] = curr_val
                    item_index = parent
                    parent = int((item_index - 1) / 2)
                else:
                    break



    def push(self, val):
        """Push a value onto the heap."""
        while i > 0:
            #move that value up until it is the lesser val.
