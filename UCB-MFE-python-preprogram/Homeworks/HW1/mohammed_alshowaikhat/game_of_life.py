def evolve(initial_state):
    rows=len(initial_state)
    cols=len(initial_state[0])
    count=0
    new_state = [[0 for i in range(rows)] for j in range(cols)]
    for r in range(rows):
      for c in range(cols):
        count=0
        for vert in range(c-1,c+2):
          for hori in range(r-1,r+2):
            if vert < 0 or vert > (rows-1) or hori < 0 or hori > (rows-1):
              continue
            else:
              if(r==hori and c==vert):
                  continue
              else:
                  count+=initial_state[hori][vert]
        if count==2 and initial_state[r][c]==1:
          new_state[r][c]=1
        elif count==3:
          new_state[r][c]=1
        else:
          new_state[r][c]=0

    return new_state


    

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


assert evolve(test_case_1)  == test_case_1
assert evolve(test_case_2) == test_case_2_next
