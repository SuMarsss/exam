# S = input()
# n = int(input())
S = "    ca     dog satdsfs   "
n = 4
i = 0

while S:
    if len(S) == n:
        if S.endswith(" "):
            print("{" + S.strip() + " }")
            S = ''
        else:
            print("{" +S[:n-1]+ "-}")
            S = S[n-1:]
    elif len(S) > n:
        t = S[:n]
        if t.endswith(" "):
            print("{" + t.strip() + " }")
            S = S[n:]
            S = S.strip()
        else:
            if t[n-2] == " ":
                print("{" +t[:n-1]+ "}")
                S = S[n-1:]
            else:
                print("{" +t[:n-1]+ "-}")
                S = S[n-1:]
    elif len(S) < n:
        print("{" + S + "}")
        S = ""




