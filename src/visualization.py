# visualization.py

import networkx as nx
import matplotlib.pyplot as plt

def plot_decision_tree(decision_node):
    """
    Plots the decision tree.
    """
    G = nx.DiGraph()

    def add_nodes(node, parent=None):
        G.add_node(node.name)
        if parent:
            G.add_edge(parent.name, node.name)
        for branch in getattr(node, 'branches', []):
            add_nodes(branch, node)
        for next_node in getattr(node, 'next_nodes', []):
            add_nodes(next_node, node)

    add_nodes(decision_node)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, arrows=True)
    plt.show()
