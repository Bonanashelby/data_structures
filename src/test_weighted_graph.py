"""Test for our weighted graph."""
# {'A': {'B': 7, 'C': 9}, 'B': {'D': 2, 'E': 4}, 'C': {'F':6}}
"""Test our graph implementation."""
import pytest
from weighted_graph import Weighted


@pytest.fixture
def new_weighted_graph():
    """Graph for testing."""
    from weighted_graph import Weighted
    empty_graph = Weighted()
    return empty_graph


@pytest.fixture
def graph_no_edges():
    """Test graph with nodes only."""
    from weighted_graph import Weighted
    example_graph = Weighted()
    example_graph.add_node('BB')
    example_graph.add_node(82)
    example_graph.add_node(99)
    example_graph.add_node('AA')
    return example_graph


@pytest.fixture
def graph_with_edges():
    """Test graph with nodes only."""
    from weighted_graph import Weighted
    new_graph = Weighted()
    new_graph.add_node('A')
    new_graph.add_node('B')
    new_graph.add_node('C')
    new_graph.add_node('D')
    new_graph.add_node('E')
    new_graph.add_node('F')
    new_graph.add_edge('A', 'B', 7)
    new_graph.add_edge('A', 'C', 9)
    new_graph.add_edge('B', 'D', 2)
    new_graph.add_edge('B', 'E', 4)
    new_graph.add_edge('C', 'F', 6)
    return new_graph


def test_graph_init_no_values_taken():
    """Ensure we raise an error if we try to init with a value."""
    from weighted_graph import Weighted
    with pytest.raises(TypeError):
        a_graph = Weighted(2)


def test_graph_init_success(new_weighted_graph):
    """Ensure our new graph is in fact a graph."""
    assert isinstance(new_weighted_graph, Weighted)


def test_graph_adds_and_lists_nodes(graph_no_edges):
    """Ensure we get list of nodes."""
    listy = ['BB', 82, 99, 'AA']
    for node in listy:
        assert node in graph_no_edges.nodes()


def test_graph_adds_nodes_and_edges(graph_no_edges):
    """Ensure we add edges to the nodes."""
    graph_no_edges.add_edge('Louisiana Crawfish', 'WA Invasive Species', 3)
    assert graph_no_edges.edges() == [(
        'Louisiana Crawfish', 'WA Invasive Species', 3)]


def test_graph_lists_adds_and_lists_edges(graph_no_edges):
    """Ensure we add edges to the nodes."""
    graph_no_edges.add_edge(82, 34, 4)
    graph_no_edges.add_edge(99, 'AA', 6)
    assert (82, 34, 4) in graph_no_edges.edges()
    assert (99, 'AA', 6) in graph_no_edges.edges()


def test_graph_deletes_nodes(graph_with_edges):
    """Ensure we can delete a node."""
    graph_with_edges.del_nodes('B')
    listy = ['A', 'C', 'D', 'E', 'F']
    for node in listy:
        assert node in graph_with_edges.nodes()
    assert 'B' not in graph_with_edges.nodes()


def test_graph_cant_delete_an_unpresent_node(graph_no_edges):
    """Ensure we can't delete that doesn't exist."""
    with pytest.raises(ValueError):
        graph_no_edges.del_nodes(3.14)


def test_graph_cant_delete_without_argument(graph_no_edges):
    """Ensure we can't delete without an argument."""
    with pytest.raises(TypeError):
        graph_no_edges.del_nodes()


def test_del_some_edges(graph_with_edges):
    """Ensure we delete edges."""
    graph_with_edges.del_edges('A', 'B')
    assert graph_with_edges['A'] == {'C': 9}


def test_cant_delete_nonexistent_edge(graph_with_edges):
    """Ensure we can't delete a nonexistent edge."""
    with pytest.raises(KeyError):
        graph_with_edges.del_edges('BB', 'Badgers')


def test_nodes_exist(graph_no_edges):
    """Ensure we can assert nodes are in a graph."""
    for node in graph_no_edges:
        assert graph_no_edges.has_node(node)


def test_false_if_no_node(graph_no_edges):
    """Ensure we get false."""
    false_nodes = ['land submarine', 'Portland Timbers', 'tug cable scope', 100]
    for node in false_nodes:
        assert graph_no_edges.has_node(node) is False


def test_node_neighbors(graph_no_edges):
    """Ensure we get the right neighbors for a node."""
    graph_no_edges.add_edge('BB', 82, 5)
    assert graph_no_edges.neighbors('BB') == {82: 5}


def test_node_without_neighbors(graph_no_edges):
    """Ensure we get None back for neighbors."""
    assert graph_no_edges.neighbors(99) == {}


def test_node_error_if_nonpresent(graph_no_edges):
    """Can not get neighbors of nonpresent node."""
    with pytest.raises(ValueError):
        graph_no_edges.adjacent('Raccoon', 'Rocket')


def test_adjacent_nodes(graph_with_edges):
    """Ensure we get adjacent edges."""
    assert graph_with_edges.adjacent('A', 'B')


def test_adjacent_none(graph_with_edges):
    """Ensure we get false."""
    assert graph_with_edges.adjacent('B', 'A') is False


def test_adjacent_unpresent(graph_with_edges):
    """Ensure we get an error."""
    with pytest.raises(ValueError):
        graph_with_edges.adjacent('Captain Picard', 'Star Wars')


def test_add_node_value_error_val_exists(graph_no_edges):
    """Ensure a value is not added twice."""
    with pytest.raises(ValueError):
        graph_no_edges.add_node('BB')


def test_del_edges_has_no_edges_to_delete(graph_with_edges):
    """Ensure there are no edges to delete."""
    with pytest.raises(KeyError):
        graph_with_edges.del_edges('F', 'G')


def test_neighbors_value_error_not_in_graph(graph_with_edges):
        """Ensure the value error raises if no neighbors."""
        with pytest.raises(ValueError):
            graph_with_edges.neighbors('G')
