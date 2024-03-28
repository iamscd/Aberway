#! /bin/python

import time

from aberway_background_code import create, update, main_loop
from ida import ida_star

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
    ListOfNodeId, final_cost = ida_star(startPos, listOfNodesToPass, length, error)
    # ---------- ---------- ---------- ---------- ---------- ---------- ----------
    end = time.time_ns()
    update(ListOfNodeId, screen, bg, lineList, nodeList, startPos, listOfNodesToPass, length, error, end - start)
    print("Path taken:", ListOfNodeId)

path_update()
main_loop()