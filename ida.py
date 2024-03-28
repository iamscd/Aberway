import math

from data import GRAPH_DATA

EDGES = {int(node): {int(neighbor): float(cost) for neighbor, cost in neighbors} for node, neighbors in GRAPH_DATA.items()}

def search(node_id, path, cost_so_far, target_nodes, total_length, error):
    if set(target_nodes).issubset(set(path)) and abs(cost_so_far - total_length) <= error:
        return path, cost_so_far

    if cost_so_far - total_length > error:
        return None, math.inf

    min_cost = math.inf
    min_path = None
    for neighbor, edge_cost in EDGES[node_id].items():
        if neighbor not in path: 
            next_path = path + [neighbor]
            next_cost = cost_so_far + edge_cost
            new_path, new_cost = search(neighbor, next_path, next_cost, target_nodes, total_length, error)
            if new_path is not None and new_cost < min_cost:
                min_cost = new_cost
                min_path = new_path

    return min_path, min_cost

def ida_star(start_node, targets, length, error):
    path, cost = search(start_node, [start_node], 0, targets, length, error)
    if path is not None:
        return path, cost
    return [], None