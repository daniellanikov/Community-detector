import sys
from graphMapping import *
from modularity import *


def main():
    edges = get_edge_list(sys.argv[1], " ")
    graph = create_graph(edges)
    print("modularity: ", modularity(graph))
    complement_coloring(graph)


if __name__ == "__main__":
    main()
