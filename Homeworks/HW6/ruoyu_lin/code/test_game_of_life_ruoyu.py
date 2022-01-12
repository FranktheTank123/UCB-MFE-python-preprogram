def evolve(initial_state):
    # padding
    padded = (
        [[0] * (len(initial_state[0]) + 2)]
        + [[0] + x + [0] for x in initial_state]
        + [[0] * (len(initial_state[0]) + 2)]
    )

    # initializing

    conv_mat = []  # initialized conv matrix
    conv_sum = 0  # initialize sum of neighbors
    out_padded = [[0] * len(padded[0]) for x in padded]
    # initialize output matrix

    # looping
    for nrow in range(1, 1 + len(initial_state)):
        # loop through rows of padded
        for ncol in range(1, 1 + len(initial_state[0])):
            # loop through cols of padded

            # compute convolution sum
            i1 = ncol - 1
            j1 = ncol + 2
            i2 = nrow - 1
            j2 = nrow + 2
            cols = padded[i2:j2]
            conv_mat = [x[i1:j1] for x in cols]
            conv_sum = (
                sum([sum(x) for x in conv_mat]) - padded[nrow][ncol]
            )  # sum of all minus self

            # treat living case
            if padded[nrow][ncol] == 1:
                if conv_sum == 2 or conv_sum == 3:
                    out_padded[nrow][ncol] = 1
                else:
                    out_padded[nrow][ncol] = 0

            # treat dead case
            elif padded[nrow][ncol] == 0:
                if conv_sum == 3:
                    out_padded[nrow][ncol] = 1
                else:
                    out_padded[nrow][ncol] = 0

            # just in case, for non-boolean entries
            else:
                raise "Error: entry non-binary."

    # Depadding
    i = len(out_padded) - 1
    j = len(out_padded[0]) - 1
    cols = out_padded[1:i]
    out_padded = [x[1:j] for x in cols]
    return out_padded


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


def test_1():
    assert evolve(test_case_1) == test_case_1
    pass


def test_2():
    assert evolve(test_case_2) == test_case_2_next
    pass


# assert evolve(test_case_1) == test_case_1
# assert evolve(test_case_2) == test_case_2_next

##
