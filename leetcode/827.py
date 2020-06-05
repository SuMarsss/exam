grid =[[0,1,0],[1,0,1],[1,0,0]]
row_len = len(grid)
col_len = len(grid[0])
FlagMap = [[0 for i in range(col_len)] for j in range(row_len)]
dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
lake_dict = {}
maxArea = 1
for ii in range(row_len):
    for jj in range(col_len):
        if grid[ii][jj] == 1 and FlagMap[ii][jj] == 0:
            FlagMap[ii][jj] = 1
            lake_set = set()

            stack = [(ii, jj)]
            area = 1
            while stack:
                i, j = stack.pop()
                for d in dire:
                    nxt_i, nxt_j = i + d[0], j + d[1]
                    if 0 <= nxt_i < row_len and 0 <= nxt_j < col_len:
                        if grid[nxt_i][nxt_j] == 1 and FlagMap[nxt_i][nxt_j] == 0:
                            FlagMap[nxt_i][nxt_j] = 1
                            stack.append((nxt_i, nxt_j))
                            area += 1

                        if grid[nxt_i][nxt_j] == 0 and (nxt_i, nxt_j) not in lake_set:
                            lake_set.add((nxt_i, nxt_j))

            for lake in lake_set:
                if lake in lake_dict:
                    lake_dict[lake] += area
                else:
                    lake_dict[lake] = area + 1
                maxArea = max(lake_dict[lake], maxArea)
if not lake_dict:
    if grid[0][0] == 1:
        maxArea = row_len * col_len

print(maxArea)