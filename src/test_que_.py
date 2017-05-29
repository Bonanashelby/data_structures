"""Our test file for our queue."""
import pytest


@pytest.fixture
def the_queue():
    """Queue fixture."""
    from que_ import Queue
    the_queue = Queue()
    return the_queue


def test_the_queue_enqueue(the_queue):
    """Test for enqueuing to the queue."""
    the_queue.enqueue(2)
    assert the_queue._new_dll.head.data == 2
    assert the_queue._new_dll.tail.data == 2


def test_the_queue_enqueue_multi_values(the_queue):
    """Test for enqueuing multiple values to the queue."""
    the_queue.enqueue(2)
    the_queue.enqueue(3)
    the_queue.enqueue(4)
    the_queue.enqueue(5)
    assert the_queue._new_dll.head.data == 5
    assert the_queue._new_dll.tail.data == 2
    assert the_queue._new_dll.head.prior_node.data == 4
    assert the_queue._new_dll.tail.next_node.data == 3


def test_the_queue_dequeue(the_queue):
    """Test for dequeuing to the queue."""
    the_queue.enqueue(2)
    assert the_queue.dequeue() == 2


def test_the_queue_dequeue_raises_exception(the_queue):
    """Test that if queue is empty the error is raised."""
    with pytest.raises(IndexError):
        the_queue.dequeue()


def test_the_queue_dequeue_multi_values(the_queue):
    """Test for dequeue on mulitple values."""
    the_queue.enqueue(2)
    assert the_queue._new_dll.tail.data == 2
    the_queue.enqueue(3)
    assert the_queue._new_dll.tail.next_node.data == 3
    the_queue.enqueue(4)
    the_queue.enqueue(5)
    assert the_queue._new_dll.head.data == 5
    the_queue.dequeue()
    assert the_queue._new_dll.tail.data == 3
    assert the_queue.dequeue() == 3
    assert the_queue._new_dll.tail.data == 4


def test_the_peek(the_queue):
    """Test the peek function."""
    the_queue.enqueue(1)
    the_queue.enqueue(2)
    the_queue.enqueue(3)
    assert the_queue._new_dll.tail.data == 1
    the_queue.dequeue()
    assert the_queue._new_dll.tail.data == 2


def test_the_queue_len(the_queue):
    """Test the length on the queue."""
    the_queue.enqueue(1)
    the_queue.enqueue(2)
    the_queue.enqueue(3)
    assert len(the_queue) == 3











