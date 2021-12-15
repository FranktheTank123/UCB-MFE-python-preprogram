
import copy

def evolve(initial_state):
    next_state = copy.deepcopy(initial_state)
    for i, row in enumerate(initial_state):
        for j, item in enumerate(row):
            total = 0
            for vertical in range(max(j-1, 0), min(j+2, len(row))):
                for horizontal in range(max(i-1, 0), min(i+2, len(row))):
                    if (i == horizontal) & (j == vertical):
                        continue
                    total += initial_state[horizontal][vertical]
            if total == 2:
                pass
            elif total == 3:
                next_state[i][j] = 1
            else:
                next_state[i][j] = 0
    return next_state


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
