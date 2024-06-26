#! /bin/python

from aberway_background_code import create, update, main_loop
import time

ColourFlip = False

screen, bg, lineList, nodeList = create(ColourFlip)
update(None, screen, bg, lineList, nodeList, None, None, None, None, 0)

# --- SET THESE VALUES TO AN EXAMPLE ---
# TEST 1
startPos = 0
listOfNodesToPass = [10,11,14]
length = 676.75
error = 0.06

# # TEST 2
startPos = 29
listOfNodesToPass = [34, 27, 17] 
length = 758.97
error = 0.06

# TEST 3
# startPos = 2
# listOfNodesToPass = [54, 51, 38, 36]
# length = 1038.42
# error = 0.07

# TEST 4
# startPos = 47
# listOfNodesToPass = [34, 19, 0, 12]
# length = 2044.79
# error = 0.14

def path_update():
    ListOfNodeId = []  # set the value of this to the nodes that your path takes
    start = time.time_ns()  # for timing your algorithm
    # ---------- ---------- YOUR CODE GOES HERE ---------- ----------
    
    graph_data = {
        "0": [["1", "219.8226557932553"], ["2", "167.4305826305338"], ["3", "129.40247292845683"], ["4", "373.75125417849773"]], "1": [["0", "219.8226557932553"], ["7", "182.3869512876401"], ["20", "364.9835612736552"], ["21", "373.60540681312415"]], "2": [["0", "167.4305826305338"], ["5", "281.3698633471609"], ["6", "159.29846201391902"], ["10", "67.06713054842886"], ["11", "198.4943324127921"]], "3": [["0", "129.40247292845683"], ["8", "203.3420763147657"], ["9", "146.696966567138"]], "4": [["0", "373.75125417849773"], ["5", "50.11985634456667"], ["57", "367.6955262170047"]], "5": [["4", "50.11985634456667"], ["2", "281.3698633471609"], ["6", "143.2515270424717"]], "6": [["2", "159.29846201391902"], ["5", "143.2515270424717"], ["11", "107.07007051459338"], ["12", "366.1816489121212"]], "7": [["1", "182.3869512876401"], ["24", "497.3529933558257"], ["56", "165.07574019219177"]], "8": [["3", "203.3420763147657"], ["9", "130.98091464026353"], ["20", "118.92854997854805"]], "9": [["3", "146.696966567138"], ["8", "130.98091464026353"], ["17", "151.5585695366646"], ["19", "48.83646178829912"]], "10": [["2", "67.06713054842886"], ["13", "158.4929020492716"], ["17", "117.6860229593982"]], "11": [["2", "198.4943324127921"], ["6", "107.07007051459338"], ["12", "302.87456149369825"], ["13", "92.66067126888301"], ["14", "152.0526224699857"]], "12": [["6", "366.1816489121212"], ["11", "302.87456149369825"], ["30", "227.1079038695043"]], "13": [["10", "158.4929020492716"], ["11", "92.66067126888301"], ["14", "125.67418191498204"]], "14": [["11", "152.0526224699857"], ["13", "125.67418191498204"], ["15", "39.05124837953327"]], "15": [["14", "39.05124837953327"], ["17", "292.083892058429"], ["16", "42.7551166528639"], ["30", "230.82894099310857"]], "16": [["15", "42.7551166528639"], ["18", "298.9648808806814"], ["29", "112.0044641967453"]], "17": [["9", "151.5585695366646"], ["10", "117.6860229593982"], ["15", "292.083892058429"], ["18", "74.33034373659252"]], "18": [["16", "298.9648808806814"], ["17", "74.33034373659252"], ["19", "177.2004514666935"], ["28", "84.17244204607586"], ["27", "114.86513831445988"]], "19": [["9", "48.83646178829912"], ["18", "177.2004514666935"], ["26", "75.7429864739964"]], "20": [["1", "364.9835612736552"], ["8", "118.92854997854805"], ["21", "37.12142238654117"], ["39", "126.21014222319853"]], "21": [["20", "37.12142238654117"], ["22", "36.87817782917155"], ["23", "48.703182647543684"], ["1", "373.60540681312415"]], "22": [["21", "36.87817782917155"], ["23", "49.193495504995376"], ["25", "82.20097323024831"]], "23": [["21", "48.703182647543684"], ["22", "49.193495504995376"], ["24", "54.91812087098393"]], "24": [["23", "54.91812087098393"], ["7", "497.3529933558257"], ["25", "181.89282558693733"]], "25": [["22", "82.20097323024831"], ["24", "181.89282558693733"], ["39", "74.72616676907762"], ["52", "204.51894777746145"]], "26": [["19", "75.7429864739964"], ["27", "166.96406799069075"], ["39", "93.81364506296512"]], "27": [["18", "114.86513831445988"], ["34", "122.93087488503447"], ["38", "86.31338250816034"], ["26", "166.96406799069075"]], "28": [["29", "228.47319317591726"], ["34", "106.04244433244644"], ["18", "84.17244204607586"]], "29": [["31", "167.14065932620943"], ["16", "112.0044641967453"], ["28", "228.47319317591726"], ["33", "141.40014144264495"]], "30": [["12", "227.1079038695043"], ["15", "230.82894099310857"], ["31", "201.55644370746373"]], "31": [["30", "201.55644370746373"], ["29", "167.14065932620943"], ["32", "54.378304497290095"]], "32": [["31", "54.378304497290095"], ["33", "196.4713719603953"], ["35", "211.68372634664195"]], "33": [["32", "196.4713719603953"], ["29", "141.40014144264495"], ["34", "187.7471704180918"], ["36", "81.98780397107853"]], "34": [["33", "187.7471704180918"], ["28", "106.04244433244644"], ["27", "122.93087488503447"], ["37", "80.05623023850174"]], "35": [["32", "211.68372634664195"], ["36", "148.94629904767692"], ["44", "56.92099788303083"], ["58", "336.93322780634145"]], "36": [["35", "148.94629904767692"], ["33", "81.98780397107853"], ["37", "174.18381095842403"], ["43", "98.2344135219425"]], "37": [["36", "174.18381095842403"], ["34", "80.05623023850174"], ["38", "156.16977940690063"], ["42", "69.65629906907199"]], "38": [["27", "86.31338250816034"], ["39", "150.30635382444748"], ["37", "156.16977940690063"], ["41", "49.33558553417604"]], "39": [["38", "150.30635382444748"], ["26", "93.81364506296512"], ["20", "126.21014222319853"], ["25", "74.72616676907762"], ["40", "87.66413177577246"]], "40": [["39", "87.66413177577246"], ["41", "169.84993376507393"], ["52", "98.71676655968832"]], "41": [["42", "107.80074211247342"], ["38", "49.33558553417604"], ["40", "169.84993376507393"], ["51", "72.78049189171504"]], "42": [["43", "169.09760495051373"], ["37", "69.65629906907199"], ["41", "107.80074211247342"]], "43": [["36", "98.2344135219425"], ["42", "169.09760495051373"], ["50", "110.34491379306978"], ["45", "168.58232410309213"]], "44": [["46", "343.1573982883073"], ["35", "56.92099788303083"], ["45", "84.50443775329198"]], "45": [["44", "84.50443775329198"], ["47", "198.03282556182447"], ["43", "168.58232410309213"]], "46": [["44", "343.1573982883073"], ["47", "152.46311029229332"], ["48", "174.0028735394907"]], "47": [["46", "152.46311029229332"], ["45", "198.03282556182447"], ["48", "65.86349520030045"]], "48": [["47", "65.86349520030045"], ["49", "61.1310068623117"], ["46", "174.0028735394907"]], "49": [["48", "61.1310068623117"], ["50", "332.66199061509866"], ["54", "328.16002194051606"]], "50": [["43", "110.34491379306978"], ["49", "332.66199061509866"], ["54", "131.04579352272242"], ["51", "212.7016690108472"]], "51": [["50", "212.7016690108472"], ["41", "72.78049189171504"], ["53", "188.74321179846442"], ["54", "290.80061898145954"]], "52": [["40", "98.71676655968832"], ["25", "204.51894777746145"], ["53", "211.00947846009194"], ["60", "180.93645293306707"]], "53": [["52", "211.00947846009194"], ["51", "188.74321179846442"], ["54", "196.91876497682998"], ["55", "177.00282483621552"], ["59", "58.60034129593445"]], "54": [["49", "328.16002194051606"], ["50", "131.04579352272242"], ["51", "290.80061898145954"], ["53", "196.91876497682998"], ["55", "65.36818798161687"]], "55": [["54", "65.36818798161687"], ["53", "177.00282483621552"]], "56": [["7", "165.07574019219177"]], "57": [["4", "367.6955262170047"]], "58": [["35", "336.93322780634145"]], "59": [["53", "58.60034129593445"]], "60": [["52", "180.93645293306707"]]
    }
        
    edges = {int(node): {int(neighbor): float(cost) for neighbor, cost in neighbors} for node, neighbors in graph_data.items()}

    def heuristic(node_id, target_nodes):
        return 0

    def search(node_id, path, cost_so_far, threshold, target_nodes):
        if not target_nodes and abs(cost_so_far - length) <= error:
            return path, cost_so_far

        if cost_so_far > threshold:
            return None, float('inf')

        min_cost = float('inf')
        for neighbor, edge_cost in edges[node_id].items():
            if neighbor not in path: 
                next_cost = cost_so_far + edge_cost
                if next_cost > threshold:
                    min_cost = min(min_cost, next_cost)
                    continue

                new_target_nodes = [n for n in target_nodes if n != neighbor]
                new_path, new_cost = search(neighbor, path + [neighbor], next_cost, threshold, new_target_nodes)
                
                if new_path is not None:
                    return new_path, new_cost
                else:
                    min_cost = min(min_cost, new_cost)

        return None, min_cost

    def ida_star(start_node, targets, max_length):
        threshold = heuristic(start_node, targets)
        while True:
            path, cost = search(start_node, [start_node], 0, threshold, targets)
            if path is not None:
                return path, cost
            if cost == float('inf'):
                return None, None
            threshold = cost 
# ---------- ---------- ---------- ---------- ---------- ---------- ----------
    ListOfNodeId, final_cost = ida_star(startPos, listOfNodesToPass, length)
    end = time.time_ns()
    update(ListOfNodeId, screen, bg, lineList, nodeList, startPos, listOfNodesToPass, length, error, end - start)
    print("Path taken:", ListOfNodeId)

path_update()
main_loop()
