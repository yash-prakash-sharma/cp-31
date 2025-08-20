# https://codeforces.com/problemset/problem/1872/D
import math
T = int(input())
for _ in range(T):
    n,x,y = list(map(int, input().split()))
    fq1=n//x
    fq2=n//y
    common=(x*y)//math.gcd(x,y)
    if common<=n:
        common=n//common
    else:
        common=0
    common=min(common, min(fq1,fq2))
    fq1-=common
    fq2-=common
    val1,val2=0,0
    if fq1>0: val1=(n*(n+1))//2-((n-fq1)*(n-fq1+1))//2
    if fq2>0: val2=(fq2*(fq2+1))//2
    print(val1-val2)