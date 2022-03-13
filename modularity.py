import networkx.algorithms.community as nx_comm


def modularity(graph, node_groups):
    # Built in networkx modularity
    value = nx_comm.modularity(graph, node_groups)
    print("networkx modularity: ", value)

    # Calculated modularity
    """
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
    """
