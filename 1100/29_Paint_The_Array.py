# https://codeforces.com/problemset/problem/1618/C
import math
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    val1,val2=a[0],a[1]
    for i in range(0,n):
        if i&1:
            val2=math.gcd(val2,a[i])
        else:
            val1=math.gcd(val1,a[i])
    for i in range(0,n):
        if i&1 and val1!=0 and a[i]%val1==0: val1=0
        elif (i&1)==0 and val2!=0 and a[i]%val2==0: val2=0
    
    print(val2) if val2!=0 else print(val1)