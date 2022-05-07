from graphMapping import *
from coloring import *


def coloring_newman(filepath):
    delimiter = ";"
    edges = get_edge_list(filepath, delimiter)
    graph = create_graph(edges)
    node_groups = newman(graph)
    colormapper(graph, node_groups)
    plt.show()

