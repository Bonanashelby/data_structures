"""Test our linked_list implementation."""


import pytest

# PARAMS_TABLE = [
#     (1234, 1234)
# ]


# @pytest.mark.parametrize('arg, result', PARAMS_TABLE)
def test_linked_list_head():
    """Test our linked_list class."""
    from linked_list import LinkedList
    new_link = LinkedList()
    assert hasattr(new_link, 'head')


def test_iterable_linked_list():
    """."""
    from linked_list import LinkedList
    new_link = LinkedList([1, 2, 3])
    assert len(new_link) == 3
    assert new_link.head == 3


def test_iterable_linked_list():
    """."""
    from linked_list import LinkedList
    with pytest.raises(TypeError):
        new_link = LinkedList(1)


def test_linked_list_push():
    """."""
    from linked_list import LinkedList
    new_link = LinkedList()
    new_link.push(5)
    assert new_link.head.data == 5


def test_linked_list_push_three():
    """."""
    from linked_list import LinkedList
    new_link = LinkedList()
    new_link.push(5)
    new_link.push(3)
    new_link.push(2)
    assert new_link.head.data == 2
    assert new_link.head.next_node.data == 3
    assert new_link.head.next_node.next_node.data == 5


def test_linked_list_popped():
    """."""
    from linked_list import LinkedList
    new_link = LinkedList()
    new_link.push(5)
    new_link.push(2)
    assert new_link.pop() == 2
    assert new_link.head.data == 5
    assert new_link.pop() == 5


def test_linked_list_popped_exception():
    """."""
    from linked_list import LinkedList
    new_link = LinkedList()
    with pytest.raises(IndexError):
        new_link.pop()


def test_linked_list_length():
    """."""
    from linked_list import LinkedList
    new_list = LinkedList()
    new_list.push(3)
    new_list.push(4)
    assert len(new_list) == 2
    new_list.push(5)
    assert len(new_list) == 3
    new_list.pop()
    assert len(new_list) == 2


def test_linked_list_search():
    """."""
    from linked_list import LinkedList
    obj_1 = 'apple'
    obj_2 = 45
    obj_3 = ['stringy']

    new_list = LinkedList([obj_1, obj_2, obj_3])
    assert new_list.search(45) == obj_2
    assert new_list.search(['stringy']) == obj_3
    assert new_list.search(obj_1) == 'apple'
    assert new_list.search(47) == None


def test_linked_list_remove():
    """."""
    from linked_list import LinkedList
    new_list = LinkedList([1, 2, 3, 4])
    new_list.remove(1)
    assert new_list.search(1) == None
    new_list.remove(4)
    assert new_list.search(4) == None
    assert new_list.search(3) == new_list.head.data
    new_list.push(5)
    new_list.remove(3)
    assert new_list.search(3) == None
    assert new_list.search(5) == new_list.head.data

# @pytest.mark.parametrize('arg, result', PARAMS_TABLE)
# def test_node_next(arg, result):
#     """Test our linked_list class."""
#     from linked_list import Node
#     new_link = Node(arg)
#     assert new_link.next_node == None


# @pytest.mark.parametrize('arg, result', PARAMS_TABLE)
# def test_linked_list_push(arg, result):
#     """Test our linked_list class."""
#     from linked_list import LinkedList, Node
#     new_link = LinkedList()
#     new_link.push(arg)
#     assert new_link.head.data == result

def test_linked_llist_display():
    """Our display list."""
    from linked_list import LinkedList
    new_list = LinkedList([1, 2, 3, 4])
    assert new_list.display() == "(4, 3, 2, 1)"
