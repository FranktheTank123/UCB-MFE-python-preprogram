def evolve(initial_state):
    X = initial_state.copy()
    R = len(X)
    C = len(X)

    Output = []

    # calculate sum of neighbors
    for i in range(R):
        Output_row =[]
        for j in range(C):
            sum = 0
            if i == 0 and j == 0:
                sum = X[i][j+1] + X[i+1][j] + X[i+1][j+1]
            elif i == 0 and j == C-1:
                sum = X[i+1][j] + X[i][j-1] + X[i+1][j-1]
            elif i == R-1 and j == 0:
                sum = X[i-1][j] + X[i][j+1] + X[i-1][j+1]
            elif i == R-1 and j == C-1:
                sum = X[i-1][j] + X[i][j-1] + X[i-1][j-1]
            elif j == 0 and i in range(1,R-1):
                sum = X[i-1][j] + X[i+1][j] + X[i][j+1] + X[i-1][j+1] + X[i+1][j+1]
            elif j == C-1 and i in range(1,R-1):
                sum = X[i-1][j] + X[i+1][j] + X[i][j-1] + X[i-1][j-1] + X[i+1][j-1]
            elif i == 0 and j in range(1,C-1):
                sum = X[i][j-1] + X[i][j+1] + X[i+1][j] + X[i+1][j-1] + X[i+1][j+1]
            elif i == R-1 and j in range(1,C-1):
                sum = X[i][j-1] + X[i][j+1] + X[i-1][j] + X[i-1][j-1] + X[i-1][j+1]
            else:
                sum = X[i-1][j-1] + X[i-1][j] + X[i-1][j+1] + X[i][j-1] + X[i][j+1] + X[i+1][j-1] + X[i+1][j] + X[i+1][j+1]

        # Advance cycle
            if X[i][j] == 1:
                if sum == 2 or sum == 3:
                    Output_row.append(1)
                else:
                    Output_row.append(0)
            elif X[i][j] == 0:
                if sum == 3:
                    Output_row.append(1)
                else:
                    Output_row.append(0)

        Output.append(Output_row)

    return Output

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
