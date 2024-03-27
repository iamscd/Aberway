#! /bin/python
import math
import random

import pygame


def create(ColourFlip):

    pygame.init()

    divVal = 2.5  # division value so that it fits on screen

    random.seed(a=0x5326478324724367635627432857846378)

    pygame.display.set_caption("AberWay")
    screen = pygame.display.set_mode([2588 / divVal, 1700 / divVal])  # screen size
    bg = pygame.image.load("map.png")  # image
    if ColourFlip:
        bg = pygame.image.load("mapI.png")  # colour flip image
    bg = pygame.transform.smoothscale(bg, (2588 / divVal, 1700 / divVal))  # image size

    # position of center of circle, radius, color, conectedtolist, ID
    nodeList = [
        [[1288, 634], 8, [50, 50, 255], [1, 2, 3, 4], 0],
        [[1507, 615], 8, [50, 50, 255], [0, 7, 20, 21], 1],
        [[1156, 737], 8, [50, 50, 255], [0, 5, 6, 10, 11], 2],
        [[1307, 762], 8, [50, 50, 255], [0, 8, 9], 3],
        [[947, 481], 8, [50, 50, 255], [0, 5, 57], 4],
        [[971, 525], 8, [50, 50, 255], [4, 2, 6], 5],
        [[1016, 661], 8, [50, 50, 255], [2, 5, 11, 12], 6],
        [[1578, 447], 8, [50, 50, 255], [1, 24, 56], 7],
        [[1465, 890], 8, [50, 50, 255], [3, 9, 20], 8],
        [[1335, 906], 8, [50, 50, 255], [3, 8, 17, 19], 9],
        [[1159, 804], 8, [50, 50, 255], [2, 13, 17], 10],
        [[958, 751], 8, [50, 50, 255], [2, 6, 12, 13, 14], 11],
        [[656, 728], 8, [50, 50, 255], [6, 11, 30], 12],
        [[1003, 832], 8, [50, 50, 255], [10, 11, 14], 13],
        [[890, 887], 8, [50, 50, 255], [11, 13, 15], 14],
        [[892, 926], 8, [50, 50, 255], [14, 17, 16, 30], 15],
        [[900, 968], 8, [50, 50, 255], [15, 18, 29], 16],
        [[1184, 919], 8, [50, 50, 255], [9, 10, 15, 18], 17],
        [[1198, 992], 8, [50, 50, 255], [16, 17, 19, 28, 27], 18],
        [[1368, 942], 8, [50, 50, 255], [9, 18, 26], 19],
        [[1545, 978], 8, [50, 50, 255], [1, 8, 21, 39], 20],
        [[1582, 981], 8, [50, 50, 255], [20, 22, 23, 1], 21],
        [[1606, 1009], 8, [50, 50, 255], [21, 23, 25], 22],
        [[1628, 965], 8, [50, 50, 255], [21, 22, 24], 23],
        [[1674, 935], 8, [50, 50, 255], [23, 7, 25], 24],
        [[1540, 1058], 8, [50, 50, 255], [22, 24, 39, 52], 25],
        [[1419, 998], 8, [50, 50, 255], [19, 27, 39], 26],
        [[1273, 1079], 8, [50, 50, 255], [18, 34, 38, 26], 27],
        [[1121, 1026], 8, [50, 50, 255], [29, 34, 18], 28],
        [[899, 1080], 8, [50, 50, 255], [31, 16, 28, 33], 29],
        [[663, 955], 8, [50, 50, 255], [12, 15, 31], 30],
        [[743, 1140], 8, [50, 50, 255], [30, 29, 32], 31],
        [[789, 1169], 8, [50, 50, 255], [31, 33, 35], 32],
        [[984, 1193], 8, [50, 50, 255], [32, 29, 34, 36], 33],
        [[1159, 1125], 8, [50, 50, 255], [33, 28, 27, 37], 34],
        [[902, 1348], 8, [50, 50, 255], [32, 36, 44, 58], 35],
        [[1025, 1264], 8, [50, 50, 255], [35, 33, 37, 43], 36],
        [[1187, 1200], 8, [50, 50, 255], [36, 34, 38, 42], 37],
        [[1332, 1142], 8, [50, 50, 255], [27, 39, 37, 41], 38],
        [[1468, 1078], 8, [50, 50, 255], [38, 26, 20, 25, 40], 39],
        [[1485, 1164], 8, [50, 50, 255], [39, 41, 52], 40],
        [[1317, 1189], 8, [50, 50, 255], [42, 38, 40, 51], 41],
        [[1231, 1254], 8, [50, 50, 255], [43, 37, 41], 42],
        [[1086, 1341], 8, [50, 50, 255], [36, 42, 50, 45], 43],
        [[920, 1402], 8, [50, 50, 255], [46, 35, 45], 44],
        [[974, 1467], 8, [50, 50, 255], [44, 47, 43], 45],
        [[669, 1636], 8, [50, 50, 255], [44, 47, 48], 46],
        [[810, 1578], 8, [50, 50, 255], [46, 45, 48], 47],
        [[843, 1635], 8, [50, 50, 255], [47, 49, 46], 48],
        [[904, 1631], 8, [50, 50, 255], [48, 50, 54], 49],
        [[1162, 1421], 8, [50, 50, 255], [43, 49, 54, 51], 50],
        [[1301, 1260], 8, [50, 50, 255], [50, 41, 53, 54], 51],
        [[1508, 1260], 8, [50, 50, 255], [40, 25, 53, 60], 52],
        [[1383, 1430], 8, [50, 50, 255], [52, 51, 54, 55, 59], 53],
        [[1219, 1539], 8, [50, 50, 255], [49, 50, 51, 53, 55], 54],
        [[1276, 1571], 8, [50, 50, 255], [54, 53], 55],
        [[1573, 282], 8, [50, 50, 255], [7], 56],
        [[591, 389], 8, [50, 50, 255], [4], 57],
        [[572, 1416], 8, [50, 50, 255], [35], 58],
        [[1336, 1395], 8, [50, 50, 255], [53], 59],
        [[1561, 1433], 8, [50, 50, 255], [52], 60],
    ]

    # valA, valB, color, more than two points for the line?, connecting nodes, weight
    # e.g.  [1288,634],[1507,615], [129, 129, 255], False, [1,2], 54
    # --------------------OR IF THERE ARE MORE THAN TWO -------------------------
    # points, None, color, more than two points for the line?, connecting nodes, weight
    # e.g.  [[1288,634],[1507,615],[1156,737]], None, [129, 129, 255], True, [1,2], 54
    #            _______________________________/
    #           /
    # there is None at the postion [1] so that the colour is always on [2]
    lineList = []
    usedPairs = []

    for node in nodeList:
        for val in node[3]:
            if ([node[4], val] not in usedPairs) and ([val, node[4]] not in usedPairs):
                usedPairs.append([node[4], val])
                block = []
                block.append(nodeList[node[4]][0])  # first point
                block.append(nodeList[val][0])  # second point
                block.append([129, 129, 255])  # colour in RGB
                block.append(False)  # more than two points bool
                block.append([node[4], val])  # ID of nodes
                block.append(0)  # will be the weight
                lineList.append(block)

    # lines that have more than one point [PURELY VISUAL]
    checks = [
        [[6, 12], [[811, 545], [653, 565]]],
        [[4, 0], [[1201, 544]]],
        [[5, 2], [[1100, 549]]],
        [[1, 21], [[1616, 627], [1640, 802]]],
        [[24, 7], [[1716, 472], [1715, 906]]],
        [[25, 24], [[1720, 1012], [1693, 1081]]],
        [[52, 25], [[1590, 1176]]],
        [[51, 53], [[1373, 1319]]],
        [[32, 33], [[900, 1212]]],
        [[14, 11], [[897, 810]]],
        [[52, 53], [[1493, 1414]]],
        [[53, 54], [[1293, 1438]]],
        [[3, 9], [[1284, 821]]],
        [[54, 49], [[1096, 1624]]],
        [[39, 20], [[1551, 1017], [1474, 1053]]],
        [[4, 57], [[812, 460], [703, 392]]],
        [[46, 44], [[625, 1550]]],
        [[53, 59], [[1372, 1378]]],
    ]
    for line in lineList:
        for c in checks:
            check = c[0]
            check2 = check
            check.reverse()
            if line[4] == check or line[4] == check2:
                cVals = []
                cVals.append(line[0])
                for i in c[1]:
                    cVals.append(i)
                cVals.append(line[1])
                line[0] = cVals
                line[1] = None
                line[3] = True

    # calculating weightings
    for line in lineList:
        r = random.randint(0, 200)
        weight = r
        if line[3]:
            for i in range(1, len(line[0])):
                weight += math.dist(line[0][i - 1], line[0][i])
        else:
            weight += math.dist(line[0], line[1])
        line[5] = round(weight, 2)
        line[2] = [
            50 + r,
            100,
            255,
        ]  # the more pink (the higher the R value) the higher the weight

    if ColourFlip:
        for node in nodeList:
            node[2][0] = 255 - node[2][0]
            node[2][1] = 255 - node[2][1]
            node[2][2] = 255 - node[2][2]

        for line in lineList:
            line[2][0] = 255 - line[2][0]
            line[2][1] = 255 - line[2][1]
            line[2][2] = 255 - line[2][2]

    return screen, bg, lineList, nodeList


