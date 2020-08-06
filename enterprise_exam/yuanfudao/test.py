
N = int(input())
awards = []
start = 0
for i in range(N):
    c = list(map(int, input().split()))
    if c[1] != 0:
        c[1] -= 2
    else:
        c[1] = -1
    awards.append(c)

sent = dict()
for i, award in enumerate(awards):
    if award[1] != -1:
        sent[award[1]] = sent.setdefault(award[1], [])
        sent[award[1]].append(i)

last = set()
for i in range(N):
    if i not in sent:
        last.add(i)

res = []


def helper(i):
    if i in last:
        a = awards[i][0]
        res.append(a)
        return a

    son = sent[i]
    a = [helper(j) for j in son]
    b = []
    for ason in a:
        if ason > 0:
            b.append(ason)
    if b:
        res.append(awards[i][0] + sum(b))
        return awards[i][0] + sum(b)
    else:
        res.append(awards[i][0])
        return awards[i][0]


helper(start)
# print(res)
print(max(res))
# print(sent)
# print(last)