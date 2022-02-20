import sys
from graphMapping import *
from coloring import *


def main():
    delimiter = " "
    edges = get_edge_list(sys.argv[1], delimiter)
    graph = create_graph(edges)
    markov(graph)
    plt.show()


if __name__ == "__main__":
    main()
