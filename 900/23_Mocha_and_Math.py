# https://codeforces.com/problemset/problem/1559/A
T = int(input())
for _ in range(T):
    n=int(input())
    a=list(map(int, input().split()))
    res=a[0]
    for x in a:
        res&=x
    print(res)
