"""Data reading and printing utils."""
import numpy as np
import pandas as pd
import networkx as nx
from texttable import Texttable

def tab_printer(args):
    """
    Function to print the logs in a nice tabular format.
    :param args: Parameters used for the model.
    """
    args = vars(args)
    keys = sorted(args.keys())
    t = Texttable()
    t.add_rows([["Parameter", "Value"]])
    t.add_rows([[k.replace("_", " ").capitalize(), args[k]] for k in keys])
    print(t.draw())

def graph_reader(path):
    """
    Function to read the graph from the path.
    :param path: Path to the edge list.
    :return graph: NetworkX object returned.
    """

    # Read the edge list from the CSV file
    edges = np.genfromtxt(path, delimiter=',', skip_header=1, dtype=int)

    # Create a dictionary to map the original node IDs to continuous IDs
    node_map = {}
    continuous_id = 0
    for node_id in np.unique(edges.flatten()):
        if node_id not in node_map:
            node_map[node_id] = continuous_id
            continuous_id += 1

    # Map the original node IDs to continuous IDs in the edge list
    mapped_edges = np.array([(node_map[edge[0]], node_map[edge[1]]) for edge in edges])

    graph = nx.from_edgelist(mapped_edges)
    graph.remove_edges_from(nx.selfloop_edges(graph))
    return graph
