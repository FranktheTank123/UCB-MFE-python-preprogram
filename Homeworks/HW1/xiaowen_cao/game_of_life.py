def evolve(initial_state):
    l = len(initial_state)
    ans = []
    
    for i in range(l):
        ans1 = []
        for j in range(l):
            neigh = initial_state[max(0,i-1):min(l,i+2)]
            neigh = list(map(lambda x:x[max(0,j-1):min(l,j+2)],neigh))
            neighbors = []
            for p in neigh:
                neighbors.extend(p)
            num_live = sum(neighbors)-initial_state[i][j]
            
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


assert evolve(test_case_1) == test_case_1
assert evolve(test_case_2) == test_case_2_next