# small function to print the duration time
def print_completion_time(duration):
    nano = duration % 1000
    duration //= 1000
    micro = duration % 1000
    duration //= 1000
    milli = duration % 1000
    duration //= 1000
    print(f"Algorithm execution time: {duration}s, {milli}ms, {micro}μs, {nano}ns")


# --- MAIN LOOP ---
# nodes it passes
def update(
    NodePassIdList,
    screen,
    bg,
    lineList,
    nodeList,
    startPos,
    listOfNodesToPass,
    length,
    error,
    duration,
):

    divVal = 2.5  # division value so that it fits on screen

    if startPos != None:
        NodePassIdList = [startPos] + NodePassIdList

    # make white the list of nodes that it passes
    contiguousLineCount = 0
    totalDist = 0
    if NodePassIdList != None:
        for n in NodePassIdList:
            nodeList[n][2] = [255, 140, 0]

        for i in range(0, len(NodePassIdList) - 1):
            # in case the algorithm wants to sit still for a while
            if NodePassIdList[i] == NodePassIdList[i + 1]:
                contiguousLineCount += 1
                continue
            for line in lineList:
                l = line[4]
                if l == [NodePassIdList[i], NodePassIdList[i + 1]]:

                    # add the distance that has been traveled
                    if line[1] != None:
                        totalDist += math.dist(line[0], line[1])
                    else:
                        totalDist += math.dist(line[0][-1], line[0][0])

                    line[2] = [255, 140, 0]
                    contiguousLineCount += 1

                l.reverse()
                if l == [NodePassIdList[i], NodePassIdList[i + 1]]:

                    # add the distance that has been traveled
                    if line[1] != None:
                        totalDist += math.dist(line[0], line[1])
                    else:
                        totalDist += math.dist(line[0][-1], line[0][0])

                    line[2] = [255, 140, 0]
                    contiguousLineCount += 1

        # check if the result is valid
        if contiguousLineCount == len(NodePassIdList) - 1:
            necissaryNodes = False
            for n in listOfNodesToPass:
                if n in NodePassIdList:
                    necissaryNodes = True
            if necissaryNodes:
                if (totalDist > length - error) and (totalDist < length + error):
                    print("Success")
                    print_completion_time(duration)
                else:
                    print(
                        f"The distance is not within the acceptable range: got {totalDist}, wanted {length}, error {error}"
                    )
                    print_completion_time(duration)
            else:
                print("Not all required nodes were passed")
                print_completion_time(duration)
        else:
            print("The line is not contiguous")

    running = True
    finished = False  # finished traversal

    # set bachgound to white, and image
    screen.fill([255, 255, 255])
    screen.blit(bg, (0, 0))

    # draw lines between nodes
    for l in lineList:
        if not l[3]:  # if it only has two points
            pygame.draw.lines(
                screen,
                l[2],
                False,
                [
                    [l[0][0] / divVal, l[0][1] / divVal],
                    [l[1][0] / divVal, l[1][1] / divVal],
                ],
                width=3,
            )
        else:  # if it has more than two points
            points = []
            for vals in l[0]:
                point = []
                point.append(vals[0] / divVal)
                point.append(vals[1] / divVal)
                points.append(point)

            pygame.draw.lines(screen, l[2], False, points, width=3)

    # draw nodes
    for node in nodeList:
        pygame.draw.circle(
            screen,
            node[2],
            [node[0][0] / divVal, node[0][1] / divVal],
            node[1],
            width=3,
        )

    pygame.display.flip()  # updates code


def main_loop():
    quit = False
    clock = pygame.time.Clock()
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
        clock.tick(30)
    pygame.quit()
