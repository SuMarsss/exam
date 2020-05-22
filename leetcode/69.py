x = 8
h = x
l = 1

while 1:
    mid = (h + l) // 2
    if mid ** 2 > x:
        h = mid
    elif mid ** 2 < x:
        l = mid
    else:
        print(mid)
        break
    if h - l <=1:
        print(mid)
        break