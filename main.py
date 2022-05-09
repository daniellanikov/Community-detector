import sys

from networkx import number_connected_components
from graphMapping import *
from coloring import *
from small_world import *
from modularity import *
from runners import *
from application import *
import tkinter as tk

def main():
    delimiter = ";"
    edges = get_edge_list(sys.argv[3], delimiter)
    graph = create_graph(edges)
    application = Application()
    application.initialize_buttons()
    application.close_app()
    #compare(graph, delimiter, sys.argv[1])
    plt.show()


if __name__ == "__main__":
    main()
