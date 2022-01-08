def evolve(initial_state):
    row_len = len(initial_state)
    col_len = len(initial_state[0])
    evolve_state = [[0 for _ in range(col_len)] for _ in range(row_len)]

    for row in range(row_len):
        for col in range(col_len):
            # count alive neighbour (includes center cell)
            neighbour_alive = 0
            for n_row in range(max(row - 1, 0), min(row + 2, row_len)):
                for n_col in range(max(col - 1, 0), min(col + 2, col_len)):
                    neighbour_alive += initial_state[n_row][n_col]

            if not initial_state[row][col] and neighbour_alive == 3:
                evolve_state[row][
                    col
                ] = 1  # Any dead cell with 3 live neighbours becomes alive
            elif initial_state[row][col] and neighbour_alive - 1 in [2, 3]:
                evolve_state[row][
                    col
                ] = 1  # Any live cell with two or three live neighbours
            else:
                evolve_state[row][
                    col
                ] = 0  # All other live cells die in the next generation

    return evolve_state
