# -*- coding: utf-8 -*-
heights = [1,1,3,1]

stack = [-1]

maxarea = 0
for i in range(len(heights)):

    while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
        maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
    stack.append(i)

while stack[-1] != -1:
    maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
ans =  maxarea
