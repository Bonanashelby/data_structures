"""Test our graph implementation."""
import pytest
<<<<<<< HEAD
=======
from graph_1 import Graph
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


@pytest.fixture
def new_graph():
    """Graph for testing."""
<<<<<<< HEAD
    from graph import Graph
=======
    from graph_1 import Graph
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8
    empty_graph = Graph()
    return empty_graph


@pytest.fixture
def graph_no_edges():
    """Test graph with nodes only."""
<<<<<<< HEAD
    from graph import Graph
    example_graph = Graph()
    example_graph.add_node('Grapefruit')
    example_graph.add_node(82)
    example_graph.add_node(['Bicycle', 1, 'Stolen'])
    trash_panda = {'likes': 'garbage', 'characteristics': ['thieving', 'conniving', 'rabies', 'sometimes cute'], 'looks-like': 'furry burglar'}
    example_graph.add_node(trash_panda)
    example_graph.add_node(99)
    example_graph.add_node('Luftballons')
=======
    from graph_1 import Graph
    example_graph = Graph()
    example_graph.add_node('Grapefruit')
    example_graph.add_node(82)
    example_graph.add_node(99)
    example_graph.add_node('Luftballons')
    return example_graph
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


@pytest.fixture
def graph_with_edges():
    """Test graph with nodes only."""
<<<<<<< HEAD
    from graph import Graph
    example_graph = Graph()
    example_graph.add_node('Grapefruit')
    example_graph.add_node(82)
    best_use_case_for_cable_lock = ['Bicycle', 1, 'Stolen']
    example_graph.add_node(best_use_case_for_cable_lock)
    trash_panda = {'likes': 'garbage', 'characteristics': ['thieving', 'conniving', 'rabies', 'sometimes cute'], 'looks-like': 'furry burglar'}
    example_graph.add_node(trash_panda)
    example_graph.add_node(99)
    example_graph.add_node('Luftballons')
    example_graph.add_edge(99, 'Luftballons')
    example_graph.add_edge('Grapefruit', trash_panda)
    example_graph.add_edge(82, best_use_case_for_cable_lock)

=======
    from graph_1 import Graph
    example_graph = Graph()
    example_graph.add_node('Grapefruit')
    example_graph.add_node(82)
    example_graph.add_node(99)
    example_graph.add_node('Luftballons')
    example_graph.add_edge(99, 'Luftballons')
    example_graph.add_edge('Grapefruit', 'Luftballons')
    example_graph.add_edge('Grapefruit', 82)
    return example_graph
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_graph_init_no_values_taken():
    """Ensure we raise an error if we try to init with a value."""
<<<<<<< HEAD
    from graph import Graph
=======
    from graph_1 import Graph
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8
    with pytest.raises(TypeError):
        a_graph = Graph(2)


def test_graph_init_success(new_graph):
    """Ensure our new graph is in fact a graph."""
    assert isinstance(new_graph, Graph)


def test_graph_adds_and_lists_nodes(graph_no_edges):
    """Ensure we get list of nodes."""
<<<<<<< HEAD
    assert graph_no_edges.nodes() == ['Grapefruit', 82, best_use_case_for_cable_lock, trash_panda, 99, 'Luftballons']


def test_wont_add_edges_to_empty_graph(empty_graph):
    """Ensure we can't just add an edge without nodes."""
    with pytest.raises(ValueError):
        empty_graph.add_edge()
=======
    listy = ['Grapefruit', 82, 99, 'Luftballons']
    for node in listy:
        assert node in graph_no_edges.nodes()


def test_wont_add_edges_to_empty_graph(new_graph):
    """Ensure we can't just add an edge without nodes."""
    with pytest.raises(TypeError):
        new_graph.add_edge()
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_graph_adds_nodes_and_edges(graph_no_edges):
    """Ensure we add edges to the nodes."""
    graph_no_edges.add_edge('Louisiana Crawfish', 'WA Invasive Species')
    assert graph_no_edges.edges() == [(
        'Louisiana Crawfish', 'WA Invasive Species')]


def test_graph_lists_adds_and_lists_edges(graph_no_edges):
    """Ensure we add edges to the nodes."""
<<<<<<< HEAD
    graph_no_edges.add_edge(82, trash_panda)
    graph_no_edges.add_edge(99, 'Luftballons')
    assert graph_no_edges.edges() == [(82, trash_panda), (99, 'Luftballons')]
=======
    graph_no_edges.add_edge(82, 34)
    graph_no_edges.add_edge(99, 'Luftballons')
    assert (82, 34) in graph_no_edges.edges()
    assert (99, 'Luftballons') in graph_no_edges.edges()
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_graph_deletes_nodes(graph_with_edges):
    """Ensure we can delete a node."""
