# analysis.py

def calculate_icer(cost_a, utility_a, cost_b, utility_b):
    """
    Calculates the Incremental Cost-Effectiveness Ratio.
    """
    delta_cost = cost_b - cost_a
    delta_utility = utility_b - utility_a
    if delta_utility == 0:
        return np.inf
    return delta_cost / delta_utility
