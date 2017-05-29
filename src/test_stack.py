"""Our test file for our stack class."""
import pytest


@pytest.fixture
def the_stack():
    """Stack fixture."""
    from stack import Stack
    the_stack = Stack([1, 2, 3, 4])
    return the_stack


def test_stack_push(the_stack):
    """Test for pushing to stack."""
    the_stack.push(5)
    assert the_stack._newLinkedList.head.data == 5


def test_stack_pop(the_stack):
    """Test for popping to stack."""
    the_stack.pop()
    assert the_stack._newLinkedList.head.data == 3


def test_stack_pop_except_error():
    """Test for pop exception error and should get index errror."""
    from stack import Stack
    empty_stack = Stack()
    with pytest.raises(IndexError):
        empty_stack.pop()


def test_stack_len_of_stack(the_stack):
    """Test for length to stack."""
    assert len(the_stack) == 4


def test_search_stack():
    """Test to make sure stack is not accessing search method."""
    with pytest.raises(AttributeError):
        the_stack.search(4)


def test_remove_stack():
    """Test to make sure stack is not accessing remove method."""
    with pytest.raises(AttributeError):
        the_stack.remove(4)
