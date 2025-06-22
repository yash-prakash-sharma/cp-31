# https://codeforces.com/problemset/problem/1850/D
T = int(input())
for _ in range(T):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort()
    res=1
    cur=1
    for i in range(1,n):
        if abs(a[i]-a[i-1])<=k:
            cur+=1
            res=max(res,cur)
        else:
            cur=1
    print(n-res)