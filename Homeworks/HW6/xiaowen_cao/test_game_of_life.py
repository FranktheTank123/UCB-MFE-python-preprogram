def evolve(initial_state):
    length = len(initial_state)
    ans = []

    for i in range(length):
        ans1 = []
        for j in range(length):
            min_r = max(0, i - 1)
            max_r = min(length, i + 2)
            neigh = initial_state[min_r:max_r]

            min_c = max(0, j - 1)
            max_c = min(length, j + 2)
            neigh = map(lambda x: x[min_c:max_c], neigh)
            neigh = list(neigh)
            neighbors = []
            for p in neigh:
                neighbors.extend(p)
            num_live = sum(neighbors) - initial_state[i][j]

            if initial_state[i][j] == 1 and num_live == 2:
                ans1.append(1)
            elif num_live == 3:
                ans1.append(1)
            else:
                ans1.append(0)
        ans.append(ans1)
    return ans
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


def test_evolve():
    assert evolve(test_case_1) == test_case_1
    assert evolve(test_case_2) == test_case_2_next
