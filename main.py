import sys
from graphMapping import *
from coloring import *
from modularity import modularity


def main():
    delimiter = " "
    edges = get_edge_list(sys.argv[1], delimiter)
    graph = create_graph(edges)
    print("number of nodes: ", nx.number_of_nodes(graph))
    node_groups = newman(graph)
    modularity(graph, node_groups)
    plt.show()


if __name__ == "__main__":
    main()
