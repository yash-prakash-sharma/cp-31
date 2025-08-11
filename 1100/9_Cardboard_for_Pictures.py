# https://codeforces.com/problemset/problem/1850/E
import math
T = int(input())
for _ in range(T):
    n,c = list(map(int, input().split()))
    s = list(map(int,input().split()))
    l,r=1,int(math.sqrt(c))
    while l<=r:
        res=(l+r)>>1
        sum=0
        for x in s:
            sum+=(x+2*res)*(x+2*res)
        if sum<=c: l=res+1
        else: r=res-1
    print(r)