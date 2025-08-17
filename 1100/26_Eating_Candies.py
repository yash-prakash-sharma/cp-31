# https://codeforces.com/problemset/problem/1669/F
T = int(input())
for _ in range(T):
    n = int(input())
    w = list(map(int, input().split()))
    suf = {}
    res,sum=0,0
    for i in range(n-1,0,-1):
        sum+=w[i]
        suf[sum]=i
    sum=0
    for i in range(n):
        sum+=w[i]
        if suf.get(sum,-1)>i:
            res=max(res,i+1+n-suf.get(sum))
    print(res)