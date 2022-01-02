def evolve(initial_state):
    # fill this out
	rows = len(initial_state) 
	columns = len(initial_state[0])

	matrix = [[0 for j in range(columns)] for i in range(rows)]
	for i in range(rows):
		for j in range(columns):
			if initial_state[i][j] == 1:
				for k in [[0,-1],[0,1],[-1,-1],[1,1],[-1,0],[1,0],[-1,1],[1,-1]]:
					if i+k[0] >= 0 and i+k[0] < len(initial_state) and j+k[1] >= 0 and j+k[1] < len(initial_state[0]):
						matrix[i+k[0]][j+k[1]] += 1

	for i in range(rows):
		for j in range(columns):
			if initial_state[i][j] == 1 and (matrix[i][j] != 2 and matrix[i][j] != 3):
				initial_state[i][j] = 0
			if initial_state[i][j] == 0 and matrix[i][j] == 3:
				initial_state[i][j] = 1
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
