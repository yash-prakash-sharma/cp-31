# https://codeforces.com/problemset/problem/1794/B
T=int(input())
for _ in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    if a[0]==1:
        a[0]+=1
    for i in range(1,n):
        if a[i]==1 and i!=n-1:
            a[i]+=1
        if a[i]%a[i-1]==0:
            a[i]+=1
    print(*a)
        