<<<<<<< HEAD
    graph_with_edges.del_node('Grapefruit')
    assert graph_with_edges.nodes() == [
        82,
        best_use_case_for_cable_lock,
        trash_panda,
        99,
        'Luftballons']
=======
    graph_with_edges.del_nodes('Grapefruit')
    listy = [82, 99, 'Luftballons']
    for node in listy:
        assert node in graph_with_edges.nodes()
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_graph_cant_delete_an_unpresent_node(graph_no_edges):
    """Ensure we can't delete that doesn't exist."""
    with pytest.raises(ValueError):
<<<<<<< HEAD
        graph_no_edges.del_node(3.14)
=======
        graph_no_edges.del_nodes(3.14)
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_graph_cant_delete_without_argument(graph_no_edges):
    """Ensure we can't delete without an argument."""
<<<<<<< HEAD
    with pytest.raises(ValueError):
        graph_no_edges.del_node()
=======
    with pytest.raises(TypeError):
        graph_no_edges.del_nodes()
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_del_some_edges(graph_with_edges):
    """Ensure we delete edges."""
<<<<<<< HEAD
    graph_with_edges.del_edge('Grapefruit', trash_panda)
    graph_with_edges.edges([(99, 'Luftballons'), (82, best_use_case_for_cable_lock)])
=======
    graph_with_edges.del_edges('Grapefruit', 'Luftballons')
    assert graph_with_edges._graph['Grapefruit'] == [82]
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_cant_delete_nonexistent_edge(graph_with_edges):
    """Ensure we can't delete a nonexistent edge."""
<<<<<<< HEAD
    with pytest.raises(AttributeError):
        graph_with_edges.del_edge('Grapefruit', 'Luftballons')
=======
    with pytest.raises(ValueError):
        graph_with_edges.del_edges('Grapefruit', 'Badgers')
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_nodes_exist(graph_no_edges):
    """Ensure we can assert nodes are in a graph."""
<<<<<<< HEAD
    for node in graph_no_edges:
=======
    for node in graph_no_edges._graph:
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8
        assert graph_no_edges.has_node(node)


def test_false_if_no_node(graph_no_edges):
    """Ensure we get false."""
    false_nodes = ['land submarine', 'Portland Timbers', 'tug cable scope', 100]
    for node in false_nodes:
<<<<<<< HEAD
        assert node in graph_no_edges is False
=======
        assert graph_no_edges.has_node(node) is False
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_node_neighbors(graph_no_edges):
    """Ensure we get the right neighbors for a node."""
<<<<<<< HEAD
    graph_no_edges.add_node(trash_panda, 'Grapefruit')
    graph_no_edges.add_node(trash_panda, best_use_case_for_cable_lock)
    graph_no_edges.add_node(trash_panda, 82)
    assert graph_no_edges.neighbors(trash_panda) == ['Grapefruit', best_use_case_for_cable_lock, 82]
=======
    graph_no_edges.add_edge('Grapefruit', 82)
    assert graph_no_edges.neighbors('Grapefruit') == [82]
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_node_without_neighbors(graph_no_edges):
    """Ensure we get None back for neighbors."""
<<<<<<< HEAD
    assert graph_no_edges(trash_panda) is None
=======
    assert graph_no_edges.neighbors(99) == []
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_node_error_if_nonpresent(graph_no_edges):
    """Can not get neighbors of nonpresent node."""
    with pytest.raises(ValueError):
<<<<<<< HEAD
        graph_no_edges('Raccoon')
=======
        graph_no_edges.adjacent('Raccoon', 'Rocket')
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_adjacent_nodes(graph_with_edges):
    """Ensure we get adjacent edges."""
<<<<<<< HEAD
    assert graph_with_edges('Grapefruit', trash_panda)
    assert graph_with_edges(99, 'Luftballons')
=======
    assert graph_with_edges.adjacent(99, 'Luftballons')
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_adjacent_none(graph_with_edges):
    """Ensure we get false."""
<<<<<<< HEAD
    assert graph_with_edges(82, 'Grapefruit') is False
=======
    assert graph_with_edges.adjacent(82, 'Grapefruit') is False
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8


def test_adjacent_unpresent(graph_with_edges):
    """Ensure we get an error."""
    with pytest.raises(ValueError):
<<<<<<< HEAD
        graph_with_edges('Captain Picard', 'Star Wars')
=======
        graph_with_edges.adjacent('Captain Picard', 'Star Wars')
>>>>>>> 3c6be99cd369560df35f117c22a4f587acf604b8
