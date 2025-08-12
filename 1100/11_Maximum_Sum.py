# https://codeforces.com/problemset/problem/1832/B
import math
T = int(input())
for _ in range(T):
    n,k = list(map(int, input().split()))
    a = list(map(int,input().split()))
    a.sort()
    pre = [0]*(n+1)
    for i in range(1,n+1):
        pre[i]=pre[i-1]+a[i-1]
    s=0
    l,r=0,k
    for i in range(k+1):
        val=pre[n]-(pre[n]-pre[n-i])-(pre[2*(k-i)])
        s=max(s,val)
    print(s)