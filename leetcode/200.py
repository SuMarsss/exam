#start time: 9.18PM

def numIslands(grid)  :
    if not grid:
        return 0
    dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    row_len = len(grid)
    col_len = len(grid[0])

    def dfs(i, j):
        stack = [(i, j)]
        while stack:
            i, j = stack.pop()
            for d in dire:
                nxt_i = i + d[0]
                nxt_j = j + d[1]
                # beyond boundary

                if 0<=nxt_i< row_len and 0<=nxt_j<col_len:
                    if grid[nxt_i][nxt_j] == "1":
                        grid[nxt_i][nxt_j] = "0"
                        stack.append((nxt_i, nxt_j))

    count = 0
    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                count += 1
                dfs(i, j)
    print(count)

grid = [["1","0","1","1","0","1","1"]]

numIslands(grid)
