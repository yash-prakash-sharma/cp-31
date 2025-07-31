# https://codeforces.com/problemset/problem/1765/M
import math
T = int(input())
for _ in range(T):
    n = int(input())
    if n&1:
        i=3
        res=n-1
        val1,val2=1,n-1
        while i*i<=n:
            if n%i==0:
                cur_res=math.lcm(n//i,n-(n//i))
                if cur_res<res:
                    val1=n//i
                    val2=n-val1
                    res=cur_res
            i+=2
        print(val1, val2)
    else:
        print(n//2, n//2)