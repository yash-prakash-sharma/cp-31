# https://codeforces.com/problemset/problem/1891/B
mod=1000000007
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    i,j=0,0
    res=1
    poss=True
    while poss and j<n:
        while i<n and a[i]>b[j]:
            i+=1
        if i==0: poss=False
        res=(res*(i-j))%mod
        j+=1
    print(res) if poss else print(0)