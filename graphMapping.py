import networkx as nx


class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2


def get_edge_list(filepath, delimiter):
    file = open(filepath, "r")
    content = file.read().split("\n")
    edges = []
    for item in content:
        if item != "":
            row = item.split(delimiter)
            edges.append(Edge(row[0], row[1]))
    return edges


def find_highest_degree(graph=nx.Graph(), amount=1):
    sorted_nodes = sorted(graph.degree, key=lambda item: item[1], reverse=True)
    colormap = {}
    for i in range(0, amount):
        colormap[sorted_nodes[i][0]] = 0.38
    return colormap


def create_graph(edges):
    graph = nx.Graph()
    for edge in edges:
        graph.add_edge(edge.node1, edge.node2)
    return graph
