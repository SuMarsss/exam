import copy
def search_zero(s):
    if not s:
        print("No")
        return False
    pastSeq=[]
    def check_repeat(subS):
        ls = len(subS)
        chongfu_flag = 0
        for seq in pastSeq:
            if seq == subS:
                chongfu_flag = 1
                break                 
            for j in range(ls): # 回文检测
                # print(seq[j], subS[ls-1-j],seq[j] != subS[ls-1-j])
                if seq[j] != subS[ls-1-j]: # 不是回文
                    break
                if j == ls-1:
                    chongfu_flag = 1 # 遍历完seq，置1
        return chongfu_flag    
    print(check_repeat(s))
    
    l = len(s)
    c = 1
    iList = []
    iList.append((0,l-1,copy.deepcopy(s),c))
    pastSeq.append(copy.deepcopy(s))

    count = 1
    tot = (2**(2*l))
    while 1:
        if count > tot  or iList == []:
            break
        count += 1
        l_ind,h_ind,s,c = iList.pop(0)
        print(l_ind,h_ind,s)
        temp_s = copy.deepcopy(s)
        for i in range(l_ind,h_ind):
            s = copy.deepcopy(temp_s)
            print("s",s,"i",i)
            s[i] =  1 if s[i]==0 else 0
            if i-1 >= 0 :
                s[i-1] = 1 if s[i-1]==0 else 0
            if i+1 < l:
                s[i+1] = 1 if s[i+1]==0 else 0
            if s == [0]*l:
                print("YES",c,count)
                return True
            if check_repeat(s) == 1:
                continue
            else:
                if i-1 >= 0 :   iList.append((0,i,copy.deepcopy(s),c+1))
                if i+1 < l:     iList.append((i+1,l,copy.deepcopy(s),c+1))
                pastSeq.append(copy.deepcopy(s))
            print(s,i)
    print("NO. time_out")
    return False

s = "11000"
s = list(map(int,s))
search_zero(s)