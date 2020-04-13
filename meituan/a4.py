# -*- coding: utf-8 -*-
n = 5
a, b = 1, 0
for i in range(1, n + 1):
    if i % 2 == 1:
        a = (3 * b) % 1000000007
        b = a + 1
    else:
        a = (3 * b) % 1000000007
        b = a - 1
print(a)
