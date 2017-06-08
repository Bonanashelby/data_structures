# data_structures
Data Structures for Python 401 

#Pair_programmed with Kurt Maurer and Anna Shelby 


##Linked List Branch
#Implement a push(val), pop(), size(), search(val), remove(node), display(), len(the_list), print(the_list) function for this exercise. 
#Worked on creating a single linked list.
#Used all these methods for our single linked list in linked_list.py
#([1, 2, 3]) => (3) -> (2) -> (1)

##Stack Branch 
#Implement a push(val) and pop() functions for this exercise.
#Used the push and pop methods from the Linked List. 


##DLL Branch
#Implement the push(val), append(val), pop(), shift(), remove(val) and len() functions for this exercise.
#Worked on making our nodes point to each other in the double link list format.
#Where (none) <- (1) -> (2) -> (3) -> (none) and
#Where (none) <- (1) <- (2) <- (3) -> (none) and
#Where (1) is the head and (3) is the tail in this instance.


##Queue Branch 
#Implement a enqueue(), dequeue(), peek(), size() function for this exercise. 
#Worked on enqueue and dequeue with our double linked list methods.
#Used the shift and pop methods from our double linked list in dll.py.


##Binary Heap Branch
#Implement a pop() and push() function for this exercise.
#Worked on initialization and implementation of our the data structure itself.
#Ended up taking init logic into its own function to be used after each initialization, pop, and push.
#Tests prove functionality of the heapify method by always returning the smallest value at the same index (index 0).


#Priority Queue Branch
#Implement a pop(), peek(), insert(value) for this exercise.
#Worked on tests.


#Graph Branch
#Implement a nodes(), edges(), add_node(), add_edge(), del_nodes(), del_edges(), has_node(), neighbors(), adjacent().
#Drove TDD by writing tests before implementing the graph. Discovered we had to make changes to the tests as we pivoted our approach to various methods.
#All tests pass.


#Graph Traversal Branch
#Implement a breadth_first and depth_first traversal for our graph data structure.
#All tests pass, the stack and the queue were instrumental in making the traversals work.
