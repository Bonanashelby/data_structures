"""Test double linked list class."""
import pytest


@pytest.fixture
def dll():
    """Instantiate a dll for testing."""
    from dll import DoubleLinkedList
    double_link = DoubleLinkedList()
    return double_link


def test_dll_initialization(dll):
    """Test that there's nothing initialized."""
    assert dll.tail is None
    assert dll.head is None


def test_dll_push_raises_type_error(dll):
    """Test that the value error  is raised."""
    with pytest.raises(TypeError):
        dll.push()


def test_dll_push_pushes_value(dll):
    """Test that the push pushes a value to head of list."""
    dll.push(1)
    assert dll.tail.data == 1
    assert dll.head.data == 1


def test_dll_push_head_and_tail_change(dll):
    """Test if second item is pushed in. Head and tail are seperate values."""
    dll.push(1)
    dll.push(2)
    assert dll.tail.data == 1
    assert dll.head.data == 2


def test_dll_push_3(dll):
    """Test that if 3 vals are pushed there is a head, prior node and tail."""
    dll.push(1)
    dll.push(2)
    dll.push(3)
    assert dll.tail.data == 1
    assert dll.head.prior_node.prior_node.data == 1
    assert dll.head != dll.head.prior_node
    assert dll.head.data == 3
    assert dll.head.prior_node.next_node.data == 3
    assert dll.tail.next_node.data == 2


def test_dll_pop_index_error(dll):
    """Test that the Index Error is raised if no val is popped."""
    with pytest.raises(IndexError):
        dll.pop()


def test_dll_pop_only_has_one_item(dll):
    """Test that pop only has one item and both are head and tail none vals."""
    dll.push(1)
    dll.push(2)
    assert dll.pop() == 2
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.head.next_node is None
    assert dll.pop() == 1
    assert dll.head is None
    assert dll.tail is None


def test_dll_append_raises_type_error(dll):
    """Test that we get a type error."""
    with pytest.raises(TypeError):
        dll.append()


def test_dll_appends_a_value(dll):
    """Ensure tail and head are the same."""
    dll.append(1)
    assert dll.tail.data == 1
    assert dll.head.data == 1


def test_dll_appends_3_values(dll):
    """Verify node connections after appending 3 values."""
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert dll.tail.data == 3
    assert dll.head.data == 1
    assert dll.head.next_node is None
    assert dll.tail.prior_node is None
    assert dll.tail.next_node.data == 2
    assert dll.head.prior_node.data == 2
    assert dll.head.prior_node.next_node.data == 1
    assert dll.tail.next_node.prior_node.data == 3


def test_dll_shift_index_error(dll):
    """Test that the Index Error is raised if no val is shifted."""
    with pytest.raises(IndexError):
        dll.shift()


def test_dll_shift_only_has_one_item(dll):
    """Test that node connections after shifting."""
    dll.push(1)
    dll.push(2)
    assert dll.shift() == 1
    assert dll.head.data == 2
    assert dll.tail.data == 2
    assert dll.head.next_node is None
    assert dll.tail.prior_node is None
    assert dll.shift() == 2
    assert dll.head is None
    assert dll.tail is None


def test_dll_remove_index_error(dll):
    """Testing that the Index Error is raised if no val is passed."""
    dll.push(1)
    dll.push(2)
    dll.push(3)
    with pytest.raises(TypeError):
        dll.remove()


def test_dll_remove(dll):
    """Testing the dll remove function."""
    dll.push(1)
    dll.push(2)
    dll.push(3)
    dll.push(4)
    dll.remove(3)
    assert dll.head.prior_node.data == 2
    assert dll.head.prior_node.next_node.data == 4
    dll.remove(1)
    assert dll.tail.data == 2
    assert dll.tail.next_node.data == 4
    dll.remove(4)
    assert dll.head.data == 2
    assert dll.tail.data == 2


def test_dll_len(dll):
    """Test to make sure we get the right number of nodes."""
    assert len(dll) == 0
    dll.push(1)
    assert len(dll) == 1
    dll.push(2)
    assert len(dll) == 2
    dll.append(3)
    assert len(dll) == 3
    dll.push(4)
    assert len(dll) == 4
    dll.push(5)
    assert len(dll) == 5
    dll.push(6)
    dll.remove(4)
    assert len(dll) == 5
    dll.pop()
    assert len(dll) == 4
    dll.shift()
    assert len(dll) == 3
    dll.pop()
    assert len(dll) == 2
