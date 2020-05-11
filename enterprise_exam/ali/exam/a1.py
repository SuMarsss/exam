T = int(input())

for _ in range(T):
    [n,m,a,b] = list(map(int,input().split()))
    if b==1:
        print(min(n//a,m))
        continue
    if n<a:
        print(0)
        continue
    elif n==a:
        print(min(b,m))
        continue
    if n*b>=m*a:
        print(m)
    else:
        print(n*b//a)


#if __name__ == "__main__":
#    T = int(input())
#    ret = [] 
#    def woodman(n, m, a, b): 
#        if n < a: return 0  
#        if n == a: return b 
#        if (n - a) * b // a + b > m: 
#            return m 
#        else: return (n - a) * b // a + b 
#        for count in range(T):
#            tmp = list(map(int, input().split(' ')))
#            ret.append(woodman(tmp[0], tmp[1], tmp[2], tmp[3])) 
#            for qq in range(len(ret)): 
#                print(ret[qq])
                
