"""Test our linked_list implementation."""


import pytest


@pytest.fixture
def linked_list():
    """Instantiate a  for testing."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    return linked_list


def test_linked_list_head(linked_list):
    """Test our linked_list class."""
    assert hasattr(linked_list, 'head')


def test_iterable_linked_list():
    """Test values of initialized linked list."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3])
    assert len(linked_list) == 3
    assert linked_list.head.data == 3


def test_iterable_linked_list_exception():
    """Ensure exception raised if a non-iterable is passed as argument."""
    from linked_list import LinkedList
    with pytest.raises(TypeError):
        new_link = LinkedList(1)


def test_linked_list_push(linked_list):
    """Test that push makes a new head of the list."""
    linked_list.push(5)
    assert linked_list.head.data == 5


def test_linked_list_push_three(linked_list):
    """Test attributes with three items in the linked list."""
    linked_list.push(5)
    linked_list.push(3)
    linked_list.push(2)
    assert linked_list.head.data == 2
    assert linked_list.head.next_node.data == 3
    assert linked_list.head.next_node.next_node.data == 5


def test_linked_list_popped(linked_list):
    """Test pop method."""
    linked_list.push(5)
    linked_list.push(2)
    assert linked_list.pop() == 2
    assert linked_list.head.data == 5
    assert linked_list.pop() == 5


def test_linked_list_popped_exception(linked_list):
    """Raise exception if empty."""
    with pytest.raises(IndexError):
        linked_list.pop()


def test_linked_list_length(linked_list):
    """Verify we can return the length of the linked list."""
    linked_list.push(3)
    linked_list.push(4)
    assert len(linked_list) == 2
    linked_list.push(5)
    assert len(linked_list) == 3
    linked_list.pop()
    assert len(linked_list) == 2


def test_linked_list_search(linked_list):
    """Test the linked list search method."""
    from linked_list import LinkedList
    obj_1 = 'apple'
    obj_2 = 45
    obj_3 = ['stringy']
    linked_list = LinkedList([obj_1, obj_2, obj_3])
    assert linked_list.search(45) == obj_2
    assert linked_list.search(['stringy']) == obj_3
    assert linked_list.search(obj_1) == 'apple'
    assert linked_list.search(47) is None


def test_linked_list_remove():
    """Test proper remove functionality."""
    from linked_list import LinkedList
    new_list = LinkedList([1, 2, 3, 4])
    new_list.remove(1)
    assert new_list.search(1) is None
    new_list.remove(4)
    assert new_list.search(4) is None
    assert new_list.search(3) == new_list.head.data
    new_list.push(5)
    new_list.remove(3)
    assert new_list.search(3) is None
    assert new_list.search(5) == new_list.head.data


def test_linked_list_display():
    """Our display list."""
    from linked_list import LinkedList
    new_list = LinkedList([1, 2, 3, 4])
    assert new_list.display() == "(4, 3, 2, 1)"
