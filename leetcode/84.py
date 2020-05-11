# -*- coding: utf-8 -*-
heights = [2,1,5,6,2,3]
llen = len(heights)
maxArea = heights[0]
for i in range(llen):
    h = heights[i]
    for left in range(i,-1,-1):
        h = min(heights[left], h)
        maxArea = max(maxArea, h*(i - left + 1))


ans =  maxArea
