def evolve(initial_state):
	neighbours = [[ 0 for j in range(len(initial_state[0]))] for i in range(len(initial_state))]
	for p in range(len(initial_state)):
		for q in range(len(initial_state[0])):
			if initial_state[p][q] == 1:
				for r in [[0,-1],[0,1],[-1,-1],[1,1],[-1,0],[1,0],[-1,1],[1,-1]]:
					if p+r[0]>=0 and p+r[0]<len(initial_state) and q+r[1]>=0 and q+r[1]<len(initial_state[0]):
						neighbours[p+r[0]][q+r[1]] = neighbours[p+r[0]][q+r[1]] + 1


	for m in range(len(initial_state)):
        	for n in range(len(initial_state[0])):
            		if initial_state[m][n] == 1 and (neighbours[m][n] != 2 and neighbours[m][n] != 3):
                		initial_state[m][n] = 0
            		if initial_state[m][n] == 0 and neighbours[m][n] == 3:
                		initial_state[m][n] = 1

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
