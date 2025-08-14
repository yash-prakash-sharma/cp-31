# https://codeforces.com/problemset/problem/1826/B
import math
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    i,j=0,n-1
    res=abs(a[i]-a[j])
    while i<j:
        if a[i]!=a[j]:
            res=math.gcd(abs(a[i]-a[j]),res)
            pal=False
        i+=1
        j-=1
    print(res)