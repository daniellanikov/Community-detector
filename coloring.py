import itertools
import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import find_cliques
from networkx.algorithms.community import girvan_newman
import markov_clustering as mc
from graphMapping import find_highest_degree
from Utils import colormap


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
    colormap(graph, comms)


def newman(graph=nx.Graph()):
    result = girvan_newman(graph)
    limited = itertools.takewhile(lambda c: len(c) <= 100, result)

    node_groups = []
    for communities in next(result):
        node_groups.append(list(communities))
    print(len(node_groups))

    colors = random.sample(range(0, 100), len(node_groups))
    for i in range(len(colors)):
        colors[i] = colors[i] / 100

    color_map = []
    for i in range(len(node_groups)):
        for node in graph:
            if node in node_groups[i]:
                color_map.append(colors[i])
    print(color_map)
    nx.draw(graph, with_labels=False, node_size=50, node_color=color_map, cmap=plt.get_cmap("plasma"), vmin=0, vmax=1,
            font_color="white")


def markov(graph=nx.Graph()):
    matrix = nx.to_scipy_sparse_matrix(graph)
    result = mc.run_mcl(matrix)
    clusters = mc.get_clusters(result)
    print(clusters)
    mc.draw_graph(matrix, clusters, node_size=50, with_labels=False, edge_color="silver")


def community(graph=nx.Graph(), clique_size=int):
    result = list(find_cliques(graph))
    cliques = []
    for index in range(len(result) - 1):
        element = result[index]
        nextelement = result[index+1]
        if element[0] != nextelement[0] and len(element) > clique_size:
            cliques.append(element)
    colormap(graph, cliques)

