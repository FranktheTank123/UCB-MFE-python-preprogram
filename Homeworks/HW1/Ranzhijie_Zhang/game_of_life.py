Ranzhijie,Zhang,The Truman Show


def evolve(initial_state):
    import copy
    ans = copy.deepcopy(initial_state)

    new_length = len(initial_state[0])+2
    new_width  = len(initial_state)+2
    first, last = [[5]*new_length], [[5]*new_length]
    for i in ans:
       i.insert(0,5)
       i.append(5)
    first.extend(ans)
    first.extend(last)
    # now use loop to count
    for i in range(1,new_width-1):
        for j in range(1,new_length-1):
            live = 0
            for t in range(j-1,j+2):
                if first[i-1][t]==1:
                    live = live+1
                if first[i+1][t] ==1:
                    live = live+1
                if first[i][t]==1 and t!=j:
                    live = live+1
            print(live)
            if first[i][j]==0 and live ==3:
                    initial_state[i-1][j-1]=1
            if first[i][j]==1 and (live<2 or live>3):
                    initial_state[i-1][j-1] =0
  
    return initial_state

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
  
