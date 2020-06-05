def maxAreaOfIsland( grid) :
    row_len = len(grid)
    col_len = len(grid[0])

    dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    maxArea = 0
    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1:
                grid[i][j] = 0
                subMax = 1
                stack = [(i, j)]
                while stack:
                    i, j = stack.pop()
                    for d in dire:
                        nxt_i, nxt_j = i + d[0], j + d[1]
                        if 0 <= nxt_i < row_len and 0 <= nxt_j < col_len:
                            if grid[nxt_i][nxt_j] == 1:
                                subMax += 1
                                grid[nxt_i][nxt_j] = 0
                                stack.append((nxt_i, nxt_j))
                maxArea = max(maxArea, subMax)
    return maxArea

grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
print(maxAreaOfIsland( grid))