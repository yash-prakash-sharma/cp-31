#https://codeforces.com/problemset/problem/1726/A
T = int(input())
for _ in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    if n==1:
        print(0)
        continue
    res=max(max(a[1:])-a[0],a[n-1]-min(a[:n-1]))
    for i in range(n-1):
        res=max(res,a[i]-a[i+1])
    print(res)