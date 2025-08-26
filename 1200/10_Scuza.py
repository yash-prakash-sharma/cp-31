# https://codeforces.com/problemset/problem/1742/E
import bisect
T = int(input())
for _ in range(T):
    n,q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    q = list(map(int, input().split()))
    pre = [0]*n
    m={}
    pre[0]=a[0]
    for i in range(1,n):
        pre[i]=pre[i-1]+a[i]
    maxi=0
    for i in range(n):
        maxi=max(a[i],maxi)
        m[maxi]=i
    keys = sorted(m)
    for val in q:
        ind=bisect.bisect_right(keys,val)-1
        if ind<0:
            print(0, end=' ')
        else:
            print(pre[m[keys[ind]]], end=' ')
    print()