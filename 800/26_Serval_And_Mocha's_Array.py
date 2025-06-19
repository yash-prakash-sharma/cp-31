# https://codeforces.com/problemset/problem/1789/A
import math
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    res=False
    for i in range(0,n):
        for j in range(i+1,n):
            factor=math.gcd(a[i],a[j])
            if factor<=2:
                res=True
                break
    if res:
        print("YES")
    else:
        print("NO")