import pytest
from ida import ida_star

@pytest.mark.parametrize("startPos, listOfNodesToPass, length, error, expect", [
    (0, [10,11, 14], 676.75, 0.06, [0, 2, 10, 13, 11, 14, 15]),
    (29, [34, 27, 17], 758.97, 0.06, [29, 33, 34, 27, 18, 17, 10]),
    (53, [54, 51, 38, 36], 1038.42, 0.07, [53, 54, 51, 41, 38, 37, 36, 43]),
    (47, [34, 19, 0, 12], 2044.79, 0.14, [47, 45, 43, 42, 37, 34, 27, 26, 19 ,9, 3, 0 ,2, 11, 12]),
])
def test_algo(startPos, listOfNodesToPass, length, error, expect):
    ListOfNodeId, final_cost = ida_star(startPos, listOfNodesToPass, length, error)

    assert ListOfNodeId == expect
