import networkx as nx
from networkx import number_connected_components
from graphMapping import *
from coloring import *
from small_world import *
from modularity import *


def sixtep_modularity(graph, delimiter, cluster_path):
    print("nodes: ", graph.number_of_nodes())
    print("edges: ", graph.number_of_edges())
    clusters = get_cluster_list(cluster_path, delimiter)
    node_list = []
    for cluster in clusters:
        node_list.append(cluster.nodes)
    print("used colors: ", len(node_list))
    modularity(graph, node_list)


def ng_finetune_with_modularity(graph, begin, end):
    for i in range(begin, end):
        node_list = girvan(graph, i)
        print("color number: ", i)
        modularity(graph, node_list)


def measure(graph):
    markov_node_groups = markov(graph)
    print("markov nr.:", len(markov_node_groups))

    greedy_node_groups = greedy_modularity(graph)
    modularity(graph, greedy_node_groups)
    print("greedy nr.:", len(greedy_node_groups))

    print("finetune: ")
    ng_finetune_with_modularity(graph, 5, 25)


