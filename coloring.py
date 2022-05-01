import itertools
import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx import adjacency_matrix
from networkx.algorithms import find_cliques, bipartite
from networkx.algorithms.community import girvan_newman, greedy_modularity_communities
import markov_clustering as mc
from graphMapping import find_highest_degree, Cluster
from utils import colormapper
from sympy import *


def source_coloring(graph=nx.Graph()):
    source = find_highest_degree(graph, 10)
    colormap = [source.get(node, 0.78) for node in graph.nodes]
    nx.draw(graph, with_labels=False, node_color=colormap, cmap=plt.get_cmap("plasma"), vmin=0, vmax=1,
            font_color="white")


"""
Greedy coloring strategies:

largest_first
random_sequential
smallest_last
connected_sequential_bfs
connected_sequential_dfs
"""


def greedy_coloring(graph=nx.Graph()):
    colored = nx.greedy_color(graph, strategy="connected_sequential_dfs")
    colormap = [colored.get(node) for node in graph.nodes]
    nx.draw(graph, with_labels=False, node_color=colormap, node_size=50, cmap=plt.get_cmap("plasma"), vmin=0, vmax=max(colormap),
            font_color="white")


def complement_greedy_coloring(graph=nx.Graph()):
    complement = nx.complement(graph)
    colored = nx.greedy_color(complement, strategy="connected_sequential_dfs")
    colormap = [colored.get(node) for node in graph.nodes]
    nx.draw(complement, with_labels=False, node_size=50, node_color=colormap, cmap=plt.get_cmap("plasma"), vmin=0, vmax=max(colormap),
            font_color="white")


def binary_coloring(graph=nx.Graph()):
    sorted_nodes = sorted(graph.degree, key=lambda item: item[1], reverse=False)
    print(sorted_nodes)
    colormap = {}
    count = 0
    for i in sorted_nodes:
        if i[1] == 1 and list(graph.neighbors(i[0]))[0] not in colormap:
            colormap[i[0]] = 0.78
            count += 1
    """colormap = {}
    for i in range(0, 500):
        colormap[sorted_nodes[i][0]] = 0.38
    """
    print(count)
    colormap2 = [colormap.get(node, 0.38) for node in graph.nodes]
    print(colormap2)
    nx.draw(graph, with_labels=False, node_size=50, node_color=colormap2, cmap=plt.get_cmap("plasma"), vmin=0, vmax=1,
            font_color="white")


def girvan(graph=nx.Graph(), comm_count=int):
    comp = nx.community.girvan_newman(graph)
    for _ in range(comm_count - 1):
        comms = next(comp)
    return comms


def newman(graph=nx.Graph()):
    result = girvan_newman(graph)
    limited = itertools.takewhile(lambda c: len(c) <= 2000, result)
    node_groups = []
    for communities in next(limited):
        node_groups.append(list(communities))
    colormapper(graph, node_groups)
    return node_groups


def markov(graph=nx.Graph()):
    matrix = nx.to_scipy_sparse_matrix(graph)
    result = mc.run_mcl(matrix)
    clusters = mc.get_clusters(result)
    node_groups = []
    for cluster in clusters:
        node_groups.append(cluster)
    #print("mc modularity: ", mc.modularity(matrix, clusters))
    #mc.draw_graph(matrix, clusters, node_size=50, with_labels=False, edge_color="silver")
    return node_groups


def clique(graph=nx.Graph(), clique_size=int):
    result = list(find_cliques(graph))
    cliques = []
    for index in range(len(result) - 1):
        element = result[index]
        nextelement = result[index+1]
        if element[0] != nextelement[0] and len(element) > clique_size:
            cliques.append(element)
    colormapper(graph, cliques)


def greedy_modularity(graph=nx.Graph()):
    result = list(greedy_modularity_communities(graph))
    #colormap(graph, result)
    return result


def adjacency(graph=nx.Graph()):
    A = adjacency_matrix(graph)
    m = Matrix(A.todense())
    A_rref = m.rref()
    print("The Row echelon form of matrix M and the pivot columns : {}".format(A_rref))


def y_sorter(graph=nx.Graph()):
    X, Y = bipartite.sets(graph)
    nodes = {}
    degrees = []
    for item in Y:
        if graph.degree[item] not in nodes.values():
            degrees.append(graph.degree[item])
        nodes[item] = graph.degree[item]
    ordered = dict(sorted(nodes.items(), key=lambda item: item[1]))
    ordered_list = list(ordered)
    return ordered_list


def degree_coloring(graph=nx.Graph()):
    X, Y = bipartite.sets(graph)
    nodes = {}
    degrees = []
    for item in Y:
        if graph.degree[item] not in nodes.values():
            degrees.append(graph.degree[item])
        nodes[item] = graph.degree[item]
    return degrees


def h_avoiding_coloring(graph=nx.Graph(), h=nx.Graph()):
    X, Y = bipartite.sets(graph)
    degrees = degree_coloring(graph)
    colordict = {}
    uuids = []
    clusters = []
    for node in graph.nodes:
        if node in Y:
            for degree in degrees:
                if graph.degree(node) == degree:
                    colordict[node] = degree / 10 * 1.5
                    if degree not in uuids:
                        uuids.append(degree)
                        clusters.append(Cluster(degree, node))
                    else:
                        for cluster in clusters:
                            if degree == cluster.uuid:
                                cluster.add_node(node)
        else:
            colordict[node] = 0.82
            if 10 not in uuids:
                uuids.append(10)
                clusters.append(Cluster(10, node))
            else:
                for cluster in clusters:
                    if 10 == cluster.uuid:
                        cluster.add_node(node)

    for cluster in clusters:
        if cluster.uuid == 10:
            cluster_1 = cluster.get_nodes(10)

    #2k2 detection
    k2s = []
    for node in cluster_1:
        for cluster in clusters:
            for item in cluster.nodes:
                for edge in graph.edges(node):
                    if edge[1] == item:
                        k2s.append(edge)
    for k2 in k2s:
        first = k2s[0]
        if first[0] != k2[0] and first[1] != k2[1]:
            colordict[k2[1]] = random.randint(1, 100) / 100

    #initialize graph position
    pos = dict()
    pos.update((n, (1, i)) for i, n in enumerate(cluster_1))
    pos.update((n, (2, i)) for i, n in enumerate(y_sorter(graph)))

    #get colormap
    colors = []
    for node in graph.nodes:
        colors.append(colordict.get(node))
    print(colordict)
    nx.draw(graph, pos=pos, with_labels=True, node_color=colors, cmap=plt.get_cmap("plasma"), edge_color='silver', vmin=0, vmax=1, font_color="white")
