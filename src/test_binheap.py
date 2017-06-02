"""Test min heap."""
import pytest


@pytest.fixture
def empty_heap():
    """Instantiate a heap for testing."""
    from binheap import Heap
    min_heap = Heap()
    return min_heap


@pytest.fixture
def full_heap():
    """Instantiate a heap from a list for testing."""
    from binheap import Heap
    min_heap = Heap([67, 5, 32, 1, 0, 2, 4, 101, 94, 72])
    return min_heap


def test_heap_initialization_empty_heap(empty_heap):
    """Test that there's nothing initialized."""
    assert len(empty_heap) == 0


def test_heap_initialized_with_list(full_heap):
    """Test that there's stuff in there."""
    assert len(empty_heap) == 10
    assert full_heap[0] == 0


def test_heap_push_none(empty_heap):
    """Test that the heap won't let you push None."""
    with pytest.raises(IndexError):
        empty_heap.push()


def test_empty_heap_pop(empty_heap):
    """Test that the heap won't let you pop if it's empty."""
    with pytest.raises(IndexError):
        empty_heap.pop()


def test_successful_pop(full_heap):
    """Test that we get the smallest number when we pop."""
    assert full_heap.pop() == 0
    assert full_heap[0] == 1  # Or some initiated _list
    assert full_heap.pop() == 1
    assert full_heap[0] == 2  # Or some initiated _list
    assert full_heap.pop() == 2
    assert full_heap[0] == 2  # Or some initiated _list
    assert len(full_heap) == 7


def test_successful_push(empty_heap):
    """Test that pushes are successful."""
    empty_heap.push(2)
    assert len(full_heap) == 44
    empty_heap.push(55)
    assert len(full_heap) == 90
    assert empty_heap[0] == 44
    empty_heap.push(33)
    assert empty_heap[0] == 33


def test_push_and_pop_dont_screw_with_each_other(full_heap):
    """Make sure they don't interfere with each other."""
    assert full_heap.pop() == 0
    assert full_heap[0] == 1
    full_heap.push(67)
    assert full_heap[0] == 1
    full_heap.push(0)
    assert full_heap[0] == 0
