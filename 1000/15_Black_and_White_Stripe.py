# https://codeforces.com/problemset/problem/1690/D
T = int(input())
for _ in range(T):
    n,k = list(map(int, input().split()))
    s = input()
    res=k
    cnt=0
    for i in range(n):
        cnt+=s[i]=='B'
        if i>=k:
            cnt-=s[i-k]=='B'
        if i>=k-1:
            res=min(res,k-cnt)
    print(res)