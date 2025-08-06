# https://codeforces.com/problemset/problem/1362/A
import math
T = int(input())
for _ in range(T):
    a,b = list(map(int, input().split()))
    if a<b: a,b=b,a
    if a%b==0 and (a==b or (a//b&((a//b)-1))==0):
        if a==b:
            print(0)
        else:
            val=a//b
            res = int(math.log2(val))
            print((res+2)//3)
    else:
        print(-1)