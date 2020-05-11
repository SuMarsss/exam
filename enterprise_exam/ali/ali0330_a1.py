from queue import PriorityQueue


N = [5,4,7,9]
K = 2
M = 3

def solution(N,K,M):
    pq = PriorityQueue()
    for i in N:
        pq.put(-i)
    for j in range(M):
        for i in range(len(pq.queue)):
            pq.queue[i] += -K
        t = pq.get()
        t = t + t//(-2)
        pq.put(t)

    ans = 0
    while not pq.empty():
        ans += pq.get()
    ans = - ans
    print(ans)


def solution(N, K, M):
    pq = PriorityQueue()
    for i in N:
        pq.put(-i)
    for j in range(M):

        t = pq.get()
        t = t + (t-K)// (-2)
        pq.put(t)
    ans = 0
    while not pq.empty():
        ans += pq.get()
    ans = - ans
    ans += M*K*len(N)
    print(ans)

N= input()
K = input()
M = input()

N = list(map(int, input().split()))
K = input()
M = input()

