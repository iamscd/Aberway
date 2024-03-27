#! /bin/python

import time

from aberway_background_code import create, main_loop, update

ColourFlip = False


screen, bg, lineList, nodeList = create(ColourFlip)
update(None, screen, bg, lineList, nodeList, None, None, None, None, 0)


# --- SET THESE VALUES TO AN EXAMPLE ---
startPos = 0
listOfNodesToPass = [10, 11, 14]
length = 676.75
error = 0.06


def path_update():
    ListOfNodeId = []  # set the value of this to the nodes that your path takes
    start = time.time_ns()  # for timing your algorithm
    # ---------- ---------- YOUR CODE GOES HERE ---------- ----------

    # ---------- ---------- ---------- ---------- ---------- ---------- ----------
    end = time.time_ns()
    update(
        ListOfNodeId,
        screen,
        bg,
        lineList,
        nodeList,
        startPos,
        listOfNodesToPass,
        length,
        error,
        end - start,
    )


path_update()
main_loop()
