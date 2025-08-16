# https://codeforces.com/problemset/problem/1742/D
import math
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    m = {}
    res=-1
    for i in range(n):
        m[a[i]]=i+1
    for x in range(1,1001):
        for y in range(1,1001):
            if math.gcd(x,y)==1 and m.get(x,-1)!=-1 and m.get(y,-1)!=-1:
                res=max(res,m[x]+m[y])
    print(res)