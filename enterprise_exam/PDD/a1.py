def a1_res(N,K):
    h, cur_v,tot= 0,1,1
    while tot < N:
        t = min(cur_v, K)
        tot += t
        h += 1
        cur_v = tot
    return h

N,K =  list(map(int,input().split()))
print(a1_res(N,K))

