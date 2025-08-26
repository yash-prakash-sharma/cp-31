# https://codeforces.com/problemset/problem/1729/D
import bisect
T = int(input())
for _ in range(T):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    a = [0]*n
    fq_pos,zero_cnt=0,0
    for i in range(n):
        a[i]=y[i]-x[i]
    a.sort()
    l,r,res=0,n-1,0
    while l<r:
        if a[l]+a[r] >=0:
            res+=1
            l+=1
            r-=1
        else:
            l+=1
    print(res)
