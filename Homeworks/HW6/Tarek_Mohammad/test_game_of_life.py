import pytest

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


def evolve(initial_state):
    row_indexing = len(initial_state)
    col_indexing = len(initial_state[0])
    evolved_state = [([0] * row_indexing) for _ in range(col_indexing)]
    neighbors = [([0] * row_indexing) for _ in range(col_indexing)]

    for row_index in range(row_indexing):
        for col_index in range(col_indexing):
            for (neighbor_row, neighbor_col) in [
                [row_index, col_index + 1],
                [row_index - 1, col_index + 1],
                [row_index - 1, col_index],
                [row_index - 1, col_index - 1],
                [row_index, col_index - 1],
                [row_index + 1, col_index - 1],
                [row_index + 1, col_index],
                [row_index + 1, col_index + 1],
            ]:
                if (
                    initial_state[row_index][col_index] == 1
                    and neighbor_row >= 0
                    and neighbor_row < row_indexing
                    and neighbor_col >= 0
                    and neighbor_col < col_indexing
                ):
                    neighbors[neighbor_row][neighbor_col] += 1
    for _ in range(row_indexing):
        for __ in range(col_indexing):
            if (initial_state[_][__] == 1) and (
                neighbors[_][__] == 2 or neighbors[_][__] == 3
            ):
                evolved_state[_][__] = 1
            if (initial_state[_][__] == 0) and (neighbors[_][__] == 3):
                evolved_state[_][__] = 1
    return evolved_state


@pytest.mark.parametrize(
    "input_case,output_case", [(case_1, case_1), (case_2, case_2_next)]
)
def test_evolve(input_case, output_case):
    assert evolve(input_case) == output_case
