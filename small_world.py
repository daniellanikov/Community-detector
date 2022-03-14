import networkx as nx
from networkx import lattice_reference, sigma, is_connected
from utils import *


def lattice(graph=nx.Graph()):
    result_graph = lattice_reference(graph)
    nx.draw(result_graph, with_labels=False, node_size=50, node_color='blue', edge_color='silver', vmin=0, vmax=1)


def is_small_world_sigma(graph=nx.Graph()):
    largest_connected_component = graph.subgraph(max(nx.connected_components(graph), key=len))
    value = sigma(largest_connected_component)
    print("sigma value of the graph", value)
    if value > 1:
        print("This is a small-world graph")

