# https://codeforces.com/problemset/problem/1904/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    mp = {}
    sorted_a = sorted(a)
    prefix=[0]*(n+1)
    res = [0]*n
    for i in range(n):
        prefix[i+1]=prefix[i]+sorted_a[i]
    res[n-1]=n-1
    mp[sorted_a[n-1]]=res[n-1]
    for i in range(n-2,-1,-1):
        if prefix[i+1]>=sorted_a[i+1]: res[i]=res[i+1]
        else: res[i]=i
        mp[sorted_a[i]]=res[i]
    for i in range(n):
        res[i]=mp[a[i]]
    print(*res)