import networkx as nx
import matplotlib.pyplot as plt
from graphMapping import find_highest_degree


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
    #complement = nx.complement(graph)
    colored = nx.greedy_color(graph, strategy="connected_sequential_dfs")
    colormap = [colored.get(node) for node in graph.nodes]
    nx.draw(graph, with_labels=False, node_color=colormap, cmap=plt.get_cmap("plasma"), vmin=0, vmax=max(colormap),
            font_color="white")
    print(len(colored))
    print(graph.number_of_nodes())
