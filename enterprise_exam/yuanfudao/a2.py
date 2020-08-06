# N = int(input())
# nums = []
# for _ in range(N):
#     v, name = list(map(int,input().split()))
#     nums.append([v,name])

nums  = [
    [2,0],
    [1,2],
    [-1,2],
    [3,4],
    [-2,4],
    [-1,5],
]
N=len(nums)
adj_list = [[[],[]] for _ in range(N)]
for i, (v,name) in enumerate(nums):
    if name == 0:
        adj_list[i][0] = v
        root = i
    else:
        adj_list[name-2][1].append(i)
        adj_list[i][0] = v
ans = 0
ha = dict()
def dfs(i):
    global ans, adj_list
    child = adj_list[i][1]
    if i in ha:
        return ha[i]
    if not child:
        ha[i] = adj_list[i][0]
        ans = max(ans, ha[i])
        return ha[i]
    else:
        tmp = adj_list[i][0]
        for nxt_i in child:
            tmp = tmp + dfs(nxt_i) if dfs(nxt_i)>0 else tmp
        ha[i] = tmp
        ans = max(ans, ha[i])
        return ha[i]

dfs(root)
print(ans)