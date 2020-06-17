# S = input()
S= " AA EE   DEEOO"
word_Dict = list("AEIOU")
word_set = set(word_Dict)
res = ""
i = 0
while i <= len(S) -1:
    if S[i] in word_set:

        if i >= 1 and S[i-1] ==" ":
            t = S[i]
        elif i == 0:
            t = S[i]
        else:
            t = S[i].lower()

        i += 1
    else:
        if i >= 1 and S[i-1] ==" ":
            t = S[i].upper()
        elif i == 0:
            t = S[i].upper()
        else:
            t = S[i]
    res = res + t
    i += 1
print(res)


