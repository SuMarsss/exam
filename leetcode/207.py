"""
# data: 2020年6月6日16:28:23
# 思路  从终点考虑  **依次弹出所有入度为0的节点**
# 1. 构建数据结构--出度list，索引为节点名，值为入度，每次弹出节点后，对应的值--
# 2. 构建倒排连接表--adj_list，索引为终点，值为起始点， 每次弹出终点后，追踪起始点

method:
1. 弹出入度为0的node：cur
2. cur 下游的node入度-1
3. if cur 下游的node入度减为0了，入栈
"""
numCourses = 5
prerequisites = [[0, 1], [0, 3], [1, 3], [1, 2], [2, 4], [3, 4]]
numCourses = 3
prerequisites =[[1,0]]
# # ------------------------------------------------- #
# from collections import deque
#
# outdegree = [0 for _ in range(numCourses)]
# adjacency = [[] for _ in range(numCourses)]
# queue = deque()
# # Get the outdegree and adjacency of every course.
# for cur, pre in prerequisites:
#     outdegree[cur] += 1
#     adjacency[pre].append(cur)
# # Get all the courses with the outdegree of 0.
# for i in range(len(outdegree)):
#     if not outdegree[i]: queue.append(i)
#
# while queue:
#     pre = queue.popleft()
#     numCourses -= 1
#     for cur in adjacency[pre]:
#         outdegree[cur] -= 1
#         if not outdegree[cur]:
#             queue.append(cur)
#
# print(numCourses)

## method2 从入度考虑 **依次删除起始点**
## 1. 构建入度list 索引为节点，值为入度值， 每次弹出节点， 入度值--
## 2. 构建adj边list，索引为起始点，值为终点，每次弹出节点，追踪终点，终点的入度值--

indegrees = [0 for _ in range(numCourses)]
adj_list = [[] for _ in range(numCourses)]
li = list()
for cur,nxt in prerequisites:
    indegrees[nxt] += 1
    adj_list[cur].append(nxt)

for cur in range(len(indegrees)):
    if not indegrees[cur] :
        li.append(cur)

while li:
    cur = li.pop(0)
    numCourses -= 1
    for nxt in adj_list[cur]:
        indegrees[nxt] -= 1
        if not indegrees[nxt]:
            li.append(nxt)

print(numCourses)
