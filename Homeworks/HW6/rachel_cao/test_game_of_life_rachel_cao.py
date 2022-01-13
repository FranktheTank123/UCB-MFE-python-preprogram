def evolve(initial_state):

    board = initial_state
    # create a temp array to fill in the next evolutionary state
    nextgen = [([0] * len(board)) for i in range(0, len(board[0]))]

    for i in range(0, len(board)):

        for j in range(0, len(board[i])):
            # let's assume that there aren't neighbors to begin with
            neighbors = 0
            # print("current piece: ", board[i][j])
            try:
                # since old code , up down left right
                if i < len(board) - 1:
                    neighbors += board[i + 1][j]  # to the right neighbor

                    if j < len(board[i]) - 1:
                        neighbors += board[i + 1][j + 1]  # up
                    if j > 0:
                        neighbors += board[i + 1][j - 1]  # down

                if i > 0:
                    neighbors += board[i - 1][j]  # to the left neighbor

                    if j > 0:
                        neighbors += board[i - 1][j - 1]  # up and down
                    if j < len(board[i]) - 1:
                        neighbors += board[i - 1][j + 1]

                if j < len(board[i]) - 1:
                    neighbors += board[i][j + 1]  # upper neighbor

                if j > 0:
                    neighbors += board[i][j - 1]  # lower neighbor

                if board[i][j] == 0 and neighbors == 3:
                    nextgen[i][j] = 1  # growth

                if (board[i][j] == 1) and neighbors == 2:
                    nextgen[i][j] = 1  # two or three neighbors lives on

                if (board[i][j] == 1) and neighbors == 3:
                    nextgen[i][j] = 1  # two or three neighbors lives on

                if board[i][j] == 1 and neighbors not in [2, 3]:
                    nextgen[i][j] = 0  # stagnation

            except IndexError:
                nextgen[i][j] = 0

    return nextgen
    pass


test_case_1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
]

test_case_2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

test_case_2_next = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


assert evolve(test_case_1) == test_case_1
assert evolve(test_case_2) == test_case_2_next
