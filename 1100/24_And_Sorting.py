# https://codeforces.com/problemset/problem/1682/B
T = int(input())
for _ in range(T):
    n = int(input())
    p = list(map(int,input().split()))
    res=(1<<31)-1
    for i in range(n):
        if p[i]!=i :
            res&=(p[i]&i)
    print(res)