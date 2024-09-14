# decision_tree.py

import numpy as np

class DecisionNode:
    """
    Represents a decision node in the tree.
    """
    def __init__(self, name):
        self.name = name
        self.branches = []

    def add_branch(self, chance_node):
        self.branches.append(chance_node)

class ChanceNode:
    """
    Represents a chance node in the tree.
    """
    def __init__(self, name, probability, cost, utility):
        self.name = name
        self.probability = probability
        self.cost = cost
        self.utility = utility
        self.next_nodes = []

    def add_next_node(self, node):
        self.next_nodes.append(node)

    def expected_values(self):
        """
        Recursively calculates expected cost and utility.
        """
        if not self.next_nodes:
            return self.cost, self.utility
        else:
            total_cost = self.cost
            total_utility = self.utility
            for node in self.next_nodes:
                c, u = node.expected_values()
                total_cost += node.probability * c
                total_utility += node.probability * u
            return total_cost, total_utility
