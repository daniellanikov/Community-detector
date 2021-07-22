import sys
import matplotlib.pyplot as plt

from graphMapping import *
from modularity import *
from coloring import *


def main():
    delimiter = ";"
    edges = get_edge_list(sys.argv[1], delimiter)
    graph = create_graph(edges)
    source_coloring(graph)
    plt.show()


if __name__ == "__main__":
    main()
