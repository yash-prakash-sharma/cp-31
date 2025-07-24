# https://codeforces.com/problemset/problem/1666/D
T = int(input())
for _ in range(T):
    s,t = input().split()
    isVisited = [False]*26
    s_ind,t_ind = len(s)-1,len(t)-1
    while t_ind>=0 and s_ind>=0:
        if isVisited[ord(t[t_ind])-ord('A')]:
            break
        if s[s_ind]==t[t_ind]:
            t_ind-=1
        # to check if character exists at right side since we can't remove in this case
        else:
            isVisited[ord(s[s_ind])-ord('A')]=True
        s_ind-=1
    print("YES" if t_ind==-1 else "NO")