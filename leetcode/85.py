# -*- coding: utf-8 -*-
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

maxarea = 0

dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "0": continue
        else:
            width = dp[i][j] = dp[i][j-1] + 1 if j else 1
        
        for k in range(i, -1 ,-1 ):
            width = min(dp[k][j], width)
            maxarea = max(maxarea, width * (i - k + 1))

ans = maxarea
            