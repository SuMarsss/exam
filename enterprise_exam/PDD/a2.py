N,M =  list(map(int,input().split()))
P = list(map(int,input().split()))
D = [0] * M
res = ""
for i in range(M):
    D[i] = list(map(int,input().split()))

from heapq import *
from collections import deque
outdegree = [0 for _ in range(N)]
adjacency = [deque() for _ in range(N)]
queue = []


for pre, cur in D:
    outdegree[cur-1] += 1
    adjacency[pre-1].appendleft( cur-1)

for i in range(len(outdegree)):
    if not outdegree[i]: heappush(queue, i)

while queue:
    pre = queue.pop()
    res = res+" "+str(pre+1)
    N -= 1
    for cur in adjacency[pre]:
        outdegree[cur] -= 1
        if not outdegree[cur]:
            heappush(queue, cur)

print(res)
