"""Test our linked_list implementation."""


import pytest

PARAMS_TABLE = [
    (1234, 1234)
]


@pytest.mark.parametrize('arg, result', PARAMS_TABLE)
def test_linked_list_head(arg, result):
    """Test our linked_list class."""
    from linked_list import LinkedList
    new_link = LinkedList(arg)
    assert new_link.head == result


@pytest.mark.parametrize('arg, result', PARAMS_TABLE)
def test_linked_list_tail(arg, result):
    """Test our linked_list class."""
    from linked_list import LinkedList
    new_link = LinkedList(arg, arg)
    assert new_link.tail == result


@pytest.mark.parametrize('arg, result', PARAMS_TABLE)
def test_node_data(arg, result):
    """Test our linked_list class."""
    from linked_list import Node
    new_link = Node(arg)
    assert new_link.data == result


@pytest.mark.parametrize('arg, result', PARAMS_TABLE)
def test_node_next(arg, result):
    """Test our linked_list class."""
    from linked_list import Node
    new_link = Node(arg)
    assert new_link.next_node == None


@pytest.mark.parametrize('arg, result', PARAMS_TABLE)
def test_linked_list_push(arg, result):
    """Test our linked_list class."""
    from linked_list import LinkedList, Node
    new_link = LinkedList()
    new_link.push(arg)
    assert new_link.head.data == result


