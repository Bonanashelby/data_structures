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
    assert dll.tail == None
    assert dll.head == None


