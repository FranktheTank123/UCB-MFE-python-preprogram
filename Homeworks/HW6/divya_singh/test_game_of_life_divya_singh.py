import pytest


def evolve(initial_state):
    c = len(initial_state[0])
    neighbours = [[0 for j in range(c)] for i in range(len(initial_state))]
    for p in range(len(initial_state)):
        for q in range(c):
            if initial_state[p][q] == 1:
                for r in [
                    [0, -1],
                    [0, 1],
                    [-1, -1],
                    [1, 1],
                    [-1, 0],
                    [1, 0],
                    [-1, 1],
                    [1, -1],
                ]:
                    if (
                        p + r[0] >= 0
                        and p + r[0] < len(initial_state)
                        and q + r[1] >= 0
                        and q + r[1] < c
                    ):
                        neighbours[p + r[0]][q + r[1]] += 1

    for m in range(len(initial_state)):
        for n in range(c):
            if initial_state[m][n] == 1 and (
                neighbours[m][n] != 2 and neighbours[m][n] != 3
            ):
                initial_state[m][n] = 0
            if initial_state[m][n] == 0 and neighbours[m][n] == 3:
                initial_state[m][n] = 1

    return initial_state


case_1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
]

case_2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

case_2_next = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


@pytest.mark.parametrize(
    "input, output", [(case_1, case_1), (case_2, case_2_next)],
)
def test_evolve(input, output):
    assert evolve(input) == output
