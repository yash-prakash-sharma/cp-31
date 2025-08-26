# https://codeforces.com/problemset/problem/1808/B
T = int(input())
for _ in range(T):
    n,m = list(map(int,input().split()))
    c = [[0]*n for _ in range(m)]
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            c[j][i] = row[j]
    res=0
    if n==1:
        print(res)
        continue
    for i in range(m):
        c[i].sort()
        for j in range(n):
            res+=j*c[i][j]
            res-=(n-j-1)*c[i][j]
    print(res)