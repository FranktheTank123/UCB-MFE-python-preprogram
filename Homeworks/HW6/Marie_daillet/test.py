import numpy as np


def neighbors(A, k, m):
    n = np.shape(A)[0]
    N = []
    if k == 0 and m == 0:
        N = [A[0, 1], A[1, 0], A[1, 1]]
    elif k == 0 and m == (n - 1):
        N = [A[0, n - 2], A[1, n - 2], A[1, n - 1]]
    elif k == (n - 1) and m == 0:
        N = [A[n - 2, 0], A[n - 2, 1], A[n - 1, 1]]
    elif k == (n - 1) and m == (n - 1):
        N = [A[n - 1, n - 2], A[n - 2, n - 2], A[n - 2, n - 1]]
    elif k == 0 and m != 0:
        N = [A[0, m - 1], A[1, m - 1], A[1, m], A[1, m + 1], A[0, m + 1]]
    elif k == n - 1 and m != 0:
        N = [
            A[n - 1, m - 1],
            A[n - 2, m - 1],
            A[n - 2, m],
            A[n - 2, m + 1],
            A[n - 1, m + 1],
        ]
    elif m == 0 and k != 0:
        N = [A[k - 1, 0], A[k - 1, 1], A[k, 1], A[k + 1, 1], A[k + 1, 0]]
    elif m == n - 1 and k != 0:
        N = [
            A[k - 1, n - 1],
            A[k - 1, n - 2],
            A[k, n - 2],
            A[k + 1, n - 2],
            A[k + 1, n - 1],
        ]
    else:
        N = [
            A[k - 1, m],
            A[k - 1, m - 1],
            A[k, m - 1],
            A[k + 1, m - 1],
            A[k + 1, m],
            A[k + 1, m + 1],
            A[k, m + 1],
            A[k - 1, m + 1],
        ]
    return N


def evolve(initial):
    n = np.shape(initial)[0]
    V = np.zeros(np.shape(initial))
    for i in range(n):
        for j in range(n):
            if initial[i, j] == 1 and sum(neighbors(initial, i, j)) == 2:
                V[i, j] = 1
            elif initial[i, j] == 1 and sum(neighbors(initial, i, j)) == 3:
                V[i, j] = 1
            elif initial[i, j] == 0 and sum(neighbors(initial, i, j)) == 3:
                V[i, j] = 1
            else:
                V[i, j] = 0
    return V


test_case_1 = np.array(
    [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
)


test_case_2 = np.array(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)


test_case_2_next = np.array(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)


def test():
    assert (evolve(test_case_1) == test_case_1).all()
    assert (evolve(test_case_2) == test_case_2_next).all()
