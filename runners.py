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
    modularities = []
    for i in range(begin, end):
        node_list = girvan(graph, i)
        print("color number: ", i)
        modularities.append(modularity(graph, node_list))
    value = max(modularities)
    return modularities.index(value)


def measure(graph):
    markov_node_groups = markov(graph)
    print("markov nr.:", len(markov_node_groups))

    greedy_node_groups = greedy_modularity(graph)
    modularity(graph, greedy_node_groups)
    print("greedy nr.:", len(greedy_node_groups))

    print("finetune: ")
    ng_finetune_with_modularity(graph, 5, 25)


def communities(graph):
    largest_connected_component = graph.subgraph(max(nx.connected_components(graph), key=len))
    groups = greedy_modularity(largest_connected_component)
    print("number of groups: ", len(groups))
    value = ng_finetune_with_modularity(largest_connected_component, len(groups)-5, len(groups)+5)
    ng_groups = girvan(largest_connected_component, value)
    colormapper(largest_connected_component, ng_groups)


def cluster_and_condense(graph, class_size, edge_number):
    largest_connected_component = graph.subgraph(max(nx.connected_components(graph), key=len))
    node_groups = greedy_modularity(largest_connected_component)
    condensed_graph = condense(largest_connected_component, node_groups, class_size, edge_number)
    print("size of condensed graph: ", condensed_graph.number_of_nodes())
    nx.draw(condensed_graph, with_labels=True, node_color='blue', edge_color='silver', vmin=0, vmax=1,
            font_color="white")


def edges_between_clusters(graph, output_filename):
    largest_connected_component = graph.subgraph(max(nx.connected_components(graph), key=len))
    groups = greedy_modularity(largest_connected_component)
    edgenumber(nodegroups2cluster(groups), largest_connected_component, output_filename)

