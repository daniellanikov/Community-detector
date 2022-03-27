import sys

from networkx import number_connected_components
from graphMapping import *
from coloring import *
from small_world import *
from modularity import *


def main():
    delimiter = " "
    edges = get_edge_list(sys.argv[1], delimiter)
    graph = create_graph(edges)
    h_avoiding_coloring(graph)
    plt.show()


if __name__ == "__main__":
    main()
