# https://codeforces.com/problemset/problem/1820/B
T = int(input())
for _ in range(T):
    n=int(input())
    c = list(map(int, input().split()))
    c.sort()
    flag=True
    if c[0]!=1: flag=False
    if flag:
        sum=a[0]
        for i in range(n):
            if a[i]>sum:
                flag=False
                break
            sum+=a[i]
    print("YES") if flag else print("NO")