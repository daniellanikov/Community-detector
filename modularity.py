import networkx as nx
import numpy as np
from networkx.algorithms import community


def modularity(graph):
    # Built in networkx modularity
    value = community.girvan_newman(graph)
    mod = next(value)
    print("networkx modularity: ", sorted(map(sorted, mod)))

    # Calculated modularity
    array = np.array(nx.adjacency_matrix(graph).todense())
    m = graph.number_of_edges()
    result = 0
    nodes = list(graph.nodes)
    for i in range(graph.number_of_nodes()):
        for j in range(graph.number_of_nodes()):
            temp = array[i][j] - ( graph.degree[nodes[i]] * graph.degree[nodes[j]] / (2*m) )
            result += temp
    normalize = result / 4 * m
    return normalize
