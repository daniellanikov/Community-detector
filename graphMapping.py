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


class Cluster:
    def __init__(self, uuid, node):
        self.uuid = uuid
        self.nodes = [node]

    def add_node(self, node):
        self.nodes.append(node)


def get_cluster_list(filepath, delimiter):
    file = open(filepath, "r")
    content = file.read().split("\n")
    uuids = []
    clusters = []
    for item in content:
        if item != "":
            row = item.split(delimiter)
            if row[1] not in uuids:
                uuids.append(row[1])
                clusters.append(Cluster(row[1], row[0]))
            else:
                for cluster in clusters:
                    if row[1] == cluster.uuid:
                        cluster.add_node(row[0])
    return clusters
