# https://codeforces.com/problemset/problem/1742/E
import bisect
T = int(input())
for _ in range(T):
    n,q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    q = list(map(int, input().split()))
    pre = [0]*n
    pmax = [0]*n
    pre[0]=a[0]
    pmax[0]=a[0]
    for i in range(1,n):
        pre[i]=pre[i-1]+a[i]
        pmax[i]=max(a[i],pmax[i-1])
    for val in q:
        ind=bisect.bisect_right(pmax,val)-1
        if ind<0:
            print(0, end=' ')
        else:
            print(pre[ind], end=' ')
    print()