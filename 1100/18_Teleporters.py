# hhttps://codeforces.com/problemset/problem/1791/G1
T = int(input())
for _ in range(T):
    n,c = list(map(int, input().split()))
    a = list(map(int,input().split()))
    for i in range(n):
        a[i]+=i+1
    a.sort()
    i=0
    while i<n and c-a[i]>=0:
        c-=a[i]
        i+=1
    print(i)