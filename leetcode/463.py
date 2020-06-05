## starting time  2020年6月5日22:20:31
## terminal time 2020年6月5日22:53:18
## 33 min
def islandPerimeter(grid):
    row_len = len(grid)
    col_len = len(grid[0])
    FlagMap = [[0 for i in range(col_len)] for j in range(row_len)]
    dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1:
                FlagMap[i][j] = 1
                break
        else:
            continue
        break

    stack = [(i, j)]
    preimeter = 0
    while stack:
        i, j = stack.pop()
        cell_p = 0
        for d in dire:
            nxt_i, nxt_j = i + d[0], j + d[1]
            if 0 <= nxt_i < row_len and 0 <= nxt_j < col_len:
                if grid[nxt_i][nxt_j] == 1 :
                    cell_p += 1
                    if FlagMap[nxt_i][nxt_j] == 0:
                        stack.append((nxt_i, nxt_j))
                        FlagMap[nxt_i][nxt_j] = 1
        sub_p = 4 - cell_p
        preimeter += sub_p
    return preimeter

grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

print(islandPerimeter(grid))