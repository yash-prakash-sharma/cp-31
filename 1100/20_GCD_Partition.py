# https://codeforces.com/problemset/problem/1780/B
import math
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    pre_sum,res=0,1
    suf_sum=sum(a)
    for i in range(n-1):
        pre_sum+=a[i]
        suf_sum-=a[i]
        res=max(res,math.gcd(pre_sum, suf_sum))

    print(res)