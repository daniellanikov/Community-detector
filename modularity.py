import networkx as nx
import networkx.algorithms.community as nx_comm
from graphMapping import *


def modularity(graph, node_groups):
    # Built in networkx modularity
    value = nx_comm.modularity(graph, node_groups)
    print("networkx modularity: ", value)

    # Calculated modularity
    """
    array = np.array(nx.adjacency_matrix(graph).todense())
    m = graph.number_of_edges()
    result = 0
    nodes = list(graph.nodes)
    for i in range(graph.number_of_nodes()):
        for j in range(graph.number_of_nodes()):
            temp = array[i][j] - ( graph.degree[nodes[i]] * graph.degree[nodes[j]] / (2*m) )
            result += temp
    normalize = result / 4 * m
    print("calculated modularity: ", normalize)
    """


def condense(graph=nx.Graph(), node_groups=list):
    """
    edges = graph.edges
    digraph = nx.DiGraph()
    digraph.add_edges_from(edges)
    scc = list(nx.strongly_connected_components(digraph))
    condensed_graph = nx.condensation(digraph, scc)
    nx.draw(condensed_graph, with_labels=False, node_size=50, node_color='blue', edge_color='silver', vmin=0, vmax=1)
    """
    condensed_graph = nx.Graph()
    for index in range(len(node_groups)):
        for index2 in range(len(node_groups)):
            if index != index2:
                for value in node_groups[index]:
                    for value2 in node_groups[index2]:
                        edge = (value, value2)
                        if edge in graph.edges:
                            if (index, index2) not in condensed_graph.edges:
                                condensed_graph.add_edge(index, index2)
    nx.draw(condensed_graph, with_labels=True, node_color='blue', edge_color='silver', vmin=0, vmax=1, font_color="white")

