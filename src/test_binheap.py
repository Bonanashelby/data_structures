"""Test min heap."""
import pytest


@pytest.fixture
def heap():
    """Instantiate a heap for testing."""
    from binheap import Heap
    min_heap = Heap()
    return min_heap


def test_heap_initialization(heap):
    """Test that there's nothing initialized."""
    assert heap.parent is None
    assert heap.left_child is None
    assert heap.right_child is None
