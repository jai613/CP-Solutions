for _ in range(int(input())):
    rows, cols = [int(i) for i in input().split()]
    grid = []
    for _ in range(rows):
        grid.append(list(input()))
 
    cols_as_rows = []
    for c in range(cols):
        new_row = ''
        for r in range(rows):
            new_row += grid[r][c]
        cols_as_rows.append(new_row)
 
    state = 0
    for row in cols_as_rows:
        if state == 0 and 'v' in row:
            state = 1
            continue
        if state == 1 and 'i' in row:
            state = 2
            continue
        if state == 2 and 'k' in row:
            state = 3
            continue
        if state == 3 and 'a' in row:
            state = 4
            break
 
    if state == 4:
        print('YES')
    else:
        print('NO')