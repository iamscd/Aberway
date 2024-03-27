import csv
import math


def euclidean_distance_2d(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Calculate the Euclidean distance
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance


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
node_list = []
for node in nodeList:
    x_y = node[0]
    id = node[-1]
    connected_to = node[-2]
    node_list.append([id, x_y, connected_to])


cost_matrix = []
for node1 in node_list:
    cost_for_node1 = []
    for node2 in node_list:
        if node1[0] in node2[-1]:  # check if connected to
            cost_for_node1.append(euclidean_distance_2d(node1[1], node2[1]))
        else:
            cost_for_node1.append(-1)
    cost_matrix.append(cost_for_node1)

with open("cost_matix.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(cost_matrix)
