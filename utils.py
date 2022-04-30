from matplotlib import pyplot as plt
import random
import networkx as nx


def colormap(graph=nx.Graph(), cliques=list):
    posi_gn = nx.spring_layout(graph)
    cmap = plt.get_cmap("plasma")
    colors = random.sample(range(0, len(cliques)), len(cliques))
    for i in range(len(colors)):
        colors[i] = colors[i] / len(cliques)

    for nodes, c in zip(cliques, colors):
        color = [cmap(c)]*len(nodes)
        nx.draw_networkx_nodes(graph, posi_gn, nodelist=nodes, node_color=color, node_size=50)
    nx.draw_networkx_edges(graph, posi_gn, edge_color="silver")

