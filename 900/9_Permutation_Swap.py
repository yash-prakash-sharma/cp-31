# https://codeforces.com/problemset/problem/1828/B
import math
T = int(input())
for _ in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    res=a[0]-1
    for i in range(2,n+1):
        res=math.gcd(res,abs(a[i-1]-i))
    print(res)