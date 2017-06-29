"""Implement a priority queue using binary heap."""

#  [{1: 0}, {100: 1}, {33: 2}, {44: 3}, {2: 0}]


    # def heapify(self, iterable):
    #     """Function that will be used in init and other methods."""
    #     heap_list = iterable
    #     for item in heap_list[::-1]:
    #         item_index = heap_list.index(item)
    #         parent = (item_index - 1) // 2
    #         while item_index > 0:
                    
        #             if list(heap_list[parent].values())[0] < list(heap_list[parent].values())[0]:
        #                 curr_val = heap_list[parent]
        #                 heap_list[parent] = heap_list[item_index]
        #                 heap_list[item_index] = curr_val
        #                 item_index = parent
        #                 parent = (item_index - 1) // 2
        #             else:
        #                 break
    #     return heap_list


class PriorityQueue(object):
    """Implement a priority queue."""

    def __init__(self):
        """Initialize our priority queue."""
        self._heap = []

    def heapify(self, iterable):
        """Function to heapify our dictionary in self._heap."""
        heap_list = iterable
        for item in heap_list[::-1]:
            item_index = heap_list.index(item)
            parent = (item_index - 1) // 2
            while item_index > 0:
                if list(heap_list[parent].values())[0] is 0 and list(heap_list[item_index].values())[0] is 0:
                    item_index = parent
                    parent = (item_index - 1) // 2
                elif list(heap_list[parent].values())[0] > 0 and list(heap_list[item_index].values())[0] is 0:
                    item_index = parent
                    parent = (item_index - 1) // 2
                elif list(heap_list[parent].values())[0] is 0 and list(heap_list[item_index].values())[0] > 0:
                    curr_val = heap_list[parent]
                    heap_list[parent] = heap_list[item_index]
                    heap_list[item_index] = curr_val
                    item_index = parent
                    parent = (item_index - 1) // 2
                elif list(heap_list[parent].values())[0] > 0 and list(heap_list[item_index].values())[0] > 0:
                    if list(heap_list[item_index].values())[0] < list(heap_list[parent].values())[0]:
                        curr_val = heap_list[parent]
                        heap_list[parent] = heap_list[item_index]
                        heap_list[item_index] = curr_val
                        item_index = parent
                        parent = (item_index - 1) // 2
                    else:
                        item_index = parent
                        parent = (item_index - 1) // 2
                else:
                    break
        return heap_list

    def insert(self, value, priority=0):
        """Insert a value into the priority queue with an optional priority."""
        if not isinstance(priority, int):
            raise TypeError("Must provide an integer for priority.")
        if priority < 0:
            raise ValueError("You may not use a negative priority. Priority must be 0 or greater.")
        self._heap.append({value: priority})
        if len(self._heap) > 1:
            self._heap = self.heapify(self._heap)

    def pop(self):
        """Pop function for removing highest priority item from queue."""
        pop_it = self._heap.pop(0)
        self.heapify(self._heap)
        return list(pop_it.keys())[0]

    def peek(self):
        """Return the highest priority item without removing from queue."""
        return list(self._heap[0].keys())[0]
