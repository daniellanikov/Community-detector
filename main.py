import sys
from graphMapping import *
from modularity import *


def main():
    delimiter = " "
    edges = get_edge_list(sys.argv[1], delimiter)
    graph = create_graph(edges)
    print("calculated modularity: ", modularity(graph))
    complement_coloring(graph)


if __name__ == "__main__":
    main()
