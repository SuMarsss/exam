
T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split(' ')))
    sets = []
    for i in range(1, N + 1):
        sets.append(set([i]))
    for i in range(M):
        ops = list(map(int, input().split(' ')))
        op = ops[0]
        nums = ops[1:]
        if op == 3:
            num = nums[0]
            for iset in sets:
                if num in iset:
                    print(len(iset))
        elif op == 1:
            X, Y = nums[0], nums[1]
            record_1 = 0
            record_2 = 0
            for idx in range(len(sets)):
                if X in sets[idx]:
                    set_1 = sets[idx]
                    record_1 = idx
                if Y in sets[idx]:
                    set_2 = sets[idx]
                    record_2 = idx
            set_1 = set_1 | set_2
            sets[record_1] = set_1
            if record_1!=record_2:
                del sets[record_2]
        else:
            num = nums[0]
            flag = False
            for iset in sets:
                if num in iset:
                    if len(iset) > 1:
                        iset.discard(num)
                        flag = True
            if flag:
                sets.append(set([num]))

