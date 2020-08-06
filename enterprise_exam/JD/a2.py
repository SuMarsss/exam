def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))

def reverse(x):
    return str(x)[::-1]

def main():
    # N,M = list(map(int, input().split()))
    N, M = 101, 120
    res = 0
    yes = set()
    no  = set()
    for n in range(N,M+1):
        sn = str(n)
        tmp = [sn[:i]+sn[i+1:] for i in range(len(sn))]
        for j in tmp:
            j = int(j)
            if j in yes:
                res +=1
                break
            elif j in no:
                continue
            else:
                if str(j) == reverse(j) and is_prime(j):
                    res += 1
                    yes.add(j)
                    break
                else:
                    no.add(j)
    print(res)
if __name__ == '__main__':
    main()

