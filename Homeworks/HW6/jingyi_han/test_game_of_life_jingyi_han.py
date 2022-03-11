import pytest


def evolve(initial_state):
    # fill this out
    n = len(initial_state)
    neighbours = [[0] * len(initial_state[0]) for i in range(n)]
    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            if initial_state[i][j] == 1:
                for k in [
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
                        i + k[0] >= 0
                        and i + k[0] < len(initial_state)
                        and j + k[1] >= 0
                        and j + k[1] < len(initial_state[0])
                    ):
                        neighbours[i + k[0]][j + k[1]] += 1

    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            if initial_state[i][j] == 1 and (
                neighbours[i][j] != 2 and neighbours[i][j] != 3
            ):
                initial_state[i][j] = 0
            if initial_state[i][j] == 0 and neighbours[i][j] == 3:
                initial_state[i][j] = 1
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
    "input,output",
    [(case_1, case_1), (case_2, case_2_next)],
)
def test_evolve(input, output):
    assert evolve(input) == output
