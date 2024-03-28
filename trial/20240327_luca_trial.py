#! /bin/python

from aberway_background_code import create, update, main_loop
import time
import math

ColourFlip = False

    
screen, bg, lineList, nodeList = create(ColourFlip)
update(None, screen, bg, lineList, nodeList, None, None, None, None, 0)


# --- SET THESE VALUES TO AN EXAMPLE ---
# TEST 1
# startPos = 0
# listOfNodesToPass = [10,11,14]
# length = 676.75
# error = 0.06

# # TEST 2
# startPos = 29
# listOfNodesToPass = [34, 27, 17] 
# length = 758.97
# error = 0.06

# TEST 3
# startPos = 53
# listOfNodesToPass = [54, 51, 38, 36]
# length = 1038.42
# error = 0.07

# TEST 4
startPos = 47
listOfNodesToPass = [34, 19, 0, 12]
length = 2044.79
error = 0.14

def path_update():
    ListOfNodeId = []  # set the value of this to the nodes that your path takes
    start = time.time_ns()  # for timing your algorithm
    # ---------- ---------- YOUR CODE GOES HERE ---------- ----------
    
        
    edges = {int(node): {int(neighbor): float(cost) for neighbor, cost in neighbors} for node, neighbors in graph_data.items()}

    def search(node_id, path, cost_so_far, target_nodes, total_length, error):
        if set(target_nodes).issubset(set(path)) and abs(cost_so_far - total_length) <= error:
            return path, cost_so_far

        if cost_so_far - total_length > error:
            return None, math.inf

        min_cost = math.inf
        min_path = None
        for neighbor, edge_cost in edges[node_id].items():
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
# ---------- ---------- ---------- ---------- ---------- ---------- ----------
    ListOfNodeId, final_cost = ida_star(startPos, listOfNodesToPass, length, error)
    end = time.time_ns()
    update(ListOfNodeId, screen, bg, lineList, nodeList, startPos, listOfNodesToPass, length, error, end - start)
    print("Path taken:", ListOfNodeId)

path_update()
main_loop()