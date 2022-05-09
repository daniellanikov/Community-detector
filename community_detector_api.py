from graphMapping import *
from coloring import *
from modularity import *
from runners import *


def parse_txt(filepath, delimiter):
    if delimiter == "semicolon":
        edges = get_edge_list(filepath, ";")
    elif delimiter == "space":
        edges = get_edge_list(filepath, " ")
    graph = create_graph(edges)
    return graph


def coloring_newman(filepath, delimiter):
    graph = parse_txt(filepath, delimiter)
    node_groups = newman(graph)
    colormapper(graph, node_groups)
    plt.show()


def coloring_markov(filepath, delimiter):
    graph = parse_txt(filepath, delimiter)
    markov(graph, true, true)
    plt.show()


def coloring_cliques(filepath, delimiter):
    graph = parse_txt(filepath, delimiter)
    clique(graph, 10)
    plt.show()


def coloring_greedy_modularity(filepath, delimiter):
    graph = parse_txt(filepath, delimiter)
    groups = greedy_modularity(graph)
    colormapper(graph, groups)
    plt.show()


def coloring_h_avoiding_clusters(filepath, delimiter):
    graph = parse_txt(filepath, delimiter)
    h_avoiding_coloring(graph)
    plt.show()


def utils_modularity(filepath, delimiter):
    graph = parse_txt(filepath, delimiter)
    modularity(graph)


def utils_condense(filepath, delimiter):
    graph = parse_txt(filepath, delimiter)
    detect_and_condense(graph, 1, 1)
    plt.show()

