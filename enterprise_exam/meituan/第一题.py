

n = 5
start = [5, 3, 1, 4, 2]
end = [2, 4, 5, 1, 3]
 
res = 0
idx1, idx2 = 0, 0
s = set()
while idx1 < n:
    if start[idx1] in s:
        idx1 += 1
        continue
    while end[idx2] != start[idx1]:
        res += 1
        s.add(end[idx2])
        print(s)
        idx2 += 1
    idx1 += 1
    idx2 += 1
print(res)