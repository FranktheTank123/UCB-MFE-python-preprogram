def evolve(initial_state):
    # fill this out
    length = len(initial_state)
    modified = []
    for i in range(0, length):
        case_row = []
        if i < 1:
            for j in range(0, length):
                if j < 1:
                    if initial_state[i][j] == 1:
                        if initial_state[i][j+1] + initial_state[i+1][j] +initial_state[i+1][j+1] < 2:
                            case_row.append(0)
                        else:
                            case_row.append(initial_state[i][j])
                    elif initial_state[i][j] == 0:
                        if initial_state[i][j+1] + initial_state[i+1][j] +initial_state[i+1][j+1] == 3:
                           case_row.append(1)
                        else:
                           case_row.append(initial_state[i][j])
                elif j < length-1:
                    if initial_state[i][j] == 1:
                        if 1 < initial_state[i][j-1] + initial_state[i][j+1] + initial_state[i+1][j-1] + \
                                initial_state[i][j+1] + initial_state[i+1][j+1] < 4:
                            case_row.append(initial_state[i][j])
                        else:
                            case_row.append(0)
                    elif initial_state[i][j-1] + initial_state[i][j+1] + initial_state[i+1][j-1] + \
                                initial_state[i+1][j] + initial_state[i+1][j+1] == 3:
                        case_row.append(1)
                    else:
                        case_row.append(initial_state[i][j])
                elif j == length-1:
                    if initial_state[i][j] == 1:
                        if initial_state[i][j-1] + initial_state[i+1][j-1] + initial_state[i+1][j] < 2:
                            case_row.append(0)
                    elif initial_state[i][j-1] + initial_state[i+1][j-1] + initial_state[i+1][j] == 2:
                            case_row.append(1)
                    else:
                        case_row.append(initial_state[i][j])
            modified.append(case_row)
        if 0 < i < length-1:
            for j in range(0, length):
                if j < 1:
                    if initial_state[i][j] == 1:
                        if 1 < initial_state[i-1][j] + initial_state[i-1][j+1] + initial_state[i][j+1] + \
                                initial_state[i+1][j] + initial_state[i+1][j+1] < 4:
                            case_row.append(initial_state[i][j])
                        else:
                            case_row.append(0)
                    elif initial_state[i-1][j] + initial_state[i-1][j+1] + initial_state[i][j+1] + \
                                initial_state[i+1][j] + initial_state[i+1][j+1] == 3:
                        case_row.append(1)
                    else:
                        case_row.append(initial_state[i][j])
                elif 0 < j < length-1:
                    if initial_state[i][j] == 1:
                        if 1 < initial_state[i-1][j-1] + initial_state[i-1][j] + initial_state[i-1][j+1] + \
                                initial_state[i][j-1] + initial_state[i][j+1] + initial_state[i+1][j-1] + \
                                initial_state[i+1][j] + initial_state[i+1][j+1] < 4:
                            case_row.append(initial_state[i][j])
                        else:
                            case_row.append(0)
                    elif initial_state[i-1][j-1] + initial_state[i-1][j] + initial_state[i-1][j+1] + \
                                initial_state[i][j-1] + initial_state[i][j+1] + initial_state[i+1][j-1] + \
                                initial_state[i+1][j] + initial_state[i+1][j+1] == 3:
                        case_row.append(1)
                    else:
                        case_row.append(initial_state[i][j])
                else:
                    if initial_state[i][j] == 1:
                        if 1 < initial_state[i-1][j-1] + initial_state[i-1][j] + initial_state[i][j-1] + \
                                initial_state[i+1][j-1] + initial_state[i+1][j] < 4:
                            case_row.append(initial_state[i][j])
                        else:
                            case_row.append(0)
                    elif initial_state[i-1][j-1] + initial_state[i-1][j] + initial_state[i][j-1] + \
                                initial_state[i+1][j-1] + initial_state[i+1][j] == 3:
                        case_row.append(1)
                    else:
                        case_row.append(initial_state[i][j])
            modified.append(case_row)
        elif i == length-1:
            for j in range(0, length):
                if j < 1:
                    if initial_state[i][j] == 1:
                        if initial_state[i-1][j] + initial_state[i-1][j+1] +initial_state[i][j+1] < 2:
                            case_row.append(0)
                        else:
                           case_row.append(initial_state[i][j])
                    elif initial_state[i][j] == 0:
                        if initial_state[i-1][j] + initial_state[i-1][j+1] +initial_state[i][j+1] == 3:
                           case_row.append(1)
                        else:
                           case_row.append(initial_state[i][j])
                elif j < length-1:
                    if initial_state[i][j] == 1:
                        if 1 < initial_state[i-1][j-1] + initial_state[i-1][j] + initial_state[i-1][j+1] + \
                                initial_state[i][j-1] + initial_state[i][j+1] < 4:
                            case_row.append(initial_state[i][j])
                        else:
                            case_row.append(0)
                    elif initial_state[i-1][j-1] + initial_state[i-1][j] + initial_state[i-1][j+1] + \
                                initial_state[i][j-1] + initial_state[i][j+1]  == 3:
                        case_row.append(1)
                    else:
                        case_row.append(initial_state[i][j])
                elif j == length-1:
                    if initial_state[i][j] == 1:
                        if initial_state[i-1][j-1] + initial_state[i-1][j] + initial_state[i][j-1] < 2:
                            case_row.append(0)
                    elif initial_state[i-1][j-1] + initial_state[i-1][j] + initial_state[i][j-1] == 2:
                            case_row.append(1)
                    else:
                        case_row.append(initial_state[i][j])
            modified.append(case_row)

    return(modified)
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
