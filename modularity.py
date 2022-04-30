import networkx as nx
import networkx.algorithms.community as nx_comm
from graphMapping import *
import numpy as np


def modularity(graph, node_groups):
    # Built in networkx modularity
    value = nx_comm.modularity(graph, node_groups)
    print("networkx modularity: ", value)
    return value


def calculated_modularity(graph):
    array = np.array(nx.adjacency_matrix(graph).todense())
    m = graph.number_of_edges()
    result = 0
    nodes = list(graph.nodes)
    for i in range(graph.number_of_nodes()):
        for j in range(graph.number_of_nodes()):
            temp = array[i][j] - ( graph.degree[nodes[i]] * graph.degree[nodes[j]] / (2*m) )
            result += temp
    normalize = result / 4 * m
    print("calculated modularity: ", normalize)


def condense_built_in(graph):
    edges = graph.edges
    digraph = nx.DiGraph()
    digraph.add_edges_from(edges)
    scc = list(nx.strongly_connected_components(digraph))
    condensed_graph = nx.condensation(digraph, scc)
    nx.draw(condensed_graph, with_labels=False, node_size=50, node_color='blue', edge_color='silver', vmin=0, vmax=1)


def condense(graph=nx.Graph(), node_groups=list, class_size=int, edge_number=int):
    condensed_graph = nx.Graph()
    for index in range(len(node_groups)):
        for index2 in range(len(node_groups)):
            if len(node_groups[index]) > class_size and len(node_groups[index2]) > class_size:
                edgelist = get_edges(node_groups[index], node_groups[index2], graph)
                length = len(edgelist)
                if index != index2 and length > edge_number:
                    for value in node_groups[index]:
                        for value2 in node_groups[index2]:
                            edge = (value, value2)
                            if edge in graph.edges:
                                if (index, index2) not in condensed_graph.edges:
                                    condensed_graph.add_edge(index, index2)
    return condensed_graph


def nodegroups2cluster(node_groups=list):
    clusters = []
    for index in range(len(node_groups)):
        clusters.append(Cluster(index, node_groups[index]))
    return clusters


def get_edges(group1=list, group2=list, graph=nx.Graph()):
    edge_list = []
    for value in group1:
        for value2 in group2:
            edge = (value, value2)
            if edge in graph.edges:
                if edge not in edge_list:
                    edge_list.append(edge)
    return edge_list


def edgenumber(clusters=list, graph=nx.Graph(), output_filename=str):
    f = open("./outputs/"+output_filename, "a")
    for cluster1 in clusters:
        for cluster2 in clusters:
            if cluster1.uuid != cluster2.uuid:
                edgelist = get_edges(cluster1.nodes, cluster2.nodes, graph)
                text = "numbers of edges " + str(len(edgelist)) + " between cluster[" + str(cluster1.uuid) + "] and cluster[" + str(cluster2.uuid) + "]\n"
                f.write(text)
                print(text)
    f.close()
