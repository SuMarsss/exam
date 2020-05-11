# -*- coding: utf-8 -*-
matrix =[["0","1"],["1","0"]]

def maxWidth(widths):
    if not widths:
        return 0
    maxArea = 0
    w_len = len(widths)
    stack = [-1]
    for row_i in range(w_len):
        while stack[-1] != -1 and widths[row_i] <= widths[stack[-1]]:
            maxArea = max(maxArea, widths[stack.pop()] * (row_i - stack[-1] -1))
        stack.append(row_i)

    while stack[-1] != -1:
        maxArea = max(maxArea,  widths[stack.pop()] * (row_i - stack[-1] ))
    return maxArea

maxArea = 0

row_len = len(matrix)
col_len = len(matrix[0])
dp = [0] * len(matrix[0])
for i in range(row_len):
    for j in range(col_len):
        if matrix[i][j] == "1":
            dp[j] = dp[j] + 1
        else:
            dp[j] = 0
    maxArea = max(maxArea, maxWidth(dp))

ans = maxArea